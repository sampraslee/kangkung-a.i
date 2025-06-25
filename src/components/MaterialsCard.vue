<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-sheet rounded="lg" class="pa-4 mb-4">
          <h3 class="text-h5 font-weight-bold mb-4">{{ title }}</h3>

          <div class="materials-list">
            <v-card
              v-for="(item, index) in materials"
              :key="index"
              max-width="600"
              variant="outlined"
              class="material-item"
              :class="{ 'mb-3': index !== materials.length - 1 }"
            >
              <div class="d-flex align-start pa-4">
                <v-img
                  :src="item.image"
                  :alt="item.title"
                  width="100"
                  height="100"
                  class="rounded flex-shrink-0"
                  cover
                >
                  <template v-slot:placeholder>
                    <div class="d-flex align-center justify-center fill-height">
                      <v-icon
                        color="grey-darken-1"
                        icon="mdi-image"
                        size="large"
                      ></v-icon>
                    </div>
                  </template>
                </v-img>
                <div class="ml-4 text-left">
                  <div class="text-h6 font-weight-bold mb-1">
                    {{ item.title }}
                  </div>
                  <div class="text-body-1">{{ item.description }}</div>
                </div>
              </div>
            </v-card>
          </div>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "MaterialsCard",
  props: {
    title: {
      type: String,
      default: "What you'll need:",
    },
    materials: {
      type: Array,
      required: true,
      validator: (value) => {
        return value.every(
          (item) =>
            typeof item.title === "string" &&
            typeof item.description === "string" &&
            typeof item.image === "string"
        );
      },
    },
  },
};
</script>

<style scoped>
.materials-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.material-item {
  border-radius: 8px;
  transition: all 0.2s ease;
  width: 100%;
}

.material-item:hover {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.text-left {
  text-align: left;
  width: 100%;
}
</style>
