<template>
  <v-card class="d-flex ga-4 pa-4 rounded-lg">
    <img :src="props.materialImageUrl" class="material-img">
    </img>
    <div class="material-info">
      <v-card-title class="pa-0">{{ materialName }}</v-card-title>
      <v-card-text class="pa-0"
        >{{ materialDescription }}</v-card-text
      >
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
      default: "Material Name",
    },
    materialDescription: {
      type: String,
      default: "This is the description of the material",
    },

  })
</script>
