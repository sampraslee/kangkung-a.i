<template>
  <v-card class="pa-6 ga-4 border-sm rounded-lg d-flex flex-row align-start h-100" border="none" elevation="0">
      <v-img src="/public/images/checklist.png" width="150" height="150" max-width="150" max-height="150" position="left" class="flex-shrink-0"></v-img>
      <div class="todos flex-grow-1">
        <h2 class="text-primary900 text-left">Your to-dos</h2>
        <v-divider color="primary900" thickness="0.75" opacity="0.5" class="mb-2 mt-1"></v-divider>
        <div class="today-todos d-flex flex-column align-start">
          <v-chip color="primary" prepend-icon="mdi-calendar-clock" size="large" rounded="pill" class="mb-1">
            Today
          </v-chip>
          <v-checkbox label="Water kangkung" density="compact" theme="kangkungTheme" hide-details></v-checkbox>
        </div>
        <br>
        <div class="upcoming-todos d-flex flex-column align-start">
          <v-chip color="primary" prepend-icon="mdi-calendar-clock" size="large" rounded="pill" class="mb-1">
            Upcoming
          </v-chip>
          <v-checkbox label="Checkup on kangkung" density="compact" theme="kangkungTheme" hide-details></v-checkbox>
        </div>
      </div>
  </v-card>
</template>

<script></script>
