<template>
  <v-card class="d-flex ga-4 pa-4 rounded-lg">
    <img :src="props.itemImageUrl" class="item-img">
    </img>
    <div class="item-info">
      <v-card-title class="pa-0">{{ itemName }}</v-card-title>
      <v-card-text class="pa-0"
        >{{ itemDescription }}</v-card-text
      >
    </div>
    <v-checkbox color="primary"></v-checkbox>
  </v-card>
</template>

<script setup lang="ts">
  const props = defineProps({
    itemImageUrl: {
      type: String,
      default: "https://placehold.co/40@3x.png",
    },
    itemName: {
      type: String,
      default: "Item Name",
    },
    itemDescription: {
      type: String,
      default: "This is the description of the item the user needs.",
    },

  })
</script>
