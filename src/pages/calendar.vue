<template>
  <v-container class="pa-0">
    <h1 class="text-center mb-5">
      When would you like to
      <span class="text-primary">start planting</span>
    </h1>
    <v-date-picker
      header-color="primary"
      bg-color="accent"
      color="secondary"
      border="sm"
      rounded="lg"
      width="100%"
      v-model="selectedDate"
      :min="currentDate"
    ></v-date-picker>
    <CallToActionButton
      button-text="Select Date"
      class="mt-3"
      @click="logSelectedDate"
    ></CallToActionButton>
  </v-container>

  <v-container class="pa-0 mt-5" v-if="!selectedDate">
    <p>
      Select a date and we will show you a timeline of your future planting
      journey.
    </p>
  </v-container>

  <v-container class="pa-0 mt-5" v-else>
    <h2>Important Dates</h2>
    <v-timeline
      align="start"
      direction="vertical"
      dot-color="primary"
      side="end"
      truncate-line="both"
    >
      <v-timeline-item v-if="selectedDate">
        <v-sheet border="sm" color="accent" rounded="lg" class="pa-2">
          <p class="font-weight-bold">
            {{ selectedDate.toDateString() }}
          </p>
          <p>Start planting</p>
        </v-sheet>
      </v-timeline-item>
      <v-timeline-item v-if="calculateEstimatedHarvestDate">
        <v-sheet border="sm" color="accent" rounded="lg" class="pa-2">
          <p class="font-weight-bold">
            {{ calculateEstimatedHarvestDate.toDateString() }}
          </p>
          <p>Ready to harvest!</p>
        </v-sheet>
      </v-timeline-item>
    </v-timeline>
  </v-container>
</template>

<script setup lang="ts">
import CallToActionButton from "../components/CallToActionButton.vue";
import { useVegetablesStore } from "@/stores/vegetable";
import { ref, computed } from "vue";

const vegetableStore = useVegetablesStore();
const selectedVegetable = vegetableStore.selectedVegetable;
const currentDate = new Date();
currentDate.setDate(currentDate.getDate() - 1); //grey-out
const selectedDate = ref(null);

const calculateEstimatedHarvestDate = computed(() => {
  const estimatedHarvestDate = new Date(selectedDate.value);
  estimatedHarvestDate.setSeconds(
    selectedDate.value.getSeconds() +
      selectedVegetable.estimated_harvest_time_in_seconds
  );
  return estimatedHarvestDate;
});

function logSelectedDate() {
  console.log(selectedDate.value.toDateString());
  console.log(calculateEstimatedHarvestDate.value);
  console.log(selectedVegetable.estimated_harvest_time);
}
</script>
