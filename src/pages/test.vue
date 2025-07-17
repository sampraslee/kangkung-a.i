<template>
  <div class="chat-container">
    <div class="chat-history" ref="chatHistoryContainer">
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
          max-height="200"
        />
        <div v-if="message.text" class="message-bubble">
          <MarkdownRenderer
            v-if="message.sender === 'ai'"
            :content="message.text"
          />
          <p v-else>{{ message.text }}</p>
        </div>
      </div>
    </div>

    <div class="input-area">
      <v-file-input
        v-if="!sessionId"
        label="Upload a plant photo to start..."
        variant="outlined"
        accept="image/*"
        :loading="isLoading"
        :disabled="isLoading"
        @change="handleFileUpload"
      ></v-file-input>

      <v-textarea
        v-if="sessionId"
        v-model="userInput"
        class="message-input"
        rows="2"
        placeholder="Ask a follow-up question..."
        variant="outlined"
        :loading="isLoading"
        :disabled="isLoading"
        @keydown.enter.exact.prevent="sendMessage"
      ></v-textarea>

      <v-btn
        v-if="sessionId"
        @click="sendMessage"
        color="primary"
        :disabled="isLoading || !userInput.trim()"
        >Send</v-btn
      >
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, nextTick } from "vue";
import MarkdownRenderer from "../components/MarkdownRenderer.vue"; // --- 1. IMPORT THE COMPONENT ---

// --- PROPS ---
// The component needs the progress ID to make API calls
const props = defineProps<{
  progressId: number;
}>();
// --- TYPES ---
interface ChatMessage {
  sender: "user" | "ai";
  text?: string;
  image?: string; // To display a preview of the uploaded image
}

// --- STATE MANAGEMENT ---
const chatHistory = ref<ChatMessage[]>([
  {
    sender: "ai",
    text: "Hello! 👋 Please upload a photo of your plant so I can analyze it for you.",
  },
]);
const userInput = ref("");
const isLoading = ref(false);
const sessionId = ref<string | null>(null); // This will store the session ID from the first API call

// For auto-scrolling
const chatHistoryContainer = ref<HTMLElement | null>(null);

// --- METHODS ---

const scrollToBottom = async () => {
  await nextTick(); // Wait for the DOM to update
  if (chatHistoryContainer.value) {
    chatHistoryContainer.value.scrollTop =
      chatHistoryContainer.value.scrollHeight;
  }
};

// Function to handle the initial image upload
const handleFileUpload = async (event: Event) => {
  const target = event.target as HTMLInputElement;
  const file = target.files?.[0];

  if (!file) return;

  isLoading.value = true;
  const imagePreviewUrl = URL.createObjectURL(file);
  chatHistory.value.push({
    sender: "user",
    image: imagePreviewUrl,
    text: "Here's my plant.",
  });
  //scrollToBottom();

  const formData = new FormData();
  formData.append("file", file);

  try {
    // --- THIS URL HAS BEEN CORRECTED ---
    const response = await fetch(
      `http://127.0.0.1:8000/AItool/analyze-image-chat/2`,
      {
        method: "POST",
        body: formData,
      }
    );

    if (!response.ok) {
      throw new Error("Failed to analyze image.");
    }

    const data = await response.json();
    sessionId.value = data.session_id;
    console.log(sessionId.value);
    chatHistory.value.push({ sender: "ai", text: data.analysis });
  } catch (error) {
    console.error(error);
    chatHistory.value.push({
      sender: "ai",
      text: "Sorry, I couldn't analyze the image. Please try again.",
    });
  } finally {
    isLoading.value = false;
    //scrollToBottom();
  }
};

// Function to handle follow-up text messages
const sendMessage = async () => {
  if (!userInput.value.trim() || isLoading.value || !sessionId.value) return;

  const messageText = userInput.value;
  isLoading.value = true;
  chatHistory.value.push({ sender: "user", text: messageText });
  userInput.value = "";
  //scrollToBottom();

  try {
    // --- THIS URL HAS BEEN CORRECTED ---
    const response = await fetch(
      `http://127.0.0.1:8000/AItool/continue-chat/2`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          session_id: sessionId.value,
          user_input: messageText,
        }),
      }
    );

    if (!response.ok) {
      throw new Error("Failed to get a response.");
    }

    const data = await response.json();
    console.log(sessionId.value);
    chatHistory.value.push({ sender: "ai", text: data.ai_response });
  } catch (error) {
    console.error(error);
    chatHistory.value.push({
      sender: "ai",
      text: "Sorry, something went wrong. Please try again.",
    });
  } finally {
    isLoading.value = false;
    //scrollToBottom();
  }
};
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 80vh;
  max-width: 800px;
  margin: auto;
  border: 1px solid #ccc;
  border-radius: 8px;
  overflow: hidden;
}

.chat-history {
  flex-grow: 1;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.message {
  display: flex;
  flex-direction: column;
  max-width: 80%;
}

.message.user {
  align-self: flex-end;
  align-items: flex-end;
}

.message.ai {
  align-self: flex-start;
  align-items: flex-start;
}

.message-bubble {
  padding: 10px 16px;
  border-radius: 18px;
  word-wrap: break-word;
  white-space: pre-wrap; /* This preserves line breaks from the AI */
}

.message.user .message-bubble {
  background-color: #4caf50; /* A nice green for user messages */
  color: white;
}

.message.ai .message-bubble {
  background-color: #f1f1f1;
  color: black;
}

.message-image {
  border-radius: 12px;
  margin-bottom: 4px;
  max-width: 100%;
}

.input-area {
  display: flex;
  align-items: center;
  padding: 16px;
  border-top: 1px solid #ccc;
}
</style>
