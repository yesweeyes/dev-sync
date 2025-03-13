/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}", // Scan all files inside src/
    "./src/components/**/*.{js,jsx,ts,tsx}", // Ensure component files are included
    "./src/screens/**/*.{js,jsx,ts,tsx}", // Ensure screen files are included
  ],
  presets: [require("nativewind/preset")],
  darkMode: "class", // Enable dark mode support
  theme: {
    extend: {},
  },
  plugins: [],
};
