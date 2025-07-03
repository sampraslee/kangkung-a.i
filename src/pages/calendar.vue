<template>
  <v-container
    class="d-flex flex-column justify-center align-center"
    style="height: 100vh"
  >
    <!-- Header -->
    <h1 class="mb-0 text-center font-weight-bold pa-0">When would you like to</h1>
    <h1 class="mb-8 text-center font-weight-bold pa-0 text-primary">start planting?</h1>
    
    <!-- Calendar -->
    <v-row>
      <v-col cols="12">
        <v-date-picker v-model="selectedDate" landscape :min="minDate"></v-date-picker>
      </v-col>
    </v-row>

    <!-- Confirm Button -->
    <v-btn color="primary" @click="confirmDate">Confirm Date</v-btn>

    <!-- Only appear after date confirmation -->
    <!-- Start Plant Container -->
    <v-container 
      v-if="confirmedDate" 
      class="rounded-lg mt-6" 
      style="border: 1px solid black; max-width: 400px;"
    >
      <v-row align="center">
        <v-col cols="2" class="d-flex justify-center">
          <v-icon>mdi-calendar</v-icon>
        </v-col>

        <v-col cols="10">
          <div class="text-subtitle-1">{{ formattedDate }}</div>
          <div class="text-caption">Start planting!</div>
        </v-col>
      </v-row>
    </v-container>

       <!-- Harvest Date Container -->
       <v-container 
    v-if="confirmedDate && estimatedHarvestTime" 
    class="rounded-lg mt-6" 
    style="border: 1px solid green; max-width: 400px;"
  >
    <v-row align="center">
      <v-col cols="2" class="d-flex justify-center">
        <v-icon color="green">mdi-sprout</v-icon>
      </v-col>

      <v-col cols="10">
        <div class="text-subtitle-1">{{ expectedHarvestDate }}</div>
        <div class="text-caption">Estimated {{ vegetableName }} harvest!</div>
      </v-col>
    </v-row>
  </v-container>
  </v-container>
</template>

<script>
import { useVegetablesStore } from "@/stores/vegetable";
const vegetableStore = useVegetablesStore(); //compulsory to call specific store

export default { //export to pinia.store
  data() {
    //get current date from date picker, this is used to grey out before date.
    const today = new Date(); //represents the current date that's by default the present
    const currentYear = today.getFullYear(); //extracts the year/month/day from constant "today"
    const currentMonth = today.getMonth() + 1; //+1 because months are 0-indexed
    const currentDay = today.getDate();

    //this line of code is used to grey out the date before present
    const formattedMonth = String(currentMonth).padStart(2, "0"); //converts the month/day number to string
    const formattedDay = String(currentDay).padStart(2, "0");

    return {
      selectedDate: null, //initially no date is selected //"selectedDate is the date value of user's picked date"
      confirmedDate: null, //initially no date is confirmed
      minDate: `${currentYear}-${formattedMonth}-${formattedDay}`, //grey out the date before present
    };
  },
  computed: {
    // Access the vegetable store and extract selectedVegetable
    selectedVegetable() {
      const vegetableStore = useVegetablesStore();
      return vegetableStore.selectedVegetable;
    },
    vegetableName() { //define constant
      return this.selectedVegetable?.name || "";
    },
    estimatedHarvestTime() { //define constant
      return this.selectedVegetable?.estimated_harvest_time || "";
    },

    formattedDate() {
      // confirmedDate is the date from the user
      if (!this.confirmedDate) return '';
      // Format as DD/MM/YYYY with leading zeros
      // Converts the day number to a string
      const day = String(this.confirmedDate.day).padStart(2, '0'); //padStart ensures day is always at 2 digits i.e (02/MM  or DD/08)
      const month = String(this.confirmedDate.month).padStart(2, '0');
      return `${day}/${month}/${this.confirmedDate.year}`; //returned as string //!!convert date picked by user to a humanized date!!
    },
    
    expectedHarvestDate() {
      if (!this.confirmedDate || !this.estimatedHarvestTime) return '';

      const daysToAdd = parseInt(this.estimatedHarvestTime.replace(/\D/g, '')) || 0; //converts religion

      const plantingDate = new Date(
        this.confirmedDate.year,
        this.confirmedDate.month - 1,
        this.confirmedDate.day
      );

      plantingDate.setDate(plantingDate.getDate() + daysToAdd);

      const harvestDay = String(plantingDate.getDate()).padStart(2, '0');
      const harvestMonth = String(plantingDate.getMonth() + 1).padStart(2, '0'); //+1 because months are 0-indexed
      const harvestYear = plantingDate.getFullYear();
  
  return `${harvestDay}/${harvestMonth}/${harvestYear}`;
}
    
  },
  methods: {  // is triggered when button confirm date is clicked
    confirmDate() {
      if (this.selectedDate) {
        const date = new Date(this.selectedDate); //converts selected date into a JavaScript Date object
        this.confirmedDate = {
          day: date.getDate(),
          month: date.getMonth() + 1,
          year: date.getFullYear(),
        };
      } else {
        // user hasn't selected a date
        alert("Please select a date first.");
      }
    },
  },
};
</script>