<template>
  <v-container fluid class="pa-4 pa-lg-6">
    <v-row>
      <!-- Column 1: Vegetable Info -->
      <v-col cols="6" lg="6" class="sticky-col">
        <v-row justify="center">

          <v-card class="pa-6 ga-4 border-lg rounded-lg d-flex flex-column" border="none" elevation="0">

            <v-img :src="vegetableStore.selectedVegetable.image_url"></v-img>

            <v-container class="vegetableInfo pa-0 ga-3 d-flex flex-column">

              <v-card-title class="font-weight-bold pa-0">
                {{ vegetableStore.selectedVegetable.name }}
              </v-card-title>

              <div class="d-inline-flex align-center ga-2">
                <p>Harvest in:</p>
                <v-chip color="primary" prepend-icon="mdi-calendar-clock" size="large" rounded="pill">
                  {{ vegetableStore.selectedVegetable.estimated_harvest_time_formatted }}
                </v-chip>
              </div>

              <div class="d-inline-flex align-center ga-2">
                <p>Watering:</p>
                <v-chip prepend-icon="mdi-water-outline" color="primary" size="large" rounded="pill">
                  {{ vegetableStore.selectedVegetable.watering_frequency_formatted }}
                </v-chip>
              </div>

              <div class="d-inline-flex align-center ga-2">
                <p>Sunlight:</p>
                <v-chip prepend-icon="mdi-weather-sunny" color="primary" size="large" rounded="pill">
                  {{ vegetableStore.selectedVegetable.amount_of_sunlight }}
                </v-chip>
              </div>
            </v-container>
          </v-card>
        </v-row>
      </v-col>

      <!-- Column 2: How to grow -->
      <v-col cols="12" lg="6">
        <v-row class="align-center pa-4">
          <!-- How to grow -->
          <div class="align-center ga-2 mt-8 mb-6">
            <h3 class="mb-4">How to grow</h3>
            <ol>
              <li class="ma-4">Choose a container or garden bed with good drainage.</li>
              <li class="ma-4">Fill with nutrient-rich, moist soil or compost.</li>
              <li class="ma-4">Sow seeds or plant cuttings about 1-2 inches deep.</li>
              <li class="ma-4">Keep the soil consistently moist, but not waterlogged.</li>
              <li class="ma-4">Place in an area receiving full sunlight (at least 6 hours daily).</li>
              <li class="ma-4">Sow seeds or plant cuttings about 1-2 inches deep.</li>
            </ol>
          </div>

          <!-- What you'll need -->
          <div class="align-center ga-2 mt-8 mb-6">
            <h3 class="mb-4">What you'll need</h3>
            <MaterialsCard v-for="material in uniqueMaterials" :key="material.id"
              :materialImageUrl="material.image || 'https://placehold.co/40@3x.png'" :materialName="material.name"
              :materialDescription="material.description" class="mb-4" />
          </div>

          <!-- Videos for you  -->
          <section>
            <h3 class="mb-4">Videos for you</h3>
            <VideoCard />
          </section>
        </v-row>

        <div class="flex-column align-center ga-2 mt-8 mb-6">
          <RouterLink :to="`/vegetablePlantingChecklist`">
            <CallToActionButton button-text="I want to grow"></CallToActionButton>
          </RouterLink>
        </div>
      </v-col>
    </v-row>
  </v-container>
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

<style scoped>
.sticky-col {
  position: sticky;
  top: 32px; /* Adjust as needed for your header/nav */
  align-self: flex-start; /* Ensures it doesn't stretch full height */
  z-index: 2; /* Make sure it stays above other content if needed */
}
</style>