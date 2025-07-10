<template>
  <v-card class="d-flex ga-4 pa-4 rounded-lg mb-4 align-center">
    <v-img 
      :src="materialImageUrl" 
      :width="100" 
      :height="100" 
      aspect-ratio="1" 
      class="material-img flex-shrink-0" 
      cover
    />
    <div class="material-info d-flex flex-column justify-center flex-grow-1">
      <v-card-title class="pa-0">{{ materialName }}</v-card-title>
      <v-card-text class="pa-0"> {{ materialDescription }}</v-card-text>
    </div>
  </v-card>
</template>

<script setup lang="ts">
const props = defineProps({
  materialImageUrl: {
    type: String,
    default: "https://placehold.co/40@3x.png",
  },
  materialName: {
    type: String,
    required: true,
  },
  materialDescription: {
    type: String,
    required: true,
  },
});
</script>

