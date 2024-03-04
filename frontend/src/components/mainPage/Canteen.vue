<template>
    <div class="canteen-box" v-bind:style="{ backgroundImage: 'linear-gradient(rgba(255, 255, 255, 0), rgba(0, 0, 0, 1)),  url(' + require('@/assets/images/' + image) + ')' }">
      <div class="stars-box">
        <star-rating 
            :rating="stars"
            :readonly="true"
            :star-size="15"
            :active-on-click="true"
            active-color="#FFC700"
            :show-rating="false"
            :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]">
        </star-rating>
      </div>
      <h2>{{ name }}</h2>
      <p>{{ address }}</p>
      <div class="flex-box">
        <p>Otvorené do {{ open_until }}</p>
        <p>Menu od {{ menu_price }} €</p>
      </div>
    </div>
</template>

<script>
import StarRating from 'vue-star-rating'

export default {
  name: 'Canteen',
  components: {
    StarRating
  },
  props: [
    'canteen_id',
    'name',
    'stars',
    'open_until',
    'menu_price',
    'image',
    'address'
  ]
}
</script>