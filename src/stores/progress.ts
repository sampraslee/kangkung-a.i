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
    async getPlantingTimeline(started: Date) {
      const progressId = "2"; 
      const requestBody = {
          startDate: started.toISOString(), 
      };
      try {
          const updateUrl = `http://127.0.0.1:8000/progress/${progressId}`;
          const updateResponse = await axios.patch(updateUrl, requestBody, {
              headers: { 'Content-Type': 'application/json' },
          });
          console.log("ayamm")
          console.log(requestBody);
          console.log("Start date updated successfully:", updateResponse.data);

      } catch (error) {
          console.error("Failed to update start date:", error);
      }
      const timelineUrl = `http://127.0.0.1:8000/AItool/calculate-dates/${progressId}`;
      try {
          const timelineResponse = await axios.get(timelineUrl);
          this.timeline = timelineResponse.data;
          console.log("Timeline fetched successfully:", this.timeline);
      } catch (error) {
          console.error("Failed to fetch timeline:", error);
      }
    }
  },
});
