<template>
  <a :href="'https://www.google.com'" target="_blank" style="text-decoration: none;">
    <v-card class="d-flex ga-4 pa-4 rounded-lg" style="cursor: pointer;">
      <img :src="videoThumbnail" class="videoThumbnail" />
      <div class="video-info">
        <v-card-title class="pa-0">{{ videoTitle }}</v-card-title>
        <v-card-text class="pa-0">
          {{ videoSummary }}
        </v-card-text>
      </div>
    </v-card>
  </a>
</template>

<script setup lang="ts">
const props = defineProps({
  videoThumbnail: {
    type: String,
    default: "https://placehold.co/40@3x.png",
  },
  videoTitle: {
    type: String,
    default: "Video Title XXX",
  },
  videoSummary: {
    type: String,
    default: "This is an A.I generated summary of the video.",
  },
  videoLink: {
    type: String,
    default: "#"
  }
})
</script>