<template>
  <v-card class="mb-4">
    <v-img
      src="https://placehold.co/600x400"
      height="200px"
      cover
    ></v-img>
    <v-card-title>How to Grow Kangkung (Water Spinach)</v-card-title>
    <v-card-text>
      This video shows step-by-step instructions for growing kangkung at home.
    </v-card-text>
    <v-card-actions>
      <v-btn
        color="primary"
        href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        target="_blank"
      >
        Watch Video
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "VideoCard"
};
</script>


<!-- <template>
  <v-card class="d-flex flex-column ga-4 pa-4 rounded-lg">
    <img :src="props.videoThumbnail" class="video-thumbnail">
    </img>
    <div class="video-info">
      <v-card-title class="pa-0">{{ videoTitle }}</v-card-title>
      <v-card-text class="pa-0">{{ videoSummary }}</v-card-text>
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
</script> -->