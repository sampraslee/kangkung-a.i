<template>
  <v-card
    class="pa-6 ga-4 border-sm rounded-lg d-flex flex-row fill-height"
    border="none"
    elevation="0"
  >
    <v-img src="/images/checklist.png" width="180" height="180"></v-img>
    <div class="todos">
      <h3 class="text-primary900">Your todos</h3>
      <div class="today-todos">
        <v-chip
          color="primary"
          prepend-icon="mdi-calendar-clock"
          size="large"
          rounded="pill"
        >
          Today
        </v-chip>
        <div v-if="todaysTasks.length > 0">
          <v-checkbox
            v-for="(task, index) in todaysTasks"
            :key="index"
            density="compact"
            :label="isFirstDay(task.date) ? 'Start planting' : task.event"
          ></v-checkbox>
        </div>
        <v-checkbox density="compact" label="Plant kangkung seeds"></v-checkbox>
        <!-- <p v-else class="text-disabled ml-4 mt-2">None for today ✨</p> -->
      </div>

      <div class="upcoming-todos mt-4">
        <v-chip
          color="primary"
          prepend-icon="mdi-calendar-clock"
          size="large"
          rounded="pill"
        >
          Upcoming
        </v-chip>
        <v-checkbox
          v-if="upcomingTask"
          density="compact"
          :label="
            isFirstDay(upcomingTask.date)
              ? `[${formatDate(upcomingTask.date)}] Start planting`
              : `[${formatDate(upcomingTask.date)}] ${upcomingTask.event}`
          "
        ></v-checkbox>
        <p v-else class="text-disabled ml-4 mt-2">All done for now! 👍</p>
      </div>
    </div>
  </v-card>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { useProgressStore } from "@/stores/progress";

const progressStore = useProgressStore();

const todaysTasks = computed(() => {
  const today = new Date().toDateString();

  return progressStore.timeline.filter((task) => {
    const taskDate = new Date(task.date).toDateString();
    return taskDate === today;
  });
});

const upcomingTask = computed(() => {
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const futureTasks = progressStore.timeline.filter(
    (task) => new Date(task.date) > today
  );

  return futureTasks.length > 0 ? futureTasks[0] : null;
});

const formatDate = (dateString: string) => {
  const options: Intl.DateTimeFormatOptions = {
    day: "numeric",
    month: "short",
  };
  return new Date(dateString).toLocaleDateString("en-GB", options);
};

const isFirstDay = (taskDate: string) => {
  if (progressStore.timeline.length === 0) {
    return false;
  }
  // Compare the task's date with the date of the very first item in the timeline
  const firstEventDate = new Date(
    progressStore.timeline[0].date
  ).toDateString();
  const currentTaskDate = new Date(taskDate).toDateString();

  return firstEventDate === currentTaskDate;
};
</script>
