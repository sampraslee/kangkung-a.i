<template>
  <v-card
    class="pa-6 ga-4 border-sm rounded-lg d-flex flex-column align-center"
    border="none"
    elevation="0"
  >
    <v-img :src="vegetableImageUrl" width="200"> </v-img>

    <v-container class="vegetableInfo pa-0 ga-3 d-flex flex-column">
      <v-card-title class="font-weight-bold pa-0">
        {{ vegetableName }}
      </v-card-title>
      <div class="d-inline-flex align-center ga-2">
        <p>Ready to harvest in:</p>
        <v-chip
          color="primary"
          prepend-icon="mdi-calendar-clock"
          size="large"
          rounded="pill"
        >
          {{ estimatedHarvestDate }}
        </v-chip>
      </div>
      <div class="d-inline-flex align-center ga-2">
        <p>Last Watered:</p>
        <v-chip
          prepend-icon="mdi-water-outline"
          color="primary"
          size="large"
          rounded="pill"
        >
          {{ lastWatered }}
        </v-chip>
      </div>
      <div class="d-inline-flex align-center ga-2">
        <p>Last Checkup:</p>
        <v-chip
          prepend-icon="mdi-weather-sunny"
          color="primary"
          size="large"
          rounded="pill"
        >
          {{ lastCheckup }}
        </v-chip>
      </div>
    </v-container>

    <CallToActionButton :to="buttonRoute">
      <slot name="button-text"></slot>
    </CallToActionButton>
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
  buttonRoute: { type: String, required: true },
});
</script>
