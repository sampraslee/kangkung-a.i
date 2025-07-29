<template>
  <v-card
    class="pa-6 ga-4 border-sm rounded-lg d-flex flex-row fill-height" border="none"
    elevation="0"
  >
    <v-img src="/public/images/info.png" width="180" v-if="!loading && !error"></v-img>
    <div class="information">
      <h3 class="text-primary900">For your information</h3>
      <p>
        <span v-if="loading">Loading...</span>
        <span v-else-if="error" class="text-error">{{ error }}</span>
        <span v-else>{{ weatherNotification }}</span>
      </p>
    </div>
  </v-card>
</template>

<script>
import axios from 'axios';

export default {
  name: 'InfoCard',
  data() {
    return {
      weatherNotification: '',
      loading: true,
      error: null
    }
  },
  async mounted() {
    try {
      const response = await axios.get('http://localhost:8000/AItool/weather-notification');
      this.weatherNotification = response.data.notification;
      this.loading = false;
    } catch (e) {
      console.error("Error fetching weather notification:", e);
      this.error = 'Failed to load weather notification';
      this.loading = false;
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