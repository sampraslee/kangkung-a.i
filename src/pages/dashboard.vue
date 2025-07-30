<template>
  <section id="user-greeting">
    <v-container class="pa-0 mb-4 mt-4">
      <p class="mb-3">Good afternoon, Sri</p>
      <RouterLink :to="`/vegetableselect/`">
        <CallToActionButton
          button-text="Want to grow a vegetable?"
        ></CallToActionButton>
      </RouterLink>
    </v-container>
  </section>
  <hr />
  <section id="user-progress" class="mt-4">
    <v-container class="pa-0 d-flex flex-column ga-7">
      <h3>You're currently growing:</h3>
      <GrowingVegetableCard></GrowingVegetableCard>
    </v-container>
  </section>
  <section id="weather-notification" class="mt-4">
    <WeatherNoti /> <!-- Add WeatherNoti component here -->
  </section>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import CallToActionButton from "@/components/CallToActionButton.vue";
import GrowingVegetableCard from "@/components/GrowingVegetableCard.vue";
import WeatherNoti from "@/components/WeatherNoti.vue";
</script>
