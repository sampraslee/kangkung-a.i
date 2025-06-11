<template>
  <!-- Header -->

  <v-container class="d-flex flex-column justify-center align-center">
    <h1 class="mb-0 text-center font-weight-bold">Here's your</h1>
    <h1 class="mb-8 text-center font-weight-bold">schedule</h1>

    <v-row>
      <v-col cols="12">
        <v-date-picker v-model="selectedDate" landscape :min="minDate" disabled>
        </v-date-picker>
      </v-col>
    </v-row>
  </v-container>
  <!-- Important Dates -->
  <v-row pa="12">
    <v-col pa="12">
      <h2 class="text-h5 font-weight-bold primary--text ml-15 mb-4">
        Important Dates
      </h2>
    </v-col>
  </v-row>
  <!-- First component -->
  <v-container class="rounded-lg" style="border: 1px solid black">
    <v-row align="center">
      <v-col cols="2" class="d-flex justify-center">
        <v-icon>mdi-calendar</v-icon>
      </v-col>

      <v-col cols="10">
        <div class="text-subtitle-1">18/05/2025</div>
        <div class="text-caption">Change your soil</div>
      </v-col>
    </v-row>
  </v-container>
  <!-- Second component -->
  <v-container class="rounded-lg" style="border: 1px solid black">
    <v-row align="center">
      <v-col cols="2" class="d-flex justify-center">
        <v-icon>mdi-calendar</v-icon>
      </v-col>

      <v-col cols="10">
        <div class="text-subtitle-1">27/05/2025</div>
        <div class="text-caption">Enjoy your harvest!</div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    const today = new Date();
    const currentYear = today.getFullYear();
    const currentMonth = today.getMonth() + 1;
    const currentDay = today.getDate();

    const formattedMonth = String(currentMonth).padStart(2, "0");
    const formattedDay = String(currentDay).padStart(2, "0");

    return {
      selectedDate: null,

      minDate: `${currentYear}-${formattedMonth}-${formattedDay}`,
    };
  },
};
</script>
