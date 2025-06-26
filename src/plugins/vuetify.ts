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

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
// creating our custom theme
const kangkungTheme = {
  // are we using a dark color scheme?
  dark: false,
  // what are our colors?
  colors: {
    primary: "#00A550",
    secondary: "#008BA3",
    accent: "#E6F6E7",
    white: "#FFFFF",
    black: "#26221E",
  },
};
export default createVuetify({
  theme: {
    defaultTheme: "kangkungTheme",
    themes: {
      kangkungTheme,
    },
  },
});
