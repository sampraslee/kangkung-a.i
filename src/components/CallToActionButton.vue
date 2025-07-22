<template>
  <v-btn
    class="bg-primary text-white text-decoration-none font-weight-black w-100 flex-column align-center"
    size="large"
    :to="to"
    @click="$emit('button-clicked')"
  >
    <slot></slot>
  </v-btn>
</template>

<script setup lang="ts">
defineProps({
  to: {
    type: String,
    required: true,
  },
});

defineEmits(["button-clicked"]);
</script>
