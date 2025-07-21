<template>
  <v-card class="pa-4 d-flex flex-row ga-4" elevation="0">
    <img :src="storeImage" />
    <div class="store-info d-flex flex-column justify-space-between">
      <div class="store-copy ga-4">
        <v-card-title class="font-weight-bold pa-0">{{
          storeName
        }}</v-card-title>
        <v-card-text class="pa-0"> {{ storeDescription }}</v-card-text>
      </div>
      <a :href="storeLink" class="text-primary">Go to store</a>
    </div>
  </v-card>
</template>

<script setup lang="ts">
const props = defineProps({
  storeImage: { type: String, default: "https://placehold.co/40@3x.png" },
  storeName: { type: String, default: "Store Name" },
  storeDescription: {
    type: String,
    default: "This is the description of the store.",
  },
  storeLink: {
    String,
    default: "https://www.groundcontrol.my/products/honest-garden-soil",
  },
});
</script>
