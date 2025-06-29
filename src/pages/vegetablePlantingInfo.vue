<template>
  <v-img src="../assets/kangkung.png" cover></v-img>

  <!-- Kangkung Info -->
  <div class="vegetable-info bg-accent pa-4 rounded-lg mb-6">
    <h3 class="mb-4">Vegetable Name</h3>
    <v-chip
      prepend-icon="mdi-clock-time-four-outline"
      variant="text"
      class="mb-3"
    >
      Estimated time to harvest:
    </v-chip>
    <v-chip prepend-icon="mdi-water-outline" variant="text" class="mb-3">
      Watering frequency:
    </v-chip>
    <v-chip prepend-icon="mdi-weather-sunny" variant="text">
      Amount of sunlight:
    </v-chip>
  </div>
  <!-- How to grow -->
  <section id="planting-instructions" class="mb-6">
    <h3 class="mb-3">How to grow</h3>
    <v-list class="pa-0">
      <v-list-item class="pa-0"
        >1. Choose a container or garden bed with good drainage.</v-list-item
      >
      <v-list-item class="pa-0"
        >2. Fill with nutrient-rich, moist soil or compost.</v-list-item
      >
      <v-list-item class="pa-0"
        >3. Sow seeds or plant cuttings about 1-2 inches deep.</v-list-item
      >
      <v-list-item class="pa-0"
        >4. Keep the soil consistently moist, but not waterlogged.</v-list-item
      >
      <v-list-item class="pa-0"
        >5. Place in an area receiving full sunlight (at least 6 hours
        daily).</v-list-item
      >
      <v-list-item class="pa-0"
        >6. Sow seeds or plant cuttings about 1-2 inches deep.</v-list-item
      >
    </v-list>
  </section>
  <!-- What you'll need -->
  <section id="materials-needed" class="mb-6">
    <h3 class="mb-4">What you'll need</h3>
    <MaterialsCard></MaterialsCard>
  </section>
  <!-- Videos for you  -->
  <section id="relevant-videos" class="mb-6">
    <h3 class="mb-6">Videos for you</h3>
    <VideoCard></VideoCard>
  </section>

  <RouterLink :to="`/vegetablePlantingChecklist`">
    <CallToActionButton button-text="I want to grow"></CallToActionButton>
  </RouterLink>
</template>

<script>
import MaterialsCard from "../components/MaterialsCard.vue";
import VideoCard from "../components/VideoCard.vue";
import CallToActionButton from "../components/CallToActionButton.vue";
</script>
