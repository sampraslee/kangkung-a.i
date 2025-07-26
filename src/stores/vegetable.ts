import axios from "axios";
import { defineStore } from "pinia";

export const useVegetablesStore = defineStore("vegetable", {
  state: () => ({
    vegetables: [],
    usersVegetables: null,
    materials: [],
    selectedVegetable: null,
    filteredVegetables: [],
    selectedMaterial: null,
    isLoading: false,
  }),

  getters: {
    // Get the currently selected vegetable
    getVegetableDetails: (state: any) => {
      return state.selectedVegetable;
    },

    // Get all materials associated with a vegetableID
    getMaterialDetails: (state: any) => {
      return (vegetableID: number | string) =>
        state.materials.filter(
          (material: any) =>
            Array.isArray(material.vegetables) &&
            material.vegetables.some((veg: any) => veg.id === vegetableID)
        );
    },

    // Get unique materials for a vegetableID (no duplicates)
    getUniqueMaterialsForVegetable: (state: any) => (vegetableID: number) => {
      const materials = state.materials.filter(
        (material: any) =>
          Array.isArray(material.vegetables) &&
          material.vegetables.some((veg: any) => veg.id === vegetableID)
      );
      const seen = new Set();
      return materials.filter((material: any) => {
        if (seen.has(material.id)) return false;
        seen.add(material.id);
        return true;
      });
    },
  },

  actions: {
    // Fetch all vegetables
    async getVegetables() {
      const url = "http://127.0.0.1:8000/vegetables/";

      try {
        const response = await axios.get(url);
        this.vegetables = response.data;
        console.log(this.vegetables);
      } catch (error: any) {
        console.log(error.message);
      }
    },

    // Select a vegetable by ID and fetch its details
    async getSelectedVegetable(vegetableId: number | string) {
      const url = `http://127.0.0.1:8000/vegetables/${vegetableId}`;
      try {
        const response = await axios.get(url);
        this.selectedVegetable = response.data;
        console.log(this.selectedVegetable);
      } catch (error: any) {
        console.log(error.message);
      }
    },

    // Get a users vegetables
    async getUserVegetables(userID: number) {
      let userProgress = null;
      let userVegetableID = null;
      const userProgressURL = `http://127.0.0.1:8000/progress/${userID}`;

      try {
        const response = await axios.get(userProgressURL);
        console.log(response.data);
        userProgress = response.data;
        userVegetableID = userProgress[0].vegetable_id;
        this.usersVegetables = await this.getSelectedVegetable(userVegetableID);
      } catch (error: any) {
        console.log(error.message);
      }
      console.log(this.usersVegetables);
    },

    // Fetch all materials
    async getMaterials() {
      const url = "http://127.0.0.1:8000/materials";

      try {
        const response = await axios.get(url);
        this.materials = response.data;
        console.log(this.materials);
      } catch (error: any) {
        console.log(error.message);
      }
    },

    async filterVegetablesByUserCriteria(userCriteria: string) {
      const url = `http://127.0.0.1:8000/AItool/filter-vegetables`;
      this.filteredVegetables = [];
      this.isLoading = true;
      try {
        const response = await axios.post(url, { criteria: userCriteria });
        const results = response.data;
        console.log(typeof results);
        console.log(typeof this.vegetables);
        console.log("Isaac was here");

        results.forEach((filteredVegetable) => {
          const matchingVegetable = this.vegetables.find(
            (vege) => vege.id === filteredVegetable.id
          );
          if (matchingVegetable) {
            console.log(matchingVegetable);
            this.filteredVegetables.push(matchingVegetable);
          }
        });

        console.log(this.filteredVegetables);
      } catch (error: any) {
        console.log(error.message);
      } finally {
        this.isLoading = false;
      }
    },

    // Select a material by vegetableID and fetch its details
    async selectMaterial(materialId: number | string) {
      const url = `http://127.0.0.1:8000/materials/${materialId}`;
      try {
        const response = await axios.get(url);
        this.selectedMaterial = response.data;
        console.log(this.selectedMaterial);
      } catch (error: any) {
        console.log(error.message);
      }
    },
  },
});
