<template>
  <v-card
    class="pa-6 ga-4 border-sm rounded-lg d-flex flex-row"
    border="none"
    elevation="0"
  >
    <v-img src="/public/images/checklist.png" width="180" height="180"></v-img>
    <div class="todos">
      <h3>Your todos</h3>
      <div class="today-todos">
        <v-chip
          color="primary"
          prepend-icon="mdi-calendar-clock"
          size="large"
          rounded="pill"
        >
          Today
        </v-chip>
        <v-checkbox
          label="Water kangkung"
          density="compact"
          theme="kangkungTheme"
        ></v-checkbox>
      </div>
      <div class="upcoming-todos">
        <v-chip
          color="primary"
          prepend-icon="mdi-calendar-clock"
          size="large"
          rounded="pill"
        >
          Upcoming
        </v-chip>
        <v-checkbox label="Checkup on kangkung"></v-checkbox>
      </div>
    </div>
  </v-card>
</template>

<script></script>
