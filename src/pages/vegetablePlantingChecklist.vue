<template>
  <section id="checklist" class="mb-4">
    <div class="instructions mb-4">
      <h2 class="text-center mb-3">Let's get ready to grow</h2>
      <p>
        Below is a checklist of materials you’ll need to get ready before we
        start. Check each item off the list if you have them. When you’re ready,
        tap on the button to proceed.
      </p>
    </div>
    <v-container class="pa-0 mb-4">
      <ChecklistItemCard></ChecklistItemCard>
    </v-container>
    <RouterLink :to="`/calendar`">
      <CallToActionButton button-text="I'm ready to plant"></CallToActionButton>
    </RouterLink>
  </section>
  <section id="where-to-buy">
    <h3 class="mb-3">Where to buy</h3>
    <div class="item-to-buy">
      <div class="item-category d-flex flex-row align-center ga-4">
        <image src="https://placehold.co/60x40.png"></image>
        <h4>Item Name</h4>
      </div>
      <WhereToBuyCard></WhereToBuyCard>
    </div>
  </section>
</template>

<script setup lang="ts">
import CallToActionButton from "../components/CallToActionButton.vue";
import ChecklistItemCard from "../components/ChecklistItemCard.vue";
import WhereToBuyCard from "../components/WhereToBuyCard.vue";
</script>
