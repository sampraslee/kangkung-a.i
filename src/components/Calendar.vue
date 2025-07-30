<template>
  <v-container class="pa-0">
    <v-date-picker
      header-color="primary"
      bg-color="accent"
      color="secondary"
      border="sm"
      rounded="lg"
      width="100%"
      v-model="selectedDate"
      :min="currentDate"
      @update:model-value="getPlantingTimeline"
    ></v-date-picker>
  </v-container>

  <v-container class="pa-0 mt-5 mb-5" v-if="!selectedDate"> <p>
      Select a date and we will show you a timeline of your future planting
      journey.
    </p>
  </v-container>

  <v-container class="pa-0 mt-5 mb-5" v-else>
    <h2>Important Dates</h2>
    <div v-if="isLoadingTimeline" class="d-flex justify-center align-center py-5">
      <v-progress-circular
        indeterminate
        color="primary"
        size="64"
        width="6"
      ></v-progress-circular>
    </div>

    <v-timeline
      v-else
      align="start"
      direction="vertical"
      dot-color="primary"
      side="end"
      truncate-line="both"
    >
      <v-timeline-item
        v-for="(item, index) in combinedTimeline"
        :key="index"
      >
        <v-sheet
          border="sm"
          color="accent"
          rounded="lg"
          class="pa-2 d-flex align-center timeline-card"
        >
          <v-avatar size="60" rounded="0" class="mr-4 flex-shrink-0">
            <v-img :src="getImageForEvent(item.event)" :alt="item.event"></v-img>
          </v-avatar>
          <div class="timeline-text-content">
            <p class="font-weight-bold mb-0 timeline-title-row">
              <v-chip
                color="primary"
                size="default"
                rounded="pill"
                class="mr-2 date-chip-match-title"
              >
                {{ formatDate(new Date(item.date)) }}
              </v-chip>
              <span class="timeline-title">{{ item.event }}</span>
            </p>
            <p class="text-caption mt-0 mb-0">{{ getDescriptionForEvent(item.event) }}</p>
          </div>
        </v-sheet>
      </v-timeline-item>
    </v-timeline>
  </v-container>
</template>

<script setup lang="ts">
import { useVegetablesStore } from "@/stores/vegetable";
import { useProgressStore } from "@/stores/progress";
import { ref, computed } from "vue";
import { storeToRefs } from "pinia";

const vegetableStore = useVegetablesStore();
const progressStore = useProgressStore();
const { timeline } = storeToRefs(progressStore);
const selectedVegetable = vegetableStore.selectedVegetable;
const currentDate = new Date();
currentDate.setDate(currentDate.getDate() - 1);
const selectedDate = ref<Date | null>(null);
const isLoadingTimeline = ref(false);

const calculateEstimatedHarvestDate = computed(() => {
  if (!selectedDate.value) return null;
  const estimatedHarvestDate = new Date(selectedDate.value);
  if (selectedVegetable && selectedVegetable.estimated_harvest_time_in_seconds !== undefined) {
    estimatedHarvestDate.setSeconds(
      selectedDate.value.getSeconds() +
      selectedVegetable.estimated_harvest_time_in_seconds
    );
  } else {
    console.warn("estimated_harvest_time_in_seconds not found for selected vegetable.");
    return null;
  }
  return estimatedHarvestDate;
});

const combinedTimeline = computed(() => {
  let events: { date: Date | string; event: string; isHarvest?: boolean }[] = [];
  if (selectedDate.value) {
    events.push({ date: selectedDate.value, event: "Start planting" });
  }
  if (timeline.value && timeline.value.length > 0) {
    const aiEvents = timeline.value.filter(item => item.event !== "Start planting").map(item => ({
      date: item.date,
      event: item.event
    }));
    events = events.concat(aiEvents);
  }
  if (calculateEstimatedHarvestDate.value) {
    events.push({ date: calculateEstimatedHarvestDate.value, event: "Ready to harvest!", isHarvest: true });
  }
  return events.sort((a, b) => {
    const dateA = new Date(typeof a.date === 'string' ? a.date.replace(/,/g, '') : a.date).getTime();
    const dateB = new Date(typeof b.date === 'string' ? b.date.replace(/,/g, '') : b.date).getTime();
    return dateA - dateB;
  });
});


