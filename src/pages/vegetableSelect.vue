<template>
  <section id="user-greeting">
    <v-container class="pa-0 mb-4 mt-4">
      <p>Hello user! What would you like to grow?</p>
    </v-container>
  </section>
  <section id="vegetable-list">
    <v-container class="pa-0 d-flex flex-column ga-7">
      <VegetableCard
        v-for="(vegetable, id) in vegetables"
        :vegetable-image-url="vegetable.image_url"
        :vegetable-name="vegetable.name"
        :vegetable-id="vegetable.id"
        :estimated-harvest-time="vegetable.estimated_harvest_time_formatted"
        :watering-frequency="vegetable.watering_frequency_formatted"
        :amount-of-sunlight="vegetable.amount_of_sunlight"
      ></VegetableCard>
    </v-container>
  </section>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import VegetableCard from "../components/VegetableCard.vue";
import { storeToRefs } from "pinia";
import { useVegetablesStore } from "@/stores/vegetable";

const vegetableStore = useVegetablesStore();
const { vegetables } = storeToRefs(vegetableStore);
const { getVegetableById } = storeToRefs(vegetableStore);

onMounted(() => {
  console.log("on mount");
  vegetableStore.getVegetables();
  console.log(vegetableStore.getVegetableById(1));
});
</script>
