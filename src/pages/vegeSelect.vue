<script setup lang="ts">
import ProductVege from "@/components/vegeProduct.vue";
import { ref, onMounted } from "vue";

// Define your backend base URL here
const BACKEND_BASE_URL = "http://127.0.0.1:8000"; // Or "http://localhost:8000"

// Interface (make sure this matches your component's needs and the backend's data after mapping)
interface ProcessedVegetable {
  id: number;
  ProductName: string;
  HarvestTime: string | null;
  SunNeeds: string | null;
  WaterNeeds: string | null;
  ImageUrl: string | null; // This will now hold the ABSOLUTE URL
}

const vegetablesData = ref<ProcessedVegetable[]>([
  {
    id: 1,
    ProductName: "Kangkung (Water Spinach)",
    HarvestTime: "4-6 weeks",
    SunNeeds: "4–6 hours/day",
    WaterNeeds: "Keep soil moist",
    ImageUrl: "https://via.placeholder.com/300x150/C8E6C9/212121?text=Kangkung", // Placeholder image
  },
  {
    id: 2,
    ProductName: "Bayam (Local Spinach)",
    HarvestTime: "4-5 weeks",
    SunNeeds: "4–5 hours/day",
    WaterNeeds: "Avoid waterlogging",
    ImageUrl: "https://via.placeholder.com/300x150/A5D6A7/212121?text=Bayam", // Placeholder image
  },
  {
    id: 3,
    ProductName: "Cili (Chili Peppers)",
    HarvestTime: "2-3 months",
    SunNeeds: "6–8 hours/day",
    WaterNeeds: "Regular",
    ImageUrl: "https://via.placeholder.com/300x150/81C784/212121?text=Cili", // Placeholder image
  },
]);

// Helper function to convert relative URL to absolute URL
/*
const getAbsoluteImageUrl = (relativePath: string | null): string | null => {
  if (relativePath && relativePath.startsWith("/static/")) {
    return `${BACKEND_BASE_URL}${relativePath}`;
  }
  return relativePath; // Return as is if it's already an absolute URL or not a static path
};*/
/*
const fetchVegetables = async () => {
  try {
    console.log("1. fetchVegetables started.");
    const response = await fetch(`${BACKEND_BASE_URL}/api/v1/plants/`); // Use BACKEND_BASE_URL here too for consistency

    console.log("2. Response received:", response);

    if (!response.ok) {
      const errorData = await response.json();
      console.error("3. HTTP error during fetch:", response.status, errorData);
      throw new Error(
        `HTTP error! status: ${response.status}, Detail: ${JSON.stringify(
          errorData
        )}`
      );
    }

    const data = await response.json();
    console.log("4. Raw JSON data:", data);

    // Ensure 'data' is an array before mapping
    if (Array.isArray(data)) {
      vegetablesData.value = data.map(
        (plant: any): ProcessedVegetable => ({
          id: plant.id,
          ProductName: plant.name,
          HarvestTime: plant.time_to_harvest,
          SunNeeds: plant.sunlight_requirements,
          WaterNeeds: plant.watering_requirements,
          // --- THE KEY CHANGE IS HERE: Call getAbsoluteImageUrl ---
          ImageUrl: getAbsoluteImageUrl(plant.image_url),
        })
      );
      console.log(
        "5. vegetablesData after mapping (with absolute URLs):",
        vegetablesData.value
      );
      console.log("6. Final length:", vegetablesData.value.length);
    } else {
      console.error("7. Fetched data is not an array:", data);
      vegetablesData.value = [];
    }
  } catch (error) {
    console.error("8. Error fetching vegetables:", error);
  }
};*/

onMounted(() => {
  console.log("0. Component mounted, calling fetchVegetables.");
  //fetchVegetables();
});
</script>

<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="text-h5 font-weight-bold">
        Kangkung A.I
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <v-container fluid class="pa-0">
        <v-row justify="center" class="my-6">
          <v-col cols="12" class="text-center">
            <h1>Hi Aina, what would you like to grow?</h1>
          </v-col>
        </v-row>

        <v-row justify="center" v-if="vegetablesData.length === 0">
          <v-col cols="12" class="text-center">
            <p>Loading vegetables...</p>
            <v-progress-circular
              indeterminate
              color="primary"
              size="64"
              width="6"
            ></v-progress-circular>
          </v-col>
        </v-row>

        <v-row justify="center">
          <v-col
            v-for="vegetable in vegetablesData"
            :key="vegetable.id"
            cols="12"
            sm="6"
            md="4"
            lg="3"
          >
            <ProductVege
              :ProductName="vegetable.ProductName"
              :HarvestTime="vegetable.HarvestTime"
              :SunNeeds="vegetable.SunNeeds"
              :WaterNeeds="vegetable.WaterNeeds"
              :ImageUrl="vegetable.ImageUrl"
            />
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped></style>
