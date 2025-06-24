import axios from "axios";
import { defineStore } from "pinia";

export const useVegetablesStore = defineStore("vegetable", {
  state: () => ({
    vegetables: [],
  }),
  getters: {
    getVegetableById: (state) => {
      return (vegetableID) =>
        state.vegetables.find((vegetable) => vegetable.id === vegetableID);
    },
  },
  actions: {
    async getVegetables() {
      const url = "http://127.0.0.1:8000/vegetables/";

      try {
        const response = await axios.get(url);
        this.vegetables = response.data;
        console.log(this.vegetables);
      } catch (error) {
        console.log(error.message);
      }
    },
  },
});
