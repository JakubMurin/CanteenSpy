<template>
    <div class="header2" v-bind:style="{ backgroundImage: 'linear-gradient(rgba(255, 255, 255, 0), rgba(0, 0, 0, 1)),  url(' + require('@/assets/images/' + canteen_image) + ')' }">
      <router-link :to="'/detail/' + this.$route.params.canteen_id" class="back-button"><img src="@/assets/images/arrow-left.png" alt="back"></router-link>
      <h1>{{ canteen_name }}</h1>
    </div>
    <div class="flex-comments">
      <CommentForm
        :comments="comments"
        :name="name"
        :price="price"
      ></CommentForm>
      <Alergens></Alergens>
    </div>
</template>

<script>
import Alergens from './Alergens.vue'
import CommentForm from './CommentForm.vue'
import moment from 'moment'
import axios from 'axios'

export default {
  name: 'CommentPage',
  components: {
    Alergens,
    CommentForm
  },
  data() {
    return {
      comments: {},
      name: '',
      price: '',
      canteen_name: '',
      canteen_image: 'no_photo.png'
    }
  },
  methods: {
    getComments() {
        axios.get('https://mupko.pythonanywhere.com/ratings/' + this.$route.params.menu_id, {headers: {'Content-Type': 'application/json'}}).then((response) => {
        this.comments = response.data;
        this.comments.forEach(el => {
            el.created_at = moment(String(el.created_at)).format('DD.MM.YYYY HH:mm')
        });
      });
    },
    getMenuDetail() {
      axios.get('https://mupko.pythonanywhere.com/menus/' + this.$route.params.menu_id, {headers: {'Content-Type': 'application/json'}}).then((response) => {
        this.name = response.data.name;
        this.price = response.data.price;
      });
    },
    getCanteenDetail() {
      axios.get('https://mupko.pythonanywhere.com/canteens/' + this.$route.params.canteen_id, {headers: {'Content-Type': 'application/json'}}).then((response) => {
        console.log(response);
        this.canteen_name = response.data.name;
        this.canteen_image = response.data.image;
        console.log(this.canteen_image);
      });
    }
  },
  mounted() {
    this.getComments()
    this.getMenuDetail()
    this.getCanteenDetail()
  }
}
</script>
