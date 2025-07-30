<template>
  <v-app class="app-background">
    <v-container class="main-container">
      <v-row align="center" justify="center" class="h-100">
        <v-col cols="12" md="6" class="text-column">
          <div class="text-content">
            <h1 class="main-heading" v-if="localVegetableImage">
              You've added a photo of
              <span class="plant-nickname">{{ plantNickname }}</span>
            </h1>
            <h1 class="main-heading" v-else>
              Add a photo of your
              <span class="plant-nickname">{{ plantNickname }}</span>
            </h1>

            <p class="sub-text" v-if="localVegetableImage">
              If you're happy with the photo, we're ready to proceed with the
              checkup on {{ plantNickname }}.
            </p>
            <p class="sub-text" v-else>
              We'll need a photo of your {{ plantNickname }} to let you know how
              it's doing.
            </p>

            <input
              type="file"
              ref="fileInputRef"
              accept="image/*"
              @change="handleFileChange"
              style="display: none"
            />

            <CallToActionButton
              v-if="localVegetableImage"
              to="/checkupChatbot"
              @button-clicked="uploadAndNavigate"
              class="checkup-button mt-6"
            >
              Checkup ({{ plantNickname }})
            </CallToActionButton>
          </div>
        </v-col>

        <v-col cols="12" md="6" class="image-column d-flex justify-center">
          <div class="image-display-area">
            <v-img
              v-if="imagePreviewUrl"
              :src="imagePreviewUrl"
              alt="Uploaded Plant"
              class="plant-image"
              cover
            ></v-img>
            <div v-else class="image-placeholder d-flex align-center justify-center flex-column">
              <v-icon size="80" color="#BDBDBD">mdi-camera</v-icon>
              <p class="placeholder-text mt-2">Upload your plant image here</p>
            </div>
            <v-btn
              class="upload-button"
              icon
              size="large"
              @click="triggerFileInput"
            >
              <v-icon>mdi-camera-plus</v-icon>
            </v-btn>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import CallToActionButton from "@/components/CallToActionButton.vue";
import { useUserStore } from "@/stores/user";

const localVegetableImage = ref<File | null>(null); // Use a local ref for file
const userStore = useUserStore();
const fileInputRef = ref<HTMLInputElement | null>(null); // Ref for the hidden file input
const plantNickname = ref("Kangkung"); // Example: Make this dynamic if needed

const imagePreviewUrl = computed(() => {
  if (localVegetableImage.value) {
    return URL.createObjectURL(localVegetableImage.value);
  }
  return null;
});

function triggerFileInput() {
  fileInputRef.value?.click(); // Programmatically click the hidden file input
}

function handleFileChange(event: Event) {
  const target = event.target as HTMLInputElement;
  if (target.files && target.files[0]) {
    localVegetableImage.value = target.files[0];
  } else {
    localVegetableImage.value = null;
  }
}

function uploadAndNavigate() {
  if (localVegetableImage.value) {
    userStore.newUploadedPhoto(localVegetableImage.value);
    // Navigation is handled by CallToActionButton's 'to' prop
  }
}
</script>

<style scoped>
/* Assuming the "peach" color is #f5f5f5 or similar from previous contexts. Adjust as needed. */
.app-background {
  min-height: 100vh;
  display: flex;
}

.main-container {
  max-width: 1200px;
  width: 100%;
  padding: 40px 20px;
  display: flex; /* Ensure it takes full height within app-background */
  flex-grow: 1;
}

.h-100 {
  height: 100%;
}

.text-column {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: left;
  padding-right: 40px; /* Space between text and image */
}

.text-content {
  max-width: 450px; /* Constrain text width for better readability */
}

.main-heading {
  font-size: 2.5rem; /* Larger font size */
  font-weight: 700; /* Bold */
  color: #333; /* Darker text */
  margin-bottom: 15px;
  line-height: 1.2;
}

.plant-nickname {
  color: #4caf50; /* Green color for the nickname */
}

.sub-text {
  font-size: 1.1rem;
  color: #555;
  line-height: 1.6;
  margin-bottom: 30px;
}

.image-column {
  display: flex;
  align-items: center;
  justify-content: center;
  padding-left: 40px; /* Space between text and image */
}

.image-display-card {
  width: 100%;
  max-width: 450px; /* Fixed size for the image card */
  height: 450px;
  border-radius: 15px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1); /* More prominent shadow */
  overflow: hidden;
  background-color: #e7e7e4; /* background for the card */
  position: relative; /* For positioning the upload button */
  display: flex; /* For placeholder centering */
  align-items: center;
  justify-content: center;
}


.plant-image {
  width: 100%;
  height: 100%;
  object-fit: contain; /* Changed to contain to fit the image without cropping if aspect ratios differ */
}

.image-placeholder {
  width: 100%;
  height: 100%;
  background-color: #e7e7e4; /* placeholder background */
  color: #e7e7e4;
  font-size: 1.2em;
  text-align: center;
}

.placeholder-text {
  font-size: 1em;
  color: #757575;
}

.upload-button {
  position: absolute;
  bottom: 20px;
  right: 20px;
  background-color: #4caf50 !important; /* Green button */
  color: white !important;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Shadow for the button */
  z-index: 5; /* Ensure it's above the image */
}

.checkup-button {
  width: auto !important; /* Allow button to size to content */
  padding: 12px 30px !important; /* Adjust padding for a larger button */
  border-radius: 8px !important; /* Slightly rounded corners */
  font-size: 1.1em !important;
  letter-spacing: 0.5px !important;
  text-transform: none !important; /* Keep original casing */
  background-color: #4caf50 !important; /* Green button */
  color: white !important;
  font-weight: bold;
}

/* Disabled state styling for the checkup button - this block is now redundant if v-if is used */
/*
.checkup-button[disabled] {
  opacity: 0.6;
  pointer-events: none;
  background-color: #a5d6a7 !important;
}
*/

@media (max-width: 960px) {
  /* On smaller screens (md and below), stack columns */
  .text-column, .image-column {
    padding-left: 15px;
    padding-right: 15px;
  }
  .text-column {
    order: 2; /* Text below image on small screens */
    text-align: center;
    margin-top: 30px;
  }
  .image-column {
    order: 1; /* Image above text on small screens */
  }
  .image-display-area {
    height: 300px; /* Adjust height for smaller screens */
    width: 300px;
  }
  .main-heading {
    font-size: 2rem;
  }
  .sub-text {
    font-size: 1em;
  }
}
</style>