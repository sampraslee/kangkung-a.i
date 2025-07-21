<template>
  <section id="user-greeting">
    <h1 class="text-primary900">Select a vegetable</h1>
    <p>
      We have a selection of 17 easy to grow vegetables perfect for beginners.
      Not sure what to grow? Let us know what you’re looking for.
    </p>
    <v-text-field
      bg-color="white"
      label="Ask a question"
      icon-color="primary"
      variant="outlined"
      rounded="xl"
      prepend-inner-icon="mdi-creation"
    ></v-text-field>
  </section>
  <section id="vegetable-list">
    <v-container class="pa-0 ma-0 d-flex flex-row flex-wrap ga-5" fluid="true">
      <VegetableCard
        v-for="(vegetable, id) in vegetables"
        :vegetable-image-url="vegetable.image_url"
        :vegetable-name="vegetable.name"
        :vegetable-id="vegetable.id"
        :estimated-harvest-time="vegetable.estimated_harvest_time_formatted"
        :watering-frequency="vegetable.watering_frequency_formatted"
        :amount-of-sunlight="vegetable.amount_of_sunlight"
        :button-route="`/vegetablePlantingInfo/`"
        @card-button-clicked="handleHowToGrowClick(vegetable.id)"
        width="360"
      >
        <template #button-text> How to grow? </template>
      </VegetableCard>
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

onMounted(() => {
  console.log("on mount");
  vegetableStore.getVegetables();
});

function handleHowToGrowClick(vegetableID) {
  // Only save the vegetableId in the selectedVegetable state
  vegetableStore.getSelectedVegetable(vegetableID);
}
</script>
