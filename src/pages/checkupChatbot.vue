<template>
  <v-textarea
    class="position-fixed bottom-0 no-resize bg-white"
    rows="3"
    width="90%"
    variant="outlined"
  ></v-textarea>
  <v-img :src="imageUrl" class="w-66 cover" />
  <p v-if="llmResponse">
    {{ llmResponse }}
  </p>
</template>

<script setup lang="ts">
import axios from "axios";
import { ref, computed } from "vue";
import { useUserStore } from "@/stores/user";

const userStore = useUserStore();
let llmResponse = ref(null);

const imageUrl = computed(() => {
  if (userStore.uploadedPhoto) {
    return URL.createObjectURL(userStore.uploadedPhoto);
  }
  return null;
});

async function imageAnalysis(image) {
  const url = "http://127.0.0.1:8000/AItool/image_analysis";
  const formData = new FormData();
  formData.append("file", image);
  try {
    const response = await axios.post(url, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    console.log("Analysis successful:", typeof response.data, response.data);
    llmResponse.value = response.data;
    console.log(llmResponse);
    return response.data;
  } catch (error) {
    if (error.response) {
      console.error("Error Response:", error.response.data);
      console.error("Error Status:", error.response.status);
    }
  }
}

watch(
  () => userStore.uploadedPhoto,
  (newPhoto) => {
    if (newPhoto) {
      console.log("New photo detected, starting analysis...");
      // Pass the ACTUAL file object to the function
      imageAnalysis(newPhoto);
    }
  },
  { immediate: true }
);
</script>
