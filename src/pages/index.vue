<template>
  <section id="user-welcome">
    <h1 class="text-primary900">Welcome, User</h1>
    <p>Let's get you up to speed!</p>
  </section>
  <v-divider color="primary900" thickness="0.75" opacity="0.5" class="mb-5 mt-5"></v-divider>
  <section id="dashboard">
    <v-row justify="space-between">
      <v-col col="6">
        <ToDoCard></ToDoCard>
      </v-col>
      <v-col col="6">
        <InfoCard></InfoCard>
      </v-col>
    </v-row>
    <br>
    <div class="d-flex flex-row flex-wrap justify-start ga-4 align-stretch mt-6">
      <h1 class="text-primary900">Here's the progress of your vegetables:</h1>
      <v-divider color="primary900" thickness="0.75" opacity="0.5" class="mb-2"></v-divider>
      <GrowingVegetableCard 
        v-if="selectedVegetable" 
        :vegetable-image-url="selectedVegetable.image_url"
        :vegetable-name="selectedVegetable.name" 
        :vegetable-id="selectedVegetable.id" 
        :estimated-harvest-time="selectedVegetable.estimated_harvest_time_formatted" 
        :watering-frequency="selectedVegetable.watering_frequency_formatted"
        :amount-of-sunlight="selectedVegetable.amount_of_sunlight" 
        :button-route="`/userVegetableImageUpload/`"
        @card-button-clicked="handleHowToGrowClick(vegetable.id)" width="360">
        <template #button-text> Get a checkup </template>
      </GrowingVegetableCard>
      <PlantNewVegetableCard></PlantNewVegetableCard>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from "vue";
import { useVegetablesStore } from "@/stores/vegetable";
import { storeToRefs } from "pinia";
import ToDoCard from "@/components/ToDoCard.vue";
import InfoCard from "@/components/InfoCard.vue";
import GrowingVegetableCard from "@/components/GrowingVegetableCard.vue";
import PlantNewVegetableCard from "@/components/PlantNewVegetableCard.vue";

const vegetableStore = useVegetablesStore();
const { selectedVegetable } = storeToRefs(vegetableStore);

onMounted(() => {
  console.log("mounted in dashboard");
  vegetableStore.getUserVegetables(1);
});
</script>
