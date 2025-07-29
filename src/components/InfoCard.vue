<template>
  <v-card
    class="pa-6 ga-4 border-sm rounded-lg d-flex flex-row fill-height"
    border="none"
    elevation="0"
  >
    <div v-if="loading" class="d-flex justify-center align-center fill-height flex-grow-1">
      <v-progress-circular indeterminate color="primary" size="40" width="4"></v-progress-circular>
    </div>

    <div v-else-if="error" class="d-flex justify-center align-center fill-height flex-grow-1">
      <p class="text-error">{{ error }}</p>
    </div>

    <template v-else>
      <v-img src="/public/images/info.png" width="180"></v-img>
      <div class="information">
        <h3 class="text-primary900">For your information</h3>
        <p>
          <span>{{ weatherNotification }}</span>
        </p>
      </div>
    </template>
  </v-card>
</template>

<script>
import axios from 'axios';

export default {
  name: 'InfoCard',
  data() {
    return {
      weatherNotification: '',
      loading: true, // Initial state set to true to show loader on mount
      error: null
    }
  },
  async mounted() {
    try {
      const response = await axios.get('http://localhost:8000/AItool/weather-notification');
      this.weatherNotification = response.data.notification;
    } catch (e) {
      console.error("Error fetching weather notification:", e);
      this.error = 'Failed to load weather notification';
    } finally {
      this.loading = false; // Always set loading to false after the operation
    }
  }
}
</script>

<style scoped>
.information {
  flex-grow: 1;
}

.text-error {
  color: red;
}
</style>