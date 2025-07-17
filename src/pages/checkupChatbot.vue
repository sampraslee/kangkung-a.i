<template>
  <div class="chat-container">
    <div class="chat-history">
      <div
        v-for="(message, index) in chatHistory"
        :key="index"
        class="message"
        :class="message.sender"
      >
        <v-img
          v-if="message.image"
          :src="message.image"
          class="message-image"
        />
        <p>{{ message.text }}</p>
      </div>
    </div>
    <div class="input-area">
      <v-textarea
        v-model="userInput"
        class="message-input"
        rows="3"
        placeholder="Type your message here..."
        variant="outlined"
        @keydown.enter.exact.prevent="sendMessage"
      ></v-textarea>
      <v-btn @click="sendMessage" color="primary">Send</v-btn>
    </div>
  </div>
</template>

<script setup lang="ts">
import axios from "axios";
import { ref, computed, onMounted } from "vue";
import { useUserStore } from "@/stores/user";

const userStore = useUserStore();
const userInput = ref("");
const chatHistory = ref([]);

const imageUrl = computed(() => {
  if (userStore.uploadedPhoto) {
    return URL.createObjectURL(userStore.uploadedPhoto);
  }
  return null;
});

async function imageAnalysis(image) {
  const url = "http://127.0.0.1:8000/AItool/image_analysis";
  const formData = new FormData();
  formData.append("file", image);
  try {
    const response = await axios.post(url, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    console.log("Analysis successful:", typeof response.data, response.data);
    return response.data;
  } catch (error) {
    if (error.response) {
      console.error("Error Response:", error.response.data);
      console.error("Error Status:", error.response.status);
    }
    return "Sorry, I couldn't analyze the image.";
  }
}

async function getGardeningAdvice(query, context) {
  const url = "http://127.0.0.1:8000/AItool/continue";
  try {
    const response = await axios.post(url, { query, context });
    return response.data;
  } catch (error) {
    console.error("Error getting gardening advice:", error);
    return "Sorry, I couldn't process your question at the moment.";
  }
}

async function sendMessage() {
  if (!userInput.value.trim()) return;
  // Add user message to chat history
  chatHistory.value.push({ sender: "user", text: userInput.value });
  // Prepare context from chat history
  const context = chatHistory.value
    .map((msg) => `${msg.sender}: ${msg.text}`)
    .join("\n");
  const response = await getGardeningAdvice(userInput.value, context); // Get response from AI
  chatHistory.value.push({ sender: "bot", text: response }); // Add AI response to chat history
  userInput.value = ""; // Clear the input
}

onMounted(async () => {
  if (userStore.uploadedPhoto) {
    // Add the uploaded image to chat history
    chatHistory.value.push({
      sender: "user",
      text: "Here is my plant:",
      image: imageUrl.value,
    });
    // Perform image analysis
    const analysis = await imageAnalysis(userStore.uploadedPhoto);
    chatHistory.value.push({ sender: "bot", text: analysis });
    // Clear the uploaded photo from the store
    userStore.uploadedPhoto = null;
  }
});
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}
.chat-history {
  flex-grow: 1;
  overflow-y: auto;
  padding: 20px;
}
.message {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 10px;
}
.user {
  background-color: #e1f5fe;
  align-self: flex-end;
}
.bot {
  background-color: #f5f5f5;
  align-self: flex-start;
}
.message-image {
  max-width: 200px;
  max-height: 200px;
  margin-bottom: 10px;
}
.input-area {
  display: flex;
  padding: 20px;
  background-color: white;
}
.message-input {
  flex-grow: 1;
  margin-right: 10px;
}
</style>
