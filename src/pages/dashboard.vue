<template>
  <section id="user-greeting">
    <v-container class="pa-0 mb-4 mt-4">
      <p class="mb-3">Good afternoon, Sri</p>
      <RouterLink :to="`/vegetablePlantingInfo/`">
        <CallToActionButton
          button-text="Want to grow a vegetable?"
        ></CallToActionButton>
      </RouterLink>
    </v-container>
  </section>
  <hr />
  <section id="user-progress" class="mt-4">
    <v-container class="pa-0 d-flex flex-column ga-7">
      <GrowingVegetableCard></GrowingVegetableCard>
    </v-container>
  </section>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import CallToActionButton from "@/components/CallToActionButton.vue";
import GrowingVegetableCard from "@/components/GrowingVegetableCard.vue";
</script>
