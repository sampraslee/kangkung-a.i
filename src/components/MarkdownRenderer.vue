<template>
  <div v-html="renderedHtml"></div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { marked } from "marked";

// Define the component's props
const props = defineProps<{
  content: string;
}>();

// Create a computed property that automatically converts the
// markdown content to HTML whenever the content changes.
const renderedHtml = computed(() => {
  if (props.content) {
    return marked.parse(props.content);
  }
  return "";
});
</script>

<style>
/* Optional: Add some basic styling for the rendered HTML */
.markdown-renderer p {
  margin-bottom: 1rem;
}
.markdown-renderer ul,
.markdown-renderer ol {
  padding-left: 2rem;
}
</style>
