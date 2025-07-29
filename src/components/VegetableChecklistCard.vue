<template>
    <v-card class="pa-6 ga-4 border-sm rounded-lg d-flex flex-column" border="none" elevation="0">
        <v-img :src="vegetableImageUrl" height="200px" cover></v-img>

        <v-container class="vegetableInfo pa-0 ga-3 d-flex flex-column">
            <v-card-title class="font-weight-bold text-h5 text-wrap pa-0 vegetable-title text-left">
                {{ capitalizedVegetableName }}
            </v-card-title>
            <div class="d-inline-flex align-center ga-2">
                <p>Harvest in:</p>
                <v-chip color="primary" prepend-icon="mdi-calendar-clock" size="large" rounded="pill">
                    {{ estimatedHarvestTime }}
                </v-chip>
            </div>
            <div class="d-inline-flex align-center ga-2">
                <p>Watering:</p>
                <v-chip prepend-icon="mdi-water-outline" color="primary" size="large" rounded="pill">
                    {{ wateringFrequency }}
                </v-chip>
            </div>
            <div class="d-inline-flex align-center ga-2">
                <p>Sunlight:</p>
                <v-chip prepend-icon="mdi-weather-sunny" color="primary" size="large" rounded="pill">
                    {{ amountOfSunlight }}
                </v-chip>
            </div>
        </v-container>
    </v-card>
</template>

<script setup lang="ts">
import { computed } from "vue";

const props = defineProps({
    vegetableImageUrl: String,
    vegetableName: { type: String, required: true },
    estimatedHarvestTime: { type: String, required: true },
    wateringFrequency: { type: String, required: true },
    amountOfSunlight: { type: String, required: true },
});

const capitalizedVegetableName = computed(() => {
    if (!props.vegetableName) return "";
    return props.vegetableName.charAt(0).toUpperCase() + props.vegetableName.slice(1);
});
</script>
