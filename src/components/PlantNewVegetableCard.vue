<template>
  <v-card
    class="pa-6 border-sm bg-primary rounded-lg d-flex flex-column justify-center"
    border="none"
    elevation="0"
    width="360"
  >
    <v-img src="/public/images/new plant.png"></v-img>

    <RouterLink to="/vegetableselect" class="text-decoration-none">
      <v-card-text class="text-white text-body-1 text-center"
        ><v-icon icon="mdi-plus-circle"></v-icon> Grow a new
        vegetable</v-card-text
      >
    </RouterLink>
  </v-card>
</template>

<script setup lang="ts">
defineEmits(["card-button-clicked"]);
</script>
