<template>
  <v-img :src="vegetableStore.selectedVegetable.image_url"></v-img>

  <!-- Kangkung Info -->
  <div class="vegetable-info bg-accent pa-4 rounded-lg mb-6">
    <h3 class="mb-4">{{ vegetableStore.selectedVegetable.name }}</h3>
    <v-chip prepend-icon="mdi-clock-time-four-outline" variant="text" class="mb-3">
      Estimated time to harvest:
      <span :style="{ marginLeft: '4px', fontWeight: 600 }" v-html="
          vegetableStore.selectedVegetable.estimated_harvest_time_formatted
        "></span>
    </v-chip>
    <v-chip prepend-icon="mdi-water-outline" variant="text" class="mb-3">
      Watering frequency:
      <span :style="{ marginLeft: '4px', fontWeight: 600 }"
        v-html="vegetableStore.selectedVegetable.watering_frequency_formatted"></span>
    </v-chip>
    <v-chip prepend-icon="mdi-weather-sunny" variant="text">
      Amount of sunlight:
      <span :style="{ marginLeft: '4px', fontWeight: 600 }"
        v-html="vegetableStore.selectedVegetable.amount_of_sunlight"></span>
    </v-chip>
  </div>

  <!-- How to grow -->
  <section id="planting-instructions" class="mb-6">
    <h3>How to grow</h3>
    <v-container class="ps-8">
      <ol>
        <li class="mb-2">Choose a container or garden bed with good drainage.</li>
        <li class="mb-2">Fill with nutrient-rich, moist soil or compost.</li>
        <li class="mb-2">Sow seeds or plant cuttings about 1-2 inches deep.</li>
        <li class="mb-2">Keep the soil consistently moist, but not waterlogged.</li>
        <li class="mb-2">Place in an area receiving full sunlight (at least 6 hours daily).</li>
        <li>Sow seeds or plant cuttings about 1-2 inches deep.</li>
      </ol>
    </v-container>
  </section>

  <!-- What you'll need -->
  <section id="materials-needed" class="mb-6">
    <h3 class="mb-4">What you'll need</h3>
    <MaterialsCard v-for="material in uniqueMaterials" :key="material.id"
      :materialImageUrl="material.image || 'https://placehold.co/40@3x.png'" :materialName="material.name"
      :materialDescription="material.description">
    </MaterialsCard>
  </section>

  <!-- Videos for you  -->
  <section id="relevant-videos" class="mb-6">
    <h3 class="mb-6">Videos for you</h3>
    <VideoCard></VideoCard>
  </section>

  <RouterLink :to="`/vegetablePlantingChecklist`">
    <CallToActionButton button-text="I want to grow" class="mb-6"></CallToActionButton>
  </RouterLink>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import { computed, onMounted } from "vue";
import { useVegetablesStore } from "@/stores/vegetable";
import MaterialsCard from "../components/MaterialsCard.vue";
import VideoCard from "../components/VideoCard.vue";
import CallToActionButton from "../components/CallToActionButton.vue";

const vegetableStore = useVegetablesStore();

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
