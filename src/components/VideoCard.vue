<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-sheet rounded="lg" class="pa-4 mb-4">
          <h3 class="text-h5 font-weight-bold mb-4">{{ title }}</h3>
        <div class="video-carousel-wrapper">
          <v-carousel
            v-model="currentSlide"
            :show-arrows="false"
            hide-delimiter-background
            height="auto"
            touch
            class="custom-carousel"
          >
            <v-carousel-item v-for="(video, index) in videos" :key="index">
              <v-card variant="outlined" max-width="600" class="mb-4">
                <v-row no-gutters>
                  <v-col cols="4" sm="3">
                    <v-img
                      :src="video.thumbnail"
                      aspect-ratio="1"
                      class="bg-grey-lighten-2"
                      cover
                    >
                      <template v-slot:placeholder>
                        <div
                          class="d-flex align-center justify-center fill-height"
                        >
                          <v-icon
                            color="grey-darken-1"
                            icon="mdi-camera"
                            size="x-large"
                          ></v-icon>
                        </div>
                      </template>
                    </v-img>
                  </v-col>

                  <v-col cols="8" sm="9">
                    <v-card-text>
                      <p class="text-subtitle-1 font-weight-bold">
                        {{ video.title }}
                      </p>

                      <p class="text-caption text-medium-emphasis">
                        {{ video.duration }}
                      </p>

                      <p class="text-body-2 mt-2">
                        {{ video.summary }}
                      </p>
                    </v-card-text>
                  </v-col>
                </v-row>
              </v-card>
            </v-carousel-item>
          </v-carousel>
        </div>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
  title: {
    type: String,
    default: "Videos for you:",
  },
  videos: {
    type: Array,
    default: () => [
      {
        title: "Video Title",
        duration: "Video Duration",
        summary: "This will be the A.I summary of the video.",
        thumbnail: null,
      },
    ],
  },
});

const currentSlide = ref(0);
</script>

<style scoped>
.v-card-text {
  padding: 12px;
}

.video-carousel-wrapper {
  position: relative;
  padding-bottom: 40px;
}

/* Customize carousel height */
:deep(.v-carousel) {
  min-height: 200px;
}

/* Style carousel controls */
:deep(.v-carousel__controls) {
  position: absolute;
  background: transparent !important;
}

:deep(.v-btn--icon.v-carousel__controls__item) {
  color: rgba(0, 0, 0, 0.87) !important;
  margin: 0 5px;
}

:deep(.v-btn--icon.v-carousel__controls__item.v-btn--active) {
  color: #000000 !important;
}

:deep(.v-carousel__controls__item .v-btn__content) {
  transform: scale(1);
}
</style>
