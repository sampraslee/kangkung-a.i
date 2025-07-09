<template>
  <v-card class="pa-6 ga-4 border-sm rounded-lg d-flex flex-column">
    <v-img :src="vegetableImageUrl"> </v-img>

    <v-container class="vegetableInfo pa-0 ga-3 d-flex flex-column">
      <v-card-title class="font-weight-bold pa-0">
        {{ vegetableName }}
      </v-card-title>
      <v-chip
        prepend-icon="mdi-clock-time-four-outline"
        size="large"
        class="rounded-lg bg-accent"
      >
        Estimated harvest date: {{ estimatedHarvestDate }}
      </v-chip>
      <v-chip
        prepend-icon="mdi-water-outline"
        size="large"
        class="rounded-lg bg-accent"
      >
        Last watered: {{ lastWatered }}
      </v-chip>
      <v-chip
        prepend-icon="mdi-weather-sunny"
        size="large"
        class="rounded-lg bg-accent"
      >
        Last checkup: {{ lastCheckup }}
      </v-chip>
    </v-container>

    <RouterLink :to="`/userVegetableImageUpload/`">
      <CallToActionButton button-text="Get a checkup"></CallToActionButton>
    </RouterLink>
  </v-card>
</template>

<script setup lang="ts">
import CallToActionButton from "@/components/CallToActionButton.vue";
import { useProgressStore } from "@/stores/progress";

const progressStore = useProgressStore();

const props = defineProps({
  vegetableImageUrl: String,
  vegetableName: { type: String, required: true, default: "Kangkung" },
  vegetableId: { type: Number },
  estimatedHarvestDate: { type: String, default: "31st July 2025" },
  lastWatered: { type: String, default: "Yesterday" },
  lastCheckup: { type: String, default: "1st July 2025" },
});
</script>
