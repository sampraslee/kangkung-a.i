<template>
  <v-card class="pa-4 d-flex flex-column ga-4">
    <div class="store-info d-flex flex-row ga-4">
      <img src="https://placehold.co/10@3x.png" />
      <div class="store-copy ga-4">
        <h5>Store name</h5>
        <p>Store description</p>
      </div>
    </div>
    <RouterLink :to="`#`">
      <CallToActionButton button-text="Go to store"></CallToActionButton>
    </RouterLink>
  </v-card>
</template>

<script setup lang="ts">
import CallToActionButton from "../components/CallToActionButton.vue";
</script>
