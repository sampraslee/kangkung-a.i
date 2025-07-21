<template>
  <v-card
    class="d-flex flex-column ga-4 pa-4 rounded-lg"
    elevation="0"
    width="280"
  >
    <v-img :src="videoThumbnail" class="videoThumbnail" />
    <div class="d-flex flex-column video-info justify-space-between">
      <div class="video-copy">
        <v-card-title class="pa-0 font-weight-bold">{{
          videoTitle
        }}</v-card-title>
        <v-card-text class="pa-0">
          {{ videoSummary }}
        </v-card-text>
      </div>
      <a :href="videoLink" class="text-primary">Watch video</a>
    </div>
  </v-card>
</template>

<script setup lang="ts">
const props = defineProps({
  videoThumbnail: {
    type: String,
    default: "https://placehold.co/40@3x.png",
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
