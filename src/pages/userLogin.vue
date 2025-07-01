<template>
  <v-container
    fluid
    fill-height
    class="d-flex align-center justify-center bg-grey-lighten-4"
  >
    <v-card class="elevation-12 pa-8 rounded-lg" max-width="450px" width="100%">
      <v-card-title class="text-h5 font-weight-bold text-center mb-4">
        Welcome To Kangkung A.I
      </v-card-title>
      <v-card-subtitle class="text-center mb-6">
        Sign in to manage your plants.
      </v-card-subtitle>

      <v-card-text>
        <v-form @submit.prevent="handleLogin">
          <v-text-field
            v-model="email"
            label="Email"
            prepend-inner-icon="mdi-email"
            variant="outlined"
            density="compact"
            class="mb-4"
            :rules="[rules.required, rules.email]"
            clearable
          ></v-text-field>

          <v-text-field
            v-model="password"
            label="Password"
            prepend-inner-icon="mdi-lock"
            :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            :type="showPassword ? 'text' : 'password'"
            variant="outlined"
            density="compact"
            @click:append-inner="showPassword = !showPassword"
            :rules="[rules.required]"
            clearable
          ></v-text-field>

          <v-btn
            type="submit"
            color="green-darken-2"
            block
            class="mt-6 text-h6 font-weight-bold"
            size="large"
            :loading="loading"
          >
            Login
          </v-btn>
        </v-form>
      </v-card-text>

      <v-card-actions class="d-flex justify-center mt-4">
        <router-link
          to="/register"
          class="text-green-darken-2 font-weight-medium text-decoration-none"
        >
          Don't have an account? Register now.
        </router-link>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from "vue";
const router = useRouter();

// Reactive variables for form inputs
const email = ref("");
const password = ref("");
const showPassword = ref(false); // To toggle password visibility
const loading = ref(false); // For showing loading state on the button

// Basic validation rules (you can expand these)
const rules = {
  required: (value: string) => !!value || "Required.",
  email: (value: string) => {
    const pattern =
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return pattern.test(value) || "Invalid e-mail.";
  },
};

// Placeholder for login logic (will be implemented later)
const handleLogin = () => {
  // Simulate API call or validation
  loading.value = true;
  console.log("Attempting login with:", email.value, password.value);

  // In a real app, you'd send this data to your backend
  setTimeout(() => {
    loading.value = false;
    router.push("/vegetableSelect");
    // Based on backend response:
    // If successful: router.push('/dashboard');
    // If failed: show error message;
  }, 1500);
};
</script>

<style scoped>
/* You can add custom styles here if needed, but Vuetify classes are quite sufficient */
/* For example, to make the card appear floating */
.elevation-12 {
  box-shadow: 0px 7px 8px -4px var(--v-shadow-key-umbra-opacity, rgba(0, 0, 0, 0.2)),
    0px 12px 17px 2px var(--v-shadow-key-penumbra-opacity, rgba(0, 0, 0, 0.14)),
    0px 5px 22px 4px var(--v-shadow-key-ambient-opacity, rgba(0, 0, 0, 0.12));
}

.bg-grey-lighten-4 {
  background-color: #f5f5f5 !important; /* A light grey background for the whole page */
}
</style>
