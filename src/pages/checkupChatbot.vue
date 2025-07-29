<!-- checkupChatbot.vue -->
<template>
  <div class="chat-container">
    <v-btn @click="exitChatAndSummarize" color="error" class="exit-button">
      Exit Chat
    </v-btn>
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
        <p class="message-text" v-html="renderMarkdown(message.text)"></p>
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
import { marked } from "marked";

const chatHistory = ref<any[]>([]);
const router = useRouter();
const route = useRoute();
const userStore = useUserStore();
const userInput = ref("");
const progressId = "2";
const imageUrl = computed(() => {
  if (userStore.uploadedPhoto) {
    return URL.createObjectURL(userStore.uploadedPhoto);
  }
  return null;
});

async function imageAnalysis(image) {
  const url = "http://127.0.0.1:8000/AItool/analyze-image-chat/2";
  const formData = new FormData();
  formData.append("file", image);
  try {
    const response = await axios.post(url, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    console.log("Analysis successful:", typeof response.data, response.data);
    return response.data.analysis;
  } catch (error) {
    if (error.response) {
      console.error("Error Response:", error.response.data);
      console.error("Error Status:", error.response.status);
    }
    return "Sorry, I couldn't analyze the image.";
  }
}

async function getGardeningAdvice(query, context) {
  const url = `http://127.0.0.1:8000/AItool/continue-chat/${progressId}`;
  console.log(query);
  try {
    const response = await axios.post(
      url,
      {
        session_id: "2",
        user_input: query,
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    const responseData = response.data.ai_response;
    return responseData;
  } catch (error) {
    console.error("Error sending message:", error);
    return error;
  }
}

async function sendMessage() {
  if (!userInput.value.trim()) return;
  const userMessage = userInput.value;
  chatHistory.value.push({ sender: "user", text: userMessage });
  userInput.value = "";
  const context = chatHistory.value
    .map((msg) => `${msg.sender}: ${msg.text}`)
    .join("\n");
  const response = await getGardeningAdvice(userMessage, context);
  chatHistory.value.push({ sender: "bot", text: response });
}
const renderMarkdown = (markdownText: string) => {
  return marked.parse(markdownText, { breaks: true });
};

onMounted(async () => {
  if (userStore.uploadedPhoto) {
    chatHistory.value.push({
      sender: "user",
      text: "Here is my plant:",
      image: imageUrl.value,
    });
    const analysis = await imageAnalysis(userStore.uploadedPhoto);
    chatHistory.value.push({ sender: "bot", text: analysis });
    userStore.uploadedPhoto = null;
  }
});

async function exitChatAndSummarize() {
  if (!progressId) {
    console.error("Progress ID is not available. Cannot summarize chat.");
    alert("Error: Cannot summarize chat. Progress ID missing.");
    router.push("/vegetableSelect");
    return;
  }

  try {
    const summarizeUrl = `http://127.0.0.1:8000/AItool/summarize-chat/${progressId}`;
    const response = await axios.post(summarizeUrl);
    console.log("Chat summarized successfully:", response.data);
  } catch (error: any) {
    console.error(
      "Error summarizing chat:",
      error.response?.data || error.message
    );
  } finally {
    router.push("/vegetableSelect");
  }
}
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  max-width: 800px;
  margin: 0 auto;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  position: relative;
}

.exit-button {
  position: absolute;
  top: 20px;
  right: 50px;
  z-index: 10;
}
.message-text {
  max-width: 70%;
  padding: 10px 15px;
  border-radius: 20px;
  line-height: 1.5;
  word-wrap: break-word;
  white-space: pre-wrap;
}
.chat-history {
  flex-grow: 1;
  overflow-y: auto;
  padding: 20px;
  max-height: 100%;
}
.message {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 10px;
}
.user {
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
}
.message-input {
  flex-grow: 1;
  margin-right: 10px;
}
</style>
