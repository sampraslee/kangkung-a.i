import axios from "axios";
import { defineStore } from "pinia";

export const useProgressStore = defineStore("progress", {
  state: () => ({
    timeline: [],
    userProgress: [],
  }),
  actions: {
    async getUserProgress(userID: number) {
      const url = `http://127.0.0.1:8000/progress/${userID}`;

      try {
        const response = await axios.get(url);
        console.log(response.data);
        this.userProgress = response.data;
        console.log(this.userProgress);
        // console.log(typeof this.useProgress);
      } catch (error: any) {
        console.log(error.message);
      }
    },
    // Send the vegetable data to Gemini to generate timeline
    async getPlantingTimeline() {
      const url = "http://127.0.0.1:8000/AItool/calculate-dates/2/";

      try {
        const response = await axios.get(url);
        console.log(response.data);
        this.timeline = response.data;
        console.log("timeline from pinia");
        console.log(this.timeline);
      } catch (error: any) {
        console.log(error.message);
      }
    },
  },
});
