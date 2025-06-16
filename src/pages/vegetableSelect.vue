<template>
  <v-container v-for="(vegetable, id) in vegetables">
    <VegetableCard
      :vegetable-image-url="vegetable.vegetableImageURL"
      :vegetable-name="vegetable.vegetableName"
      :estimated-harvest-time="vegetable.estimatedHarvestTime"
      :watering-frequency="vegetable.wateringFrequency"
      :min-sunlight="vegetable.minSunlight"
      :max-sunlight="vegetable.maxSunlight"
    ></VegetableCard>
  </v-container>
</template>

<script setup lang="ts">
import VegetableCard from "../components/VegetableCard.vue";

// test data
const vegetables = [
  {
    vegetableImageUrl: "https://placehold.co/600x400.png",
    vegetableName: "Kangkung (Water Spinach)",
    estimatedHarvestTime: 4,
    wateringFrequency: 1,
    minSunlight: 6,
    maxSunlight: 8,
  },
  {
    vegetableImageURL: "https://placehold.co/600x400@2x.png",
    vegetableName: "Bayam (Spinach)",
    estimatedHarvestTime: 5,
    wateringFrequency: 2,
    minSunlight: 5,
    maxSunlight: 7,
  },
  {
    vegetableImageURL: "https://placehold.co/600x400@2x.png",
    vegetableName: "Cili Padi (Bird's Eye Chili)",
    estimatedHarvestTime: 10,
    wateringFrequency: 1,
    minSunlight: 7,
    maxSunlight: 9,
  },
  {
    vegetableImageURL: "https://placehold.co/600x400@2x.png",
    vegetableName: "Terung (Eggplant)",
    estimatedHarvestTime: 12,
    wateringFrequency: 1,
    minSunlight: 6,
    maxSunlight: 8,
  },
];
</script>
