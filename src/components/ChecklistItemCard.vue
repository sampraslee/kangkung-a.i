<template>
  <v-card class="d-flex ga-4 pa-4 rounded-lg mb-4" elevation="0">
    <v-avatar size="100" rounded="lg" class="bg-grey-lighten-4 material-img flex-shrink-0">
      <v-img :src="materialImageUrl" cover />
    </v-avatar>
    <div class="material-info d-flex align-start flex-column flex-grow-1">
      <v-card-title class="font-weight-bold pa-0">{{ materialName }}</v-card-title>
      <v-card-text class="pa-0">{{ materialDescription }}</v-card-text>
    </div>
    <div class="checkbox-container d-flex align-center justify-end flex-shrink-0">
      <v-checkbox-btn color="primary" class="custom-checkbox" density="comfortable"></v-checkbox-btn>
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
