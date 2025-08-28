/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',
    '../../templates/**/*.html',
    '../../../templates/**/*.html',
    './src/**/*.{js,jsx,ts,tsx,vue}',
  ],
  theme: {
    extend: {
      spacing: {
        '17': '4.25rem', // You can also add it to the spacing scale
      },
      height: {
        '17': '4.25rem', // This creates the h-17 class
      },
    },
  },
  plugins: [],
};