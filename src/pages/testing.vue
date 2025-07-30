<template>
  <v-img :src="vegetable_img"></v-img>

  <VegetableCard
    vegetable-image-url="/public/images/vegetables/Bayam.png"
    vegetable-name="isaac"
    estimated-harvest-time="cheetat"
    watering-frequency="42"
    amount-of-sunlight="perlis"
  ></VegetableCard>
</template>

<script>
import VegetableCard from "../components/VegetableCard.vue";
let vegetable_img = "@assets/images/vegetables/Bayam.png";
</script>
