import { fileURLToPath, URL } from "url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({

  // MARK: start vite build config
  build: {
    manifest: true,
    rollupOptions: {
      input: [
        // MARK: list all entry points
        './interview_db_vue/main.js',
      ]
    },
    outDir: './interview_db/static/', // NOTE: '/static/'
    assetsDir: 'interview_db/assets', // NOTE: '/static/app_name/assets/xxxx.js'
    emptyOutDir: false,
  },
  base: "/static/", // MARK: allows for proper css url path creation
  // root: "./app_name_vue",

  // MARK: standard vite/vue plugin and resolver
  plugins: [vue(),],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./interview_db_vue", import.meta.url)),
    },
  },
});
