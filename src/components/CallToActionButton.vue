<template>
  <v-btn class="bg-primary text-white w-100">{{ buttonText }}</v-btn>
</template>

<script setup lang="ts">
const props = defineProps({
  buttonText: {
    type: String,
    default: "Button text",
  },
});
</script>
