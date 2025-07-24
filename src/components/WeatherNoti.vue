<template>
  <v-card
    class="mx-auto"
    max-width="400"
    outlined
  >
    <v-row no-gutters>
      <v-col cols="auto" class="mr-3">
        <v-icon size="60" class="mt-3 ml-3">{{ icon }}</v-icon>
      </v-col>
      <v-col>
        <v-list-item three-line>
          <v-list-item-content>
            <div class="text-overline mb-4">For your information</div>
            <v-list-item-title class="text-h5 mb-1">Weekly Weather Update</v-list-item-title>
            <v-list-item-subtitle v-if="loading">Loading...</v-list-item-subtitle>
            <v-list-item-subtitle v-else-if="error">{{ error }}</v-list-item-subtitle>
            <v-list-item-subtitle v-else>{{ weatherNotification }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-col>
    </v-row>
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
      icon: 'mdi-weather-cloudy'
    }
  },
  async mounted() {
    try {
      const response = await axios.get('http://localhost:8000/AItool/weather-notification'); //create api for this...
      this.weatherNotification = response.data.notification;
      this.loading = false;
    } catch (e) {
      this.error = 'Failed to load weather notification';
      this.loading = false;
    }
  }
}
</script>