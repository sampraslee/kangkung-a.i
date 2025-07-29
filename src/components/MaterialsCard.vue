<template>
  <v-card class="d-flex ga-4 pa-4 rounded-lg mb-4 align-start" elevation="0">
    <v-avatar size="100" rounded="lg" class="bg-grey-lighten-4 material-img flex-shrink-0">
      <v-img :src="materialImageUrl" cover />
    </v-avatar>
    <div class="material-info d-flex flex-column">
      <div class="d-flex align-center mb-1 ga-2">
        <v-chip 
          color="primary" 
          size="large" 
          rounded="pill">
          {{ capitalizedMaterialType }}
        </v-chip>
        <v-card-title class="font-weight-bold pa-0">{{ materialName }}</v-card-title>
      </div>
      <v-card-text class="pa-0"> {{ materialDescription }}</v-card-text>
    </div>
  </v-card>
</template>

<script setup lang="ts">
import { computed } from "vue";

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
  materialType: {
    type: String,
    required: true,
  },
});

const capitalizedMaterialType = computed(() => {
  if (!props.materialType) return "";
  return props.materialType.charAt(0).toUpperCase() + props.materialType.slice(1);
});
</script>

<style scoped>
.material-img {
  /* Ensures the avatar and image are always the same size */
  width: 100px;
  height: 100px;
}
</style>
