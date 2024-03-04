<template>
  <div class="opening-hours-box">
    <div class="opening-hours-dropdown" @click="toggleOpeningHours">
      <h3>Otváracie hodiny</h3>
      <img v-if="!isOpen" src="@/assets/images/caret-down-fill.svg" alt="Opening Hours Detail Show">
      <img v-else src="@/assets/images/caret-up-fill.svg" alt="Opening Hours Detail Hide">
    </div>
    <div id="opening-hours-content">
      <div class="opening-hours-day-detail" v-for="(day, index) in days" :key="day">
        <p>{{ day }}</p>
        <p>{{ openingHours[index] }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: [
    'openingHours'
  ],
  data() {
    return {
      isOpen: true,
      days: ['Pondelok', 'Utorok', 'Streda', 'Štvrtok', 'Piatok', 'Sobota', 'Nedeľa'],
    }
  },
  methods: {
    toggleOpeningHours() {
      if(this.isOpen) {
        this.isOpen = false;
        document.getElementById('opening-hours-content').style.display = "none";
      }else{
        this.isOpen = true;
        document.getElementById('opening-hours-content').style.display = "block";
      }
    },
    getOpeningHours(day) {
      return this.openingHours[day];
    }
  },
  mounted() {
    if(document.getElementById('opening-hours-content').style.display == "block") {
      this.isOpen = true;
    }else{
      this.isOpen = false;
    }
  }
};
</script>