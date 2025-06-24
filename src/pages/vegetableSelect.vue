<template>
  <div>
    <VegetableCard
      v-for="(vegetable, id) in vegetables"
      :vegetable-image-url="vegetable.image_url"
      :vegetable-name="vegetable.name"
      :vegetable-id="vegetable.id"
      :estimated-harvest-time="vegetable.estimated_harvest_time"
      :watering-frequency="vegetable.watering_frequency"
      :amount-of-sunlight="vegetable.amount_of_sunlight"
    ></VegetableCard>
  </div>
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
