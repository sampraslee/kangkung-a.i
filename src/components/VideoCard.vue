<template>
  <v-card
    class="d-flex flex-row ga-4 pa-4 rounded-lg align-start"
    elevation="0"
  >
    <v-avatar size="100" rounded="lg" class="bg-grey-lighten-4 flex-shrink-0">
      <v-img :src="videoThumbnail" cover></v-img>
    </v-avatar>
    <div class="d-flex flex-column ga-2">
      <div>
        <v-card-title class="pa-0 font-weight-bold">{{
          videoTitle
        }}</v-card-title>
        <v-card-text class="pa-0"> {{ videoSummary }} </v-card-text>
      </div>
      <a :href="videoLink" class="text-primary">Watch video</a>
    </div>
  </v-card>
</template>

<script setup lang="ts">
const props = defineProps({
  videoThumbnail: {
    type: String,
    default: "https://placehold.co/100x100.png",
  },
  videoTitle: {
    type: String,
    default: "Video title",
  },
  videoSummary: {
    type: String,
    default: "This is the description for the video.",
  },
  videoLink: {
    type: String,
    default: "https://youtu.be/dQw4w9WgXcQ?si=WrPOjesR3ny1USz2",
  },
});
</script>
