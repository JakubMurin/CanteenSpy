<template>
    <div :class="{ 'item-box-available' : isAvailable(), 'item-box-unavailable' : !isAvailable()  }">
        <div class="item-availability rotated">
            <p v-if="isAvailable()">DOSTUPNÉ</p>
            <p v-else>VYPREDANÉ</p>
        </div>
        <div class="item-info">
            <RouterLink :to="'/comments/' + canteen_id + '/' + id">
                <p v-if="meat" class="item-name">{{ name }} 🍗</p>
                <p v-else-if="vegetarian" class="item-name">{{ name }} 🌱</p>
                <div class="item-price-rating">
                    <div class="stars-box">
                        <star-rating 
                            :rating="rating"
                            :readonly="true"
                            :star-size="12"
                            active-color="#FFC700"
                            inactive-color="#FFFFFF"
                            border-color="#000000"
                            :active-on-click="true"
                            :border-width="1"
                            :show-rating="false"
                            :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]">
                        </star-rating>
                    </div>
                    <p>{{ price }}€</p>
                </div>
            </RouterLink>
            <div class="item-mark">
                <p>Je to dostupné?</p>
                <div class="item-mark-buttons">
                    <button v-show="compareDate()" class="mark-available" @click="reportAvailable()" :disabled="buttonReportMissing" >Áno</button>
                    <button v-show="compareDate()" class="mark-unavailable" @click="reportUnavailable()" :disabled="buttonReportAvailable" >Nie</button>
                </div>
            </div>
            <div class="item-voting-results">
                <p>VÝSLEDKY NAHLASOVANIA: </p>
                <div class="item-counter">
                    <div class="item-result-number">
                        <img src="@/assets/images/check-circle.svg" alt="Number available">
                        <p>{{ availableCount }}</p>
                    </div>
                    <div class="item-result-number">
                        <img src="@/assets/images/x-circle.svg" alt="Number unavailable">
                        <p>{{ unavailableCount }}</p>               
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import StarRating from 'vue-star-rating'
const Swal = require('sweetalert2')

export default {
    name: 'MenuItem',
    props: [
        'id',
        'name',
        'price',
        'rating',
        'available',
        'unavailable',
        'meat',
        'vegetarian',
        'menu_date',
        'canteen_id'
    ],
    components: {
        StarRating
    },
    methods: {
        isAvailable() {
            return this.availableCount >= this.unavailableCount;
        },
        reportAvailable(){
            Swal.fire({
                title: "Naozaj chcete označiť jedlo ako dostupné??",
                text: "Každé jedlo môžete označiť ako dostupné iba raz!",
                icon: "question",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                cancelButtonText: "Nie, neoznačovať",
                confirmButtonText: "Áno, označiť!"
                }).then((result) => {
                    if (result.isConfirmed) {
                        Swal.fire({
                        title: "Označené ako dostupné!",
                        text: "Vaše hlásenie bolo úspešne zaznamenané. Ďakujeme!",
                        icon: "success"
                        });
                        sessionStorage.setItem(this.id, true);
                        if(this.isButtonDisabled()){
                            this.buttonReportMissing = this.isButtonDisabled();
                            this.buttonReportAvailable = false;
                        }
                        axios.put('https://mupko.pythonanywhere.com/menus/available/' + this.id, {headers: {'Content-Type': 'application/json'}});
                        this.availableCount++;
                    }
                });

            return;
        },
        reportUnavailable(){
            Swal.fire({
                title: "Naozaj chcete označiť jedlo ako nedostupné??",
                text: "Každé jedlo môžete označiť ako nedostupné iba raz!",
                icon: "question",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Áno, označiť!",
                cancelButtonText: "Nie, neoznačovať",
                }).then((result) => {
                    if (result.isConfirmed) {
                        Swal.fire({
                        title: "Označené ako nedostupné!",
                        text: "Vaše hlásenie bolo úspešne zaznamenané. Ďakujeme!",
                        icon: "success"
                        });
                        if(this.isButtonDisabled()){
                            this.buttonReportMissing = false;
                            this.buttonReportAvailable = this.isButtonDisabled();
                        }
                        sessionStorage.removeItem(this.id);
                        axios.put('https://mupko.pythonanywhere.com/menus/unavailable/' + this.id , {headers: {'Content-Type': 'application/json'}});
                        this.unavailableCount++;
                    }
                });
        },
        compareDate(){
            var today = new Date();
            today.setDate(today.getDate() - 1); // yesterday
            const currentDate = this.formatDateForAPI(today);
            //const currentDate = this.formatDateForAPI(new Date());
            return this.menu_date == currentDate;
        },
        formatDateForAPI(date) {
            var dd = date.getDate();
            var mm = date.getMonth()+1; 
            var yyyy = date.getFullYear();
            if(dd<10) {
                dd='0'+dd;
            } 
            if(mm<10) {
                mm='0'+mm;
            } 
            return yyyy+'-'+mm+'-'+dd;
        },
        isButtonDisabled(){
            return sessionStorage.getItem(this.id) != null;
        }
    },
    data() {
        return {
            buttonReportMissing: this.buttonReportMissing,
            buttonReportAvailable: false,
            meatOption: this.meat,
            vegetarianOption: this.vegetarian,
            availableCount: this.available,
            unavailableCount: this.unavailable,
            foodName: this.name,
            foodPrice: this.price
        };
    },
    mounted() {
            this.buttonReportMissing = this.isButtonDisabled();
            this.buttonReportAvailable = false;
        },

}
</script>
