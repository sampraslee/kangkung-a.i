<<<<<<< HEAD
<template>
  <v-card class="mx-auto my-4 rounded-lg" max-width="600" elevation="2">
    <v-card-title class="d-flex justify-space-between align-center">
      <span>Kangkung A.I</span>
      <v-btn icon="mdi-menu"></v-btn>
    </v-card-title>

    <v-img
      src="../assets/garlic.png"
      alt="Garlic"
      class="rounded-circle mx-auto"
      width="150"
      height="150"
      cover
    ></v-img>

    <!-- Garlic Info -->
    <v-card-text>
      <v-sheet color="light-green-lighten-4" rounded="lg" class="pa-4 mb-4">
        <h2 class="text-h4 font-weight-bold mb-3">Garlic</h2>
        <v-list-item color="26221e">
          <template v-slot:prepend>
            <v-icon color="26221e">mdi-clock-outline</v-icon>
          </template>
          <v-list-item-title>
            Estimated time to harvest: <strong>2 - 6 weeks</strong>
          </v-list-item-title>
        </v-list-item>

        <v-list-item>
          <template v-slot:prepend>
            <v-icon color="26221e">mdi-water</v-icon>
          </template>
          <v-list-item-title>
            Water needs: <strong>Daily</strong>
          </v-list-item-title>
        </v-list-item>

        <v-list-item>
          <template v-slot:prepend>
            <v-icon color="26221e">mdi-white-balance-sunny</v-icon>
          </template>
          <v-list-item-title>
            Sunlight needs: <strong>1 - 2 hours a day</strong>
          </v-list-item-title>
        </v-list-item>
      </v-sheet>
    </v-card-text>

    <!-- How to grow -->
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-sheet rounded="lg" class="pa-4 mb-4">
            <h3 class="text-h5 font-weight-bold">How to grow:</h3>
            <v-list class="pa-0">
              <v-list-item
                v-for="(step, index) in growingSteps"
                :key="index"
                class="px-0 py-2"
                min-height="auto"
              >
                <v-list-item-content>
                  <v-list-item-title class="d-flex text-wrap">
                    <span class="min-width-25 mr-2">{{ index + 1 }}.</span>
                    <span
                      class="flex-grow-1 text-body-1"
                      style="line-height: 1.5; word-break: break-word"
                      >{{ step }}</span
                    >
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>

    <!-- What you'll need -->
    <MaterialsCard
      :materials="[
        {
          title: 'Soil',
          description: 'Describe the type of soil.',
          image: '../assets/soil.png',
        },
        {
          title: 'Fertilizer',
          description: 'Describe the type of fertilizer.',
          image: '../assets/logo.png',
        },
      ]"
    />

    <!-- Videos for you  -->
    <VideoCard
      :videos="[
        {
          title: 'Getting Started with Vue.js',
          duration: '15:30',
          summary:
            'An introductory guide to the core concepts of Vue.js, including components, reactivity, and the template syntax.',
          thumbnail: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg',
        },
        {
          title: 'Advanced Vuetify Layouts',
          duration: '25:12',
          summary:
            'Learn how to create responsive layouts using Vuetify\'s powerful grid system, layouts, and display helpers.',
          thumbnail: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg',
        },
        {
          title: 'The Future of AI',
          duration: '08:45',
          summary:
            'A discussion on the latest trends in artificial intelligence, machine learning, and their potential impact on society.',
          thumbnail: 'https://cdn.vuetifyjs.com/images/cards/docks.jpg',
        },
      ]"
    />

    <!-- Plant Button -->
    <div class="d-flex justify-center pa-2">
      <v-btn
        color="#00a550"
        size="large"
        class="text-white px-10 py-2"
        rounded="pill"
        href="https://www.google.com"
        target="_blank"
      >
        I want to plant garlic
      </v-btn>
    </div>
  </v-card>
</template>

<script>
import VideoCard from "../components/VideoCard.vue";
import MaterialsCard from "../components/MaterialsCard.vue";

export default {
  name: "VegeCard",
  components: {
    VideoCard,
    MaterialsCard,
  },
  data() {
    return {
      growingSteps: [
        "Choose a container or garden bed with good drainage.",
        "Fill with nutrient-rich, moist soil or compost.",
        "Sow seeds or plant cuttings about 1-2 inches deep.",
        "Keep the soil consistently moist, but not waterlogged.",
        "Place in an area receiving full sunlight (at least 6 hours daily).",
        "Harvest in 4-6 weeks by cutting the stems just above soil level, leaving roots intact for regrowth.",
      ],
    };
  },
};
</script>

<style>
.min-width-25 {
  min-width: 25px;
}
</style>
=======
>>>>>>> 1f52acb6a788d283ea8e3e2cc47f369fa4ead57d
