<template>
  <v-btn class="bg-primary text-white font-weight-black w-100 flex-column align-center" size="large">
    {{ buttonText }}
  </v-btn>
</template>

<script>
export default {
  name: "CallToActionButton",
  props: {
    buttonText: {
      type: String,
      default: "Button text",
    },
  },
};
</script>
