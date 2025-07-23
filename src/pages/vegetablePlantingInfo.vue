<template>
  <v-row>
    <v-col cols="5" id="selected-vegetable">
      <div class="sticky-card">
        <VegetableCard
          :vegetable-image-url="selectedVegetable?.image_url"
          :vegetable-name="selectedVegetable?.name"
          :vegetable-id="selectedVegetable?.id"
          :estimated-harvest-time="selectedVegetable?.estimated_harvest_time_formatted"
          :watering-frequency="selectedVegetable?.watering_frequency_formatted"
          :amount-of-sunlight="selectedVegetable?.amount_of_sunlight"
          :button-route="`/vegetablePlantingChecklist/`"
          width="360"
        >
          <template #button-text>Let's grow</template>
        </VegetableCard>
      </div>
    </v-col>
    <v-col cols="7" id="planting-guide">
      <div class="how-to-grow">
        <h2>How to grow</h2>
        <ol>
          <li>Choose a container or garden bed with good drainage.</li>
          <li>Fill with nutrient-rich, moist soil or compost.</li>
          <li>Sow seeds or plant cuttings about 1–2 inches deep.</li>
          <li>Keep the soil consistently moist, but not waterlogged.</li>
          <li>
            Place in an area receiving full sunlight (at least 6 hours daily).
          </li>
          <li>
            Harvest in 4–6 weeks by cutting the stems just above soil level,
            leaving roots intact for regrowth.
          </li>
        </ol>
      </div>
      <div class="what-you-need">
        <h2>What you'll need</h2>
        <MaterialsCard
          v-for="material in uniqueMaterials"
          :key="material.id"
          :materialImageUrl="material.image"
          :materialName="material.name"
          :materialDescription="material.description"
          class="mb-4"
        >
        </MaterialsCard>
      </div>
      <div class="where-to-buy">
        <h2>Where to buy</h2>
        <WhereToBuyCard></WhereToBuyCard>
      </div>
      <div class="videos">
        <h2>Videos for you</h2>
        <VideoCard></VideoCard>
      </div>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import { computed, onMounted } from "vue";
import { useVegetablesStore } from "@/stores/vegetable";
import VegetableCard from "@/components/VegetableCard.vue";
import MaterialsCard from "../components/MaterialsCard.vue";
import WhereToBuyCard from "@/components/WhereToBuyCard.vue";
import VideoCard from "../components/VideoCard.vue";

const vegetableStore = useVegetablesStore();
const { selectedVegetable } = storeToRefs(vegetableStore);

onMounted(async () => {
  if (!vegetableStore.materials.length) {
    await vegetableStore.getMaterials();
  }
});

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
  top: 32px; /* Adjust as needed for your header */
  z-index: 2;
}
</style>
