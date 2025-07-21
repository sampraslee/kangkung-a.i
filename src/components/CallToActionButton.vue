<template>
  <v-btn
    class="bg-primary text-white font-weight-black w-100 flex-column align-center"
    size="large"
  >
    <slot></slot>
  </v-btn>
</template>

<script>
export default {
  name: "CallToActionButton",
};
</script>
