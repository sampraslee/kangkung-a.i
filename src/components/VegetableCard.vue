<template>
  <v-card
    class="pa-6 ga-4 border-sm rounded-lg d-flex flex-column"
    border="none"
    elevation="0"
  >
    <v-img :src="vegetableImageUrl"></v-img>

    <v-container class="vegetableInfo pa-0 ga-3 d-flex flex-column">
      <v-card-title class="font-weight-bold pa-0">
        {{ vegetableName }}
      </v-card-title>
      <div class="d-inline-flex align-center ga-2">
        <p>Harvest in:</p>
        <v-chip
          color="primary"
          prepend-icon="mdi-calendar-clock"
          size="large"
          rounded="pill"
        >
          {{ estimatedHarvestTime }}
        </v-chip>
      </div>
      <div class="d-inline-flex align-center ga-2">
        <p>Watering:</p>
        <v-chip
          prepend-icon="mdi-water-outline"
          color="primary"
          size="large"
          rounded="pill"
        >
          {{ wateringFrequency }}
        </v-chip>
      </div>
      <div class="d-inline-flex align-center ga-2">
        <p>Sunlight:</p>
        <v-chip
          prepend-icon="mdi-weather-sunny"
          color="primary"
          size="large"
          rounded="pill"
        >
          {{ amountOfSunlight }}
        </v-chip>
      </div>
    </v-container>

    <CallToActionButton
      :to="buttonRoute"
      @button-clicked="$emit('card-button-clicked')"
    >
      <slot name="button-text"></slot>
    </CallToActionButton>
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
  buttonRoute: { type: String, required: true },
});

function handleHowToGrowClick() {
  // Only save the vegetableId in the selectedVegetable state
  vegetableStore.getSelectedVegetable(props.vegetableId);
}

defineEmits(["card-button-clicked"]);
</script>
