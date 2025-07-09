<template>
  <v-textarea
    class="position-absolute bottom-0"
    width="90%"
    variant="outlined"
  ></v-textarea>
  <v-img :src="imageUrl" class="w-66 cover" />
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
});
</script>
