<template>
    <v-container class="d-flex flex-column justify-center align-center" style="height: 100vh">
      <!-- Header -->
      <h1 class="mb-0 text-center font-weight-bold pa-0">When would you like to</h1>
      <h1 class="mb-8 text-center font-weight-bold pa-0 text-primary">start planting?</h1>
  
      <!-- Date Picker -->
      <v-row>
        <v-col cols="12">
          <v-date-picker v-model="selectedDate" landscape :min="minDate"></v-date-picker>
        </v-col>
      </v-row>
  
      <v-btn color="primary" @click="confirmDate">Confirm Date</v-btn>
  
      <!-- Planting Date Container -->
      <v-container 
        v-if="confirmedDate && selectedVegetable" 
        class="rounded-lg mt-6" 
        style="border: 1px solid black; max-width: 400px;"
      >
        <v-row align="center">
          <v-col cols="2" class="d-flex justify-center">
            <v-icon>mdi-calendar</v-icon>
          </v-col>
          <v-col cols="10">
            <div class="text-subtitle-1">{{ formattedDate }}</div>
            <div class="text-caption">Start planting {{ selectedVegetable.name }}!</div>
          </v-col>
        </v-row>
      </v-container>
  
      <!-- Harvest Date Container -->
      <v-container 
        v-if="confirmedDate && selectedVegetable" 
        class="rounded-lg mt-4" 
        style="border: 1px solid black; max-width: 400px;"
      >
        <v-row align="center">
          <v-col cols="2" class="d-flex justify-center">
            <v-icon>mdi-sprout</v-icon>
          </v-col>
          <v-col cols="10">
            <div class="text-subtitle-1">{{ formattedHarvestDate }}</div>
            <div class="text-caption">Estimated {{ selectedVegetable.name }} harvest!</div>
          </v-col>
        </v-row>
      </v-container>
    </v-container>
  </template>
  
  <script setup>
  import { computed, ref } from 'vue';
  import { useVegetablesStore } from '@/stores/vegetable';
  
  // Initialize Pinia store
  const vegetablesStore = useVegetablesStore();
  const selectedVegetable = vegetablesStore.selectedVegetable;
  
  // Date handling
  const today = new Date();
  const minDate = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;
  const selectedDate = ref(null);
  const confirmedDate = ref(null);
  
  // Format planting date (DD/MM/YYYY)
  const formattedDate = computed(() => {
    if (!confirmedDate.value) return '';
    const day = String(confirmedDate.value.day).padStart(2, '0');
    const month = String(confirmedDate.value.month).padStart(2, '0');
    return `${day}/${month}/${confirmedDate.value.year}`;
  });
  
  // Calculate harvest date from store's harvest_time
  const formattedHarvestDate = computed(() => {
    if (!confirmedDate.value || !selectedVegetable?.harvest_time) return '';
    
    // Parse harvest time (supports "6 weeks", "P6W", or similar)
    const harvestTimeStr = selectedVegetable.harvest_time;
    const daysToHarvest = parseInt(harvestTimeStr.match(/\d+/)[0]) * 7; // Convert weeks to days
    
    // Calculate harvest date
    const harvestDate = new Date(
      confirmedDate.value.year,
      confirmedDate.value.month - 1,
      confirmedDate.value.day
    );
    harvestDate.setDate(harvestDate.getDate() + daysToHarvest);
    
    // Format as DD/MM/YYYY
    return `${String(harvestDate.getDate()).padStart(2, '0')}/${String(harvestDate.getMonth() + 1).padStart(2, '0')}/${harvestDate.getFullYear()}`;
  });
  
  // Confirm date selection
  const confirmDate = () => {
    if (selectedDate.value) {
      const date = new Date(selectedDate.value);
      confirmedDate.value = {
        day: date.getDate(),
        month: date.getMonth() + 1,
        year: date.getFullYear(),
      };
    } else {
      alert("Please select a date first.");
    }
  };
  </script>
  
  <style scoped>
  .text-primary {
    color: var(--v-primary-base);
  }
  </style>