async function getPlantingTimeline() {
  if (selectedDate.value) {
    isLoadingTimeline.value = true; // Set loading to true before fetching
    try {
      await progressStore.getPlantingTimeline(selectedDate.value);
    } finally {
      isLoadingTimeline.value = false; // Set loading to false after fetch (success or error)
    }
  }
}

const getImageForEvent = (eventName: string): string => {
  switch (eventName) {
    case "Start planting":
      return "/images/timeline/planting.png";
    case "Check Soil":
      return "/images/timeline/check.png";
    case "Fertilize":
      return "/images/timeline/fertilize.png";
    case "Check for Pests":
      return "/images/timeline/pesticide.png";
    case "Check Pot Size":
      return "/images/timeline/size.png";
    case "Ready to harvest!":
      return "/images/timeline/harvest.png";
    case "First sprouts":
        return "/images/timeline/sprouts.png";
    case "Checkup":
        return "/images/timeline/checkup.png";
    default:
      return "/images/timeline/default.png";
  }
};

const getDescriptionForEvent = (eventName: string): string => {
  const vegetableName = selectedVegetable?.name || "your plant";

  switch (eventName) {
    case "Start planting":
      return "Here's where your journey starts! We'll guide you through planting the seeds.";
    case "Fertilize":
      return `We'll add fertilizer to boost the yield of your ${vegetableName}.`;
    case "Check Soil":
      return `Check the soil moisture and nutrients to ensure healthy growth for your ${vegetableName}.`;
    case "Check for Pests":
      return `Inspect your ${vegetableName} for any signs of pests and address them.`;
    case "Check Pot Size":
      return `Determine if your ${vegetableName} needs a larger pot for root expansion.`;
    case "Ready to harvest!":
      return `Your hard work has paid off. Time to enjoy your fresh ${vegetableName} produce!`;
    case "First sprouts":
      return `Signs of your hard work paying off for your ${vegetableName}.`;
    case "Checkup":
      return `Let's see how your ${vegetableName} is growing.`;
    default:
      return `An important step in your ${vegetableName} planting journey.`;
  }
};

const formatDate = (date: Date): string => {
  const options: Intl.DateTimeFormatOptions = { weekday: 'short', month: 'short', day: '2-digit', year: 'numeric' };
  return new Intl.DateTimeFormat('en-US', options).format(date).replace(/,/g, '');
};
</script>

<style scoped>
/* Ensure flexbox for vertical alignment and spacing */
.v-sheet.d-flex {
  display: flex;
  align-items: flex-start; /* Changed from 'center' to 'flex-start' to align content to the top */
  box-sizing: border-box; /* Include padding and border in the total height */
  /* Increased width to make the box longer */
  width: 450px; /* Adjust this value as needed for your desired longer card width */
  max-width: 100%; /* Ensures it's responsive on smaller screens */
}
/* Styles for the row containing the date chip and the event title */
.timeline-title-row {
  display: flex;
  align-items: center; /* Align items (chip and span) vertically */
  font-size: 1rem; /* Base font size for this row */
  line-height: 1.3; /* Line height for consistent spacing */
  margin-bottom: 4px; /* Small space between title row and description */
}
/* Styling for the description text */
.text-caption {
  font-size: 0.85rem;
  color: #666; /* Lighter color for description */
  line-height: 1.2;
  white-space: normal; /* Allow text to wrap naturally */
  overflow: hidden; /* Hide overflow if text is too long */
  text-overflow: ellipsis; /* Add ellipsis for overflowed text */
  display: -webkit-box; /* For multi-line ellipsis in Webkit browsers */
  -webkit-line-clamp: 2; /* Limit description to 2 lines */
  -webkit-box-orient: vertical;
}

/* Style to make the date chip match the title size */
.date-chip-match-title {
  height: 28px !important; /* Adjust this value to precisely match the height of your title text */
  padding: 0 10px !important; /* Adjust horizontal padding to control width */
  font-size: 0.9rem !important; /* Adjust font size within the chip */
  text-transform: none !important; /* Prevent text from becoming uppercase */
  font-weight: 500; /* Medium weight for the date text within the chip */
  display: flex; /* Ensure flex for content alignment within the chip */
  align-items: center; /* Center text vertically within the chip */
  flex-shrink: 0; /* Prevent the chip from shrinking */
}
</style>