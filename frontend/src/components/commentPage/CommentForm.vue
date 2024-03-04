<template>
    <div class="comments-form-box">
        <h3>{{ name }}</h3>
        <p>{{ price }} €</p>
        <div class="comments-box">
            <h3>Komentáre</h3>
            <div class="comments-scroll">
                <div class="comment-box" v-bind:key="comment" v-for="comment in comments">
                    <p>{{ comment.body }}</p>
                    <div class="message-flex">
                        <star-rating 
                            :rating="comment.stars"
                            :readonly="true"
                            :star-size="15"
                            active-color="#FFC700"
                            inactive-color="#FFFFFF"
                            border-color="#000000"
                            :active-on-click="true"
                            :border-width="1"
                            :show-rating="false"
                            :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]">
                        </star-rating>
                        <em>{{ comment.created_at }}</em>
                    </div>
                    <div class="arrow"></div>
                </div>
            </div>
        </div>
        <div class="stars-input">
            <star-rating 
                v-model:rating="rating"
                :star-size="40"
                active-color="#FFC700"
                inactive-color="#E3E3E3"
                border-color="#000000"
                :border-width="1"
                :padding="5"
                :show-rating="false"
                :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]">
            </star-rating>
        </div>
        <textarea v-model="comment" class="comment-input" placeholder="Napísať hodnotenie" rows="5"></textarea>
        <button v-on:click="submitComment" type="button" class="comment-submit">Odoslať</button>
    </div>
</template>

<script>
import StarRating from 'vue-star-rating'
//import axios from 'axios'

export default {
  name: 'CommentForm',
  components: {
    StarRating
  },
  props: [
    'comments',
    'name',
    'price'
  ],
  data() {
    return {
        rating: 3,
        comment: ''
    }
  },
  methods: {
    submitComment() {
        if (this.comment != "") {
            // TODO
        }
        this.rating = 3;
        this.comment = "";
    }
  }
}
</script>
