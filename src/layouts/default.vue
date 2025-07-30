<template>
  <v-app>
    <v-app-bar style="position: fixed; top: 0; width: 100%; z-index: 1004" elevation="2" color="primary"
      density="compact">
      <template #prepend>
        <v-app-bar-nav-icon v-if="showBackButton" icon="mdi-arrow-left" @click="goBack"></v-app-bar-nav-icon>
      </template>

      <v-spacer></v-spacer>
      <div class="d-flex align-center" style="cursor: pointer" @click="router.push('/')">
        <v-avatar image="/images/KangkungAI.png" size="40" class="mr-4 avatar-border"></v-avatar>
        <span class="font-weight-bold text-h5">KANGKUNG AI</span>
      </div>
      <v-spacer></v-spacer>

      <template #append>
        <div v-if="showBackButton" style="width: 48px"></div>
      </template>
    </v-app-bar>
    <v-main class="ml-auto mr-auto w-90 w-lg-75" style="padding-top: 60px; padding-bottom: 60px;">
      <router-view />
    </v-main>
    <v-footer style="position: fixed; bottom: 0; width: 100%; z-index: 1005;" class="d-flex justify-center text-caption"
      color="primary">
      <span class="text-h7">Created by: Team 5</span>
    </v-footer>
  </v-app>
</template>
<script lang="ts" setup>
import { computed, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
const route = useRoute();
const router = useRouter();

watch(
  () => route.path,
  () => window.scrollTo(0, 0)
);

// Define routes where the back button should be hidden
const noBackButtonRoutes = ["/", "/userLogin"];
const showBackButton = computed(() => !noBackButtonRoutes.includes(route.path));
const goBack = () => router.back();
</script>
<style scoped>
.avatar-border {
  border: 2px solid #1B5E20;
  /* dark green */
}
</style>
