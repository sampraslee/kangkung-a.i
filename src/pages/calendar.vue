<template>
  <v-container
    class="d-flex flex-column justify-center align-center"
    style="height: 100vh"
  >
    <!-- Header -->
    <h1 class="mb-0 text-center font-weight-bold pa-0">
      When would you like to
    </h1>
    <h1 class="mb-8 text-center font-weight-bold pa-0 text-primary">
      start planting?
    </h1>

    <!-- Date Picker -->
    <v-row>
      <v-col cols="12">
        <v-date-picker
          v-model="selectedDate"
          header-color="primary"
          bg-color="accent"
          color="secondary"
          border="sm"
          landscape
          :min="minDate"
        ></v-date-picker>
      </v-col>
    </v-row>

    <v-btn color="primary" @click="confirmDate">Confirm Date</v-btn>

    <!-- Planting Date Container -->
    <v-container
      v-if="confirmedDate"
      class="rounded-lg mt-6"
      style="border: 1px solid black; max-width: 400px"
    >
      <v-row align="center">
        <v-col cols="2" class="d-flex justify-center">
          <v-icon>mdi-calendar</v-icon>
        </v-col>
        <v-col cols="10">
          <div class="text-subtitle-1">{{ formattedDate }}</div>
          <div class="text-caption">Start planting {{ vegetableName }}!</div>
        </v-col>
      </v-row>
    </v-container>

    <!-- NEW: Harvest Date Container -->
    <v-container
      v-if="confirmedDate"
      class="rounded-lg mt-4"
      style="border: 1px solid black; max-width: 400px"
    >
      <v-row align="center">
        <v-col cols="2" class="d-flex justify-center">
          <v-icon>mdi-sprout</v-icon>
        </v-col>
        <v-col cols="10">
          <div class="text-subtitle-1">{{ formattedHarvestDate }}</div>
          <div class="text-caption">Estimated {{ vegetableName }} harvest!</div>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import { storeToRefs } from "pinia";
import { useVegetablesStore } from "@/stores/vegetable";

const vegetableStore = useVegetablesStore();
const { vegetableName, estimatedHarvestTime } = storeToRefs(vegetableStore);

export default {
  data() {
    const today = new Date();
    const currentYear = today.getFullYear();
    const currentMonth = today.getMonth() + 1;
    const currentDay = today.getDate();

    return {
      selectedDate: null,
      minDate: `${currentYear}-${String(currentMonth).padStart(
        2,
        "0"
      )}-${String(currentDay).padStart(2, "0")}`,
      confirmedDate: null,
      // Use the prop or fallback to placeholder
      currentVegetable: this.selectedVegetable,
    };
  },
  computed: {
    // this is where I get the date the user clicked
    formattedDate() {
      if (!this.confirmedDate) return "";
      const day = String(this.confirmedDate.day).padStart(2, "0");
      const month = String(this.confirmedDate.month).padStart(2, "0");
      const userSelectedDate = Date(
        `${day}/${month}/${this.confirmedDate.year}`
      );
      console.log(typeof `${day}/${month}/${this.confirmedDate.year}`);
      return `${day}/${month}/${this.confirmedDate.year}`;
    },

    formattedHarvestDate() {
      if (!this.confirmedDate) return "";

      const harvestDate = new Date(
        this.confirmedDate.year,
        this.confirmedDate.month - 1,
        this.confirmedDate.day
      );
      harvestDate.setDate(harvestDate.getDate() + estimatedHarvestTime * 7);

      // Format as DD/MM/YYYY
      return `${String(harvestDate.getDate()).padStart(2, "0")}/${String(
        harvestDate.getMonth() + 1
      ).padStart(2, "0")}/${harvestDate.getFullYear()}`;
    },
  },
  methods: {
    confirmDate() {
      if (this.selectedDate) {
        const date = new Date(this.selectedDate);
        this.confirmedDate = {
          day: date.getDate(),
          month: date.getMonth() + 1,
          year: date.getFullYear(),
        };
      } else {
        alert("Please select a date first.");
      }
    },
  },
};
</script>
