import { defineConfig } from "vite";

// vite.config.js
export default defineConfig({
  root: "frontend",
  build: {
    // generate manifest.json in outDir
    manifest: true,
    rollupOptions: {
      // overwrite default .html entry
      input: ["frontend/main.js", "frontend/styles.scss"],
    },
  },
});
