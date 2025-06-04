<template>
  <v-card class="pa-4 product-vege-card">
    <div class="mb-3">
      <v-img
        v-if="ImageUrl"
        class="rounded-lg plant-image"
        :src="ImageUrl"
        :alt="ProductName"
        cover
      ></v-img>
      <v-icon
        v-else
        size="48"
        color="green-darken-2"
        class="plant-image-placeholder-icon"
        >mdi-leaf-circle-outline</v-icon
      >
    </div>

    <div class="text-h5 font-weight-bold mb-2">{{ ProductName }}</div>

    <div class="text-body-2 mb-1">
      <span class="font-weight-medium">Estimated time to harvest:</span>
      {{ HarvestTime }}
      <span
        v-if="
          HarvestTime &&
          !HarvestTime.includes('days') &&
          !HarvestTime.includes('weeks')
        "
        >weeks</span
      >
    </div>
    <div class="text-body-2 mb-1">
      <span class="font-weight-medium">Water needs:</span> {{ WaterNeeds }}
    </div>
    <div class="text-body-2">
      <span class="font-weight-medium">Sunlight needs:</span> {{ SunNeeds }}
    </div>

    <v-btn color="primary" block class="mt-4">How to grow?</v-btn>
  </v-card>
</template>

<script setup lang="ts">
// No need to import defineProps explicitly if using <script setup> with Vue 3.
// It's globally available.

defineProps({
  ProductName: {
    type: String,
    default: "Vege name",
  },
  HarvestTime: {
    // FIX: Allow String OR null
    type: [String, null],
    default: null, // It's better to default to null if the prop can be null
  },
  WaterNeeds: {
    // FIX: Allow String OR null
    type: [String, null],
    default: null,
  },
  SunNeeds: {
    // FIX: Allow String OR null
    type: [String, null],
    default: null,
  },
  ImageUrl: {
    // FIX: Allow String OR null
    type: [String, null],
    default: null, // It's better to default to null if the prop can be null
  },
});
</script>

<style scoped>
.product-vege-card {
  max-width: 300px;
  margin: auto;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* Base style for the image/icon area */
.plant-image,
.plant-image-placeholder-icon {
  width: 100%;
  height: 150px; /* Consistent height for all cards */
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 4px;
  overflow: hidden;
}

/* Specific background for the icon placeholder */
.plant-image-placeholder-icon {
  background-color: #e0f2f1; /* Light green background for icon */
}
</style>
