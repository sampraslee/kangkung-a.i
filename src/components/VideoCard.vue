<template>
  <v-card class="d-flex flex-column ga-4 pa-4 rounded-lg">
    <img :src="props.videoThumbnail" class="video-thumbnail">
    </img>
    <div class="video-info">
      <v-card-title class="pa-0">{{ videoTitle }}</v-card-title>
      <v-card-text class="pa-0"
        >{{ videoSummary }}</v-card-text
      >
      <a :href="props.videoLink" class="text-color-primary">Watch Video</a>
    </div>
  </v-card>
</template>

<script setup lang="ts">
const props = defineProps({
  videoThumbnail: {
    type: String,
    default: "https://placehold.co/40@3x.png"
  },
  videoTitle: {
    type: String,
    default: "Video title"
  },
  videoSummary: {
    type: String,
    default: "This is an A.I generated summary of the video."
  },
  videoLink: {
    type: String,
    default: "#"
  }
})
</script>
