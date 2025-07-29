<template>
  <v-card
    class="pa-6 ga-4 border-sm rounded-lg d-flex flex-column vegetable-card"
    border="none"
    elevation="0"
  >
    <div class="d-flex justify-center">
      <v-avatar size="180" rounded="lg" class="bg-grey-lighten-4">
        <v-img :src="vegetableImageUrl" cover></v-img>
      </v-avatar>
    </div>

    <v-container class="vegetableInfo pa-0 ga-3 d-flex flex-column flex-grow-1">
      <div class="vegetable-title-block">
        <v-card-title class="font-weight-bold pa-0 vegetable-title">
          {{ vegetableName }}
        </v-card-title>
      </div>
      <div
        class="details-list d-flex flex-column flex-grow-1 justify-space-between"
      >
        <div class="detail-row d-inline-flex align-center ga-2">
          <p class="detail-label">Harvest in:</p>
          <v-chip
            color="primary"
            prepend-icon="mdi-calendar-clock"
            size="large"
            rounded="pill"
          >
            {{ estimatedHarvestTime }}
          </v-chip>
        </div>
        <div class="detail-row d-inline-flex align-center ga-2">
          <p class="detail-label">Watering:</p>
          <v-chip
            prepend-icon="mdi-water-outline"
            color="primary"
            size="large"
            rounded="pill"
          >
            {{ wateringFrequency }}
          </v-chip>
        </div>
        <div class="detail-row d-inline-flex align-center ga-2">
          <p class="detail-label">Sunlight:</p>
          <v-chip
            prepend-icon="mdi-weather-sunny"
            color="primary"
            size="large"
            rounded="pill"
          >
            {{ amountOfSunlight }}
          </v-chip>
        </div>
      </div>
      <div class="flex-grow-1"></div>
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

<style scoped>
.vegetable-card {
  min-height: 500px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.vegetable-title-block {
  min-height: 60px; /* Adjust this value as needed for your design */
  display: flex;
  align-items: center;
}
.vegetable-title {
  white-space: normal;
  word-break: break-word;
  overflow-wrap: break-word;
  width: 100%;
}
.details-list {
  min-height: 150px; /* Ensures details block is same height in all cards */
  justify-content: space-between;
  flex-grow: 1;
}
.detail-row {
  min-height: 40px; /* Ensures each row is same height */
  align-items: center;
}
.detail-label {
  margin: 0;
  min-width: 90px; /* Ensures label width is consistent */
}
</style>
