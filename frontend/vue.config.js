const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'https://mupko.pythonanywhere.com',  // Replace with your Django server URL
        changeOrigin: true,
        pathRewrite: {
          '^/api': '',
        },
      },
    },
  },
})
