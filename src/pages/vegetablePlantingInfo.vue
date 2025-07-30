<template>
  <v-row>
    <v-col cols="5" id="selected-vegetable">
      <div class="sticky-card">
        <VegetableChecklistCard :vegetable-image-url="selectedVegetable?.image_url"
          :vegetable-name="selectedVegetable?.name" :vegetable-id="selectedVegetable?.id"
          :estimated-harvest-time="selectedVegetable?.estimated_harvest_time_formatted"
          :watering-frequency="selectedVegetable?.watering_frequency_formatted"
          :amount-of-sunlight="selectedVegetable?.amount_of_sunlight" width="360">
        </VegetableChecklistCard>
      </div>
    </v-col>
    <v-col cols="7" id="planting-guide">
      <div class="how-to-grow mb-5">
        <h2 class="mb-2">How to grow:</h2>
        <v-card class="d-flex ga-4 pa-4 rounded-lg align-start" elevation="0">
          <div class="d-flex flex-column">
            <v-card-text class="pa-0">
              <ol class="instructions-list pl-6">
                <li v-for="(instruction, index) in plantingInstructions" :key="index" class="mb-2 pl-2">
                  {{ instruction }}
                </li>
              </ol>
            </v-card-text>
          </div>
        </v-card>
      </div>
      <div class="what-you-need mb-5">
        <h2 class="mb-2">What you'll need:</h2>
        <template v-if="uniqueMaterials.length">
          <MaterialsCard v-for="material in uniqueMaterials" :key="material.id" :materialImageUrl="material.image"
            :materialName="material.name" :materialDescription="material.description" :materialType="material.type"
            class="mb-4">
          </MaterialsCard>
        </template>
        <template v-else>
          <div class="ml-2 text-grey">No materials found for this vegetable.</div>
        </template>
      </div>
      <div class="where-to-buy mb-2">
        <h2>Where to buy:</h2>
        <p class="mb-2">We've found the nearest stores to you according to your location:
          <v-chip color="primary" size="large" rounded="pill">
            Petaling Jaya
          </v-chip>
        </p>
        <WhereToBuyCard v-for="(store, index) in stores" :key="index" :store-name="store.name"
          :store-description="store.description" :store-image="store.img" :store-link="store.link" class="mb-4">
        </WhereToBuyCard>
      </div>
      <div class="videos mb-5">
        <h2 class="mb-2">Videos for you:</h2>
        <VideoCard v-for="(video, index) in videos" :key="index" :video-title="video.title"
          :video-summary="video.summary" :video-thumbnail="video.thumbnail" :video-link="video.link" class="mb-4">
        </VideoCard>
      </div>
      <div class="mb-5">
        <CallToActionButton :to="`/vegetablePlantingChecklist/`">
          LET'S GROW!
        </CallToActionButton>
      </div>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import { computed, onMounted } from "vue";
import { useVegetablesStore } from "@/stores/vegetable";
import VegetableChecklistCard from "@/components/VegetableChecklistCard.vue";
import MaterialsCard from "../components/MaterialsCard.vue";
import WhereToBuyCard from "@/components/WhereToBuyCard.vue";
import VideoCard from "../components/VideoCard.vue";
import CallToActionButton from "@/components/CallToActionButton.vue";

const vegetableStore = useVegetablesStore();
const { selectedVegetable } = storeToRefs(vegetableStore);

onMounted(async () => {
  if (!vegetableStore.materials.length) {
    await vegetableStore.getMaterials();
  }
});

const plantingInstructions = [
  "Choose a container or garden bed with good drainage.",
  "Fill with nutrient-rich, moist soil or compost.",
  "Sow seeds or plant cuttings about 1–2 inches deep.",
  "Keep the soil consistently moist, but not waterlogged.",
  "Place in an area receiving full sunlight (at least 6 hours daily).",
  "Harvest in 4–6 weeks by cutting the stems just above soil level, leaving roots intact for regrowth.",
];

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

const videos = [
  {
    title: "Gardening 101: How To Start A Garden 🥕",
    summary:
      "A beginner's guide to starting your own garden, from choosing a location to planting your first seeds.",
    thumbnail: "https://img.youtube.com/vi/X3SP1Fub3bw/hqdefault.jpg",
    link: "https://www.youtube.com/watch?v=X3SP1Fub3bw",
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
.instructions-list {
  list-style-position: outside;
}
</style>
