<template>
  <header class="header">
    <div class="logo">
      <RouterLink to="/">
        <img src="@/assets/images/canteen_spy_logo.png" alt="Canteenspy Logo" />
      </RouterLink>
    </div>
    <div class="language-button">
      <button @click="changeLanguage">
        <img src="@/assets/images/slovak_language.png" alt="Language Flag" />
      </button>
    </div>  
  </header>
</template>

<script>
export default {
  name: 'Header',
  methods: {
    changeLanguage() {

    }
  }
}
</script>
