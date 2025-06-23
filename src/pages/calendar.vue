<template>
  <!-- Header -->

  <v-container
    class="d-flex flex-column justify-center align-center"
    style="height: 100vh"
  >
    <h1 class="mb-0 text-center font-weight-bold pa-0">
      When would you like to
    </h1>
    <h1 class="mb-8 text-center font-weight-bold pa-0 text-primary">
      start planting?
    </h1>

    <v-row>
      <v-col cols="12">
        <v-date-picker v-model="selectedDate" landscape :min="minDate">
          <!-- <template v-slot:header>
          <div class="d-flex justify-space-between align-center pa-2">
            <v-btn icon @click="prevMonth">
              <v-icon>mdi-chevron-left</v-icon>
            </v-btn>
            <div class="text-h6">{{ currentMonthYear }}</div>
            <v-btn icon @click="nextMonth">
              <v-icon>mdi-chevron-right</v-icon>
            </v-btn>
          </div>
          </template> -->
        </v-date-picker>
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
    // },
    // computed: {
    //   currentMonthYear() {
    //     const date = new Date(this.date);
    //     const options = { month: "long", year: "numeric" };
    //     return date.toLocaleDateString(undefined, options);
    //   },
    // },
    // methods: {
    //   updateDisplayDate() {
    //     const [year, month, day] = this.date.split("-");
    //     this.formattedDate = `${day}/${month}/${year}`;
    //   },
    //   prevMonth() {
    //     const date = new Date(this.date);
    //     date.setMonth(date.getMonth() - 1);
    //     this.date = date.toISOString().substr(0, 10);
    //   },
    //   nextMonth() {
    //     const date = new Date(this.date);
    //     date.setMonth(date.getMonth() + 1);
    //     this.date = date.toISOString().substr(0, 10);
    //   },
  },
};
</script>
