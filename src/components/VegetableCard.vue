<template>
  <v-card
    class="pa-6 ga-4 border-sm rounded-lg d-flex flex-column"
    width="450px"
  >
    <v-img :src="props.vegetableImageUrl"></v-img>
    <v-container class="vegetableInfo pa-0 ga-3 d-flex flex-column">
      <v-card-title class="font-weight-bold pa-0">{{
        vegetableName
      }}</v-card-title>
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
    <RouterLink :to="`/vegetablePlantingInfo`">
      <v-btn class="bg-primary text-white">How to grow</v-btn>
    </RouterLink>
  </v-card>
</template>

<script setup lang="ts">
// define the types of data that every card needs to show
const props = defineProps({
  vegetableImageUrl: {
    type: String,
    required: false,
  },
  vegetableName: {
    type: String,
    required: true,
  },
  vegetableId: {
    type: Number,
    required: true,
  },
  estimatedHarvestTime: {
    type: Number,
    required: true,
  },
  wateringFrequency: {
    type: Number,
    required: true,
  },
  amountOfSunlight: {
    type: String,
    required: true,
  },
});
</script>
