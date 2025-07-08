<template>
  <h1>You've added a photo of </h1>
  <v-img
    :src="imageUrl"
    class="w-200 framed-image"
  />
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import { useUserStore } from "@/stores/user";

const userStore = useUserStore();

const imageUrl = computed(() => {
  if (userStore.uploadedPhoto) {
    return URL.createObjectURL(userStore.uploadedPhoto);
  }
  return null;
})

</script>
