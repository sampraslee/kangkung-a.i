<template>
  <v-card class="d-flex ga-4 pa-4 rounded-lg mb-4 align-start" elevation="0">
    <v-avatar size="100" rounded="lg" class="bg-grey-lighten-4 material-img flex-shrink-0">
      <v-img :src="materialImageUrl" cover />
    </v-avatar>
    <div class="material-info d-flex flex-column flex-grow-1">
      <div class="d-flex align-center mb-1 ga-2">
        <v-chip
          v-if="capitalizedMaterialType"
          color="primary" 
          size="large" 
          rounded="pill">
          {{ capitalizedMaterialType }}
        </v-chip>
        <v-card-title class="font-weight-bold pa-0">{{ materialName }}</v-card-title>
      </div>
      <v-card-text class="pa-0">{{ materialDescription }}</v-card-text>
    </div>
    <div class="checkbox-container d-flex align-center justify-end flex-shrink-0 align-self-center">
      <v-checkbox-btn color="primary" class="custom-checkbox" density="comfortable"></v-checkbox-btn>
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
    default: "",
  },
  materialType: {
    type: String,
    default: "",
  },
});

const capitalizedMaterialType = computed(() => {
  if (!props.materialType) return "";
  return props.materialType.charAt(0).toUpperCase() + props.materialType.slice(1);
});
</script>

<style scoped>
.material-img {
  width: 100px;
  height: 100px;
}
.checkbox-container {
  min-width: 56px;
}
.custom-checkbox {
  font-size: 1.5rem;
}
</style>
