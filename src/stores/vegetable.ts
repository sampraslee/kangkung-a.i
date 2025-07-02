import axios from "axios";
import { defineStore } from "pinia";

export const useVegetablesStore = defineStore("vegetable", {
  state: () => ({
    vegetables: [],
    selectedVegetable: null,
  }),
  getters: {
    getVegetableById: (state) => {
      return (vegetableID) =>
        state.vegetables.find((vegetable) => vegetable.id === vegetableID);
    },
    getVegetableDetails: (state) => {
      return state.selectedVegetable;
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
    async selectVegetable(vegetableId) {
      const url = `http://127.0.0.1:8000/vegetables/${vegetableId}`;
      try {
        const response = await axios.get(url);
        this.selectedVegetable = response.data;
        console.log(this.selectedVegetable);
      } catch (error) {
        console.log(error.message);
      }
    },
  },
});
