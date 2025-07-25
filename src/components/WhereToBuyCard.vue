<template>
  <v-card class="pa-4 d-flex flex-row ga-4 align-start" elevation="0">
    <v-avatar size="100" rounded="lg" class="bg-grey-lighten-4 store-img flex-shrink-0">
      <v-img :src="storeImage" cover></v-img>
    </v-avatar>
    <div class="store-info d-flex flex-column ga-2">
      <div class="store-copy">
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
  storeImage: { type: String, default: "https://placehold.co/100x100.png" },
  storeName: { type: String, default: "Store Name" },
  storeDescription: {
    type: String,
    default: "This is the description of the store.",
  },
  storeLink: {
    type: String,
    default: "https://www.groundcontrol.my/products/honest-garden-soil",
  },
});
</script>

<style scoped>
.store-img {
  width: 100px;
  height: 100px;
}
</style>
