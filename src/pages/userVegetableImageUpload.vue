<template>
  <div class="mb-5" v-if="vegetableImage != null">
    <h1>You've added a photo of your kangkung</h1>
    <p>If you're happy with the photo, let's proceed with the checkup.</p>
  </div>
  <div class="mb-5" v-else>
    <h1>Add a photo of your kangkung</h1>
    <p>We'll need a photo of your kangkung to let you know how it's doing.</p>
  </div>
  <v-file-upload
    border="sm"
    browse-text="Choose photo"
    clearable
    color="accent"
    density="default"
    divider-text=""
    title="Upload a photo of kangkung"
    v-model="vegetableImage"
  ></v-file-upload>

  <RouterLink to="/checkupChatbot">
    <CallToActionButton
      button-text="Analyze"
      @click="UploadPhotoFile(vegetableImage)"
      v-if="vegetableImage != null"
    ></CallToActionButton>
  </RouterLink>
</template>

<script setup lang="ts">
import { ref } from "vue";
import CallToActionButton from "@/components/CallToActionButton.vue";
import { useUserStore } from "@/stores/user";

const vegetableImage = ref(null);
const userStore = useUserStore();

function UploadPhotoFile(file: File | null){
  if(file != null){
    userStore.newUploadedPhoto(file);
    console.log(file);
  }
}

function logUploadedImg() {
  console.log(typeof vegetableImage.value);
  console.log(vegetableImage.value);
}
</script>
