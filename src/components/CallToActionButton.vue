<template>
  <v-btn class="bg-primary text-white w-100 font-weight-black" size="large">
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
