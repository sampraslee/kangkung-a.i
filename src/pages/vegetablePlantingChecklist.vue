<template>
  <v-row>
    <!-- Column 1 -->
    <v-col cols="5" id="selected-vegetable">
      <div class="sticky-card">
        <VegetableChecklistCard
          :vegetable-image-url="selectedVegetable?.image_url"
          :vegetable-name="selectedVegetable?.name"
          :vegetable-id="selectedVegetable?.id"
          :estimated-harvest-time="selectedVegetable?.estimated_harvest_time_formatted"
          :watering-frequency="selectedVegetable?.watering_frequency_formatted"
          :amount-of-sunlight="selectedVegetable?.amount_of_sunlight"
          width="360"
        >
        </VegetableChecklistCard>
      </div>
    </v-col>

    <!-- Column 2 -->
    <!-- Instructions -->
    <v-col cols="7" id="planting-guide">
      <div class="instructions mb-4">
        <h1 class="mb-4">Are you ready to start growing?</h1>
      </div>

      <!-- Materials -->
      <div class="what-you-need">
        <h2 class="mb-4">What you'll need:</h2>
        <ChecklistItemCard
          v-for="material in uniqueMaterials"
          :key="material.id"
          :materialImageUrl="material.image || 'https://placehold.co/40@3x.png'"
          :materialName="material.name"
          :materialType="material.type"
          :materialDescription="material.description"
        >
        </ChecklistItemCard>
      </div>

      <!-- Where To Buy -->
      <div class="where-to-buy mb-5">
        <h2 class="mb-4">Where to buy:</h2>
        <WhereToBuyCard
          v-for="(store, index) in stores"
          :key="index"
          :store-name="store.name"
          :store-description="store.description"
          :store-image="store.img"
          :store-link="store.link"
          class="mb-4"
        >
        </WhereToBuyCard>
      </div>

      <!-- Calendar -->
      <div>
        <h2 class="mb-4">When would you like to start planting?</h2>
        <Calendar class="mb-5"></Calendar>
      </div>

      <!-- Call to Action Button -->
      <CallToActionButton :to="`/`" class="mb-4">
        I'm ready to plant
      </CallToActionButton>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import { computed, onMounted } from "vue";
import { useVegetablesStore } from "@/stores/vegetable";
import VegetableChecklistCard from "@/components/VegetableChecklistCard.vue";
import Calendar from "@/components/Calendar.vue";
import ChecklistItemCard from "@/components/ChecklistItemCard.vue";
import WhereToBuyCard from "@/components/WhereToBuyCard.vue";
import CallToActionButton from "@/components/CallToActionButton.vue";

const vegetableStore = useVegetablesStore();
const { selectedVegetable } = storeToRefs(vegetableStore);

onMounted(async () => {
  if (!vegetableStore.materials.length) {
    await vegetableStore.getMaterials();
  }
});

const stores = [
  {
    name: "Damansara Nursery",
    description: "Wholesale Plant Nursery",
    link: "https://maps.app.goo.gl/mmhvppr8CP88adEE9",
    img: "/images/vegestores/damansara_nursey.png",
  },
  {
    name: "54 Weng Thye Nursery & Landscapes",
    description: "Plant Nursery",
    link: "https://maps.app.goo.gl/SSyyVxthNQAtbajb6",
    img: "/images/vegestores/weng_thye.png",
  },
  {
    name: "Katsura Garden Centre",
    description: "Plant Nursery",
    link: "https://maps.app.goo.gl/j5poP3JQsSmRTVdVA",
    img: "/images/vegestores/katsura.png",
  },
];

const selectedVegetableId = computed(
  () => vegetableStore.selectedVegetable?.id
);

const uniqueMaterials = computed(() =>
  selectedVegetableId.value
    ? vegetableStore.getUniqueMaterialsForVegetable(selectedVegetableId.value)
    : []
);
</script>

<style scoped>
.sticky-card {
  position: sticky;
  top: 32px;
  /* Adjust as needed for your header */
  z-index: 2;
}
</style>
