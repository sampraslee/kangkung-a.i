<template>
  <section id="user-welcome">
    <h1 class="text-primary900">Good afternoon, User</h1>
    <p>Welcome back, let's get you up to speed with your growing vegetables</p>
  </section>
  <v-divider
    color="primary900"
    thickness="0.75"
    opacity="1"
    class="mb-5 mt-5"
  ></v-divider>
  <section id="dashboard">
    <v-row>
      <v-col col="6">
        <ToDoCard></ToDoCard>
      </v-col>
      <v-col col="6">
        <InfoCard fill-height="100"></InfoCard>
      </v-col>
    </v-row>
    <v-row>
      <v-col col="3">
        <GrowingVegetableCard
          v-if="selectedVegetable"
          :vegetable-image-url="selectedVegetable.image_url"
          :vegetable-name="selectedVegetable.name"
          :vegetable-id="selectedVegetable.id"
          :estimated-harvest-time="
            selectedVegetable.estimated_harvest_time_formatted
          "
          :watering-frequency="selectedVegetable.watering_frequency_formatted"
          :amount-of-sunlight="selectedVegetable.amount_of_sunlight"
          :button-route="`/userVegetableImageUpload/`"
          @card-button-clicked="handleHowToGrowClick(vegetable.id)"
          width="360"
        >
          <template #button-text> Get a checkup </template>
        </GrowingVegetableCard>
      </v-col>
      <v-col col="3">
        <PlantNewVegetableCard
          :button-route="`/userVegetableImageUpload`"
          width="320"
        ></PlantNewVegetableCard>
      </v-col>
    </v-row>
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
