<template>
  <v-card
    class="pa-6 ga-4 border-sm rounded-lg d-flex flex-row"
    border="none"
    elevation="0"
  >
    <v-img src="/public/images/info.png" width="180"></v-img>
    <div class="information">
      <h3 class="text-primary900">For your information</h3>
      <p>
        <v-list-item-subtitle v-if="loading">Loading...</v-list-item-subtitle>
        <v-list-item-subtitle v-else-if="error">{{ error }}</v-list-item-subtitle>
        <v-list-item-subtitle v-else>{{ weatherNotification }}</v-list-item-subtitle>
      </p>
    </div>
  </v-card>
</template>
<script>
import axios from 'axios';

export default {
  name: 'WeatherNotificationCard',
  data() {
    return {
      weatherNotification: '',
      loading: true,
      error: null,
    }
  },
  async mounted() {
    try {
      const response = await axios.get('http://localhost:8000/AItool/weather-notification');
      this.weatherNotification = response.data.notification;
      this.loading = false;
    } catch (e) {
      this.error = 'Failed to load weather notification';
      this.loading = false;
    }
  }
}</script>
