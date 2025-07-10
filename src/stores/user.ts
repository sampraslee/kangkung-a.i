import axios from "axios"; //for api
import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => ({
    uploadedPhoto: null,
    user: null,
  }),

  actions: {
    newUploadedPhoto(photo: File) {
      this.uploadedPhoto = photo;
    },
  },
});