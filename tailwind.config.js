/** @type {import("tailwindcss").Config} */
module.exports = {
  content: ["./website/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/aspect-ratio"),
  ],
}