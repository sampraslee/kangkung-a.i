/**
 * plugins/vuetify.ts
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import "@mdi/font/css/materialdesignicons.css";
import "vuetify/styles";

// Composables
import { createVuetify } from "vuetify";
import { VFileUpload } from "vuetify/labs/VFileUpload";

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
// creating our custom theme
const kangkungTheme = {
  // are we using a dark color scheme?
  dark: false,
  // what are our colors?
  colors: {
    primary: "#00A550",
    primary50: "#E6F6EE",
    primary900: "#004522",
    secondary: "#008BA3",
    white: "#FEFEFA",
    black: "#26221E",
    background: "#EFEAE4",
  },
};
export default createVuetify({
  theme: {
    defaultTheme: "kangkungTheme",
    themes: {
      kangkungTheme,
    },
  },
  components: {
    VFileUpload,
  },
});
