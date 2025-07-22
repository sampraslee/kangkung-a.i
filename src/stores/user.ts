// stores/user.ts
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('user', () => {
  const uploadedPhoto = ref<File | null>(null)

  function newUploadedPhoto(file: File) {
    uploadedPhoto.value = file
  }

  return { uploadedPhoto, newUploadedPhoto }
})