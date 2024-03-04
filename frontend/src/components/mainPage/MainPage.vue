<template>
  <Filter></Filter>

  <div class="canteens-box">
      <router-link :to="'/detail/' + canteen.id" v-bind:key="canteen" v-for="canteen in canteens" class="canteen-href">
          <Canteen 
            :canteen_id="canteen.id" 
            :name="canteen.name" 
            :stars="canteen.avg_rating"
            :open_until="canteen.closing"
            :menu_price="canteen.low_price"
            :image="canteen.image"
            :address="canteen.location"
          ></Canteen>
      </router-link>
  </div>

</template>

<script>
import Filter from './Filter.vue'
import Canteen from './Canteen.vue'
import axios from 'axios'

export default {
  name: 'MainPage',
  components: {
    Filter,
    Canteen
  },
  data() {
    return {
      canteens: {}
    }
  },
  methods: {
    getCanteens() {
      //axios.get('http://127.0.0.1:8000/canteens/', {headers: {'Content-Type': 'application/json'}}).then((response) => {
      axios.get('https://mupko.pythonanywhere.com/canteens/', {headers: {'Content-Type': 'application/json'}}).then((response) => {
        this.canteens = response.data.canteens;
      });
    },
  },
  mounted() {
    this.getCanteens()
  }
}
</script>
