<template>
  <v-card class="pa-6 ga-4 border-sm rounded-lg d-flex flex-column">
    <v-img :src="vegetableImageUrl"> </v-img>

    <v-container class="vegetableInfo pa-0 ga-3 d-flex flex-column">
      <v-card-title class="font-weight-bold pa-0">
        {{ vegetableName }}
      </v-card-title>
      <v-chip
        prepend-icon="mdi-clock-time-four-outline"
        size="large"
        class="rounded-lg bg-accent"
      >
        Estimated time to harvest: {{ estimatedHarvestTime }}
      </v-chip>
      <v-chip
        prepend-icon="mdi-water-outline"
        size="large"
        class="rounded-lg bg-accent"
      >
        Watering frequency: {{ wateringFrequency }}
      </v-chip>
      <v-chip
        prepend-icon="mdi-weather-sunny"
        size="large"
        class="rounded-lg bg-accent"
      >
        Amount of sunlight: {{ amountOfSunlight }}
      </v-chip>
    </v-container>

    <RouterLink :to="`/vegetablePlantingInfo/`" @click="handleHowToGrowClick">
      <CallToActionButton button-text="How to grow"></CallToActionButton>
    </RouterLink>
  </v-card>
</template>

<script setup lang="ts">
import CallToActionButton from "../components/CallToActionButton.vue";
import { useVegetablesStore } from "@/stores/vegetable";
const vegetableStore = useVegetablesStore();

const props = defineProps({
  vegetableImageUrl: String,
  vegetableName: { type: String, required: true },
  vegetableId: { type: Number, required: true },
  estimatedHarvestTime: { type: Number, required: true },
  wateringFrequency: { type: Number, required: true },
  amountOfSunlight: { type: String, required: true },
});

function handleHowToGrowClick() {
  // Only save the vegetableId in the selectedVegetable state
  vegetableStore.getSelectedVegetable(props.vegetableId);
}
</script>
