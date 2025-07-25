<template>
  <v-card
    class="pa-6 ga-4 border-sm bg-primary rounded-lg d-flex flex-column"
    border="none"
    elevation="0"
  >
    <v-img src="/public/images/new plant.png"></v-img>

    <RouterLink to="/vegetableSelect/">
      <v-card-text class="text-white"
        ><v-icon icon="mdi-plus-circle"></v-icon> Grow a new
        vegetable</v-card-text
      >
    </RouterLink>
  </v-card>
</template>

<script setup lang="ts">
defineEmits(["card-button-clicked"]);
</script>
