<template>
    <div class="menu-box">
        <div class="pagination">
            <img class="nav-arrow" src="../../assets/images/left_arrow.svg" alt="Previous Day" @click="previousDay" :disabled="currentDayIndex === 0" >

            <div class="menu-date">
                <h3>{{ this.currentDay() }}</h3>
                <p>{{ this.formatDate(currentDate) }}</p>
            </div>

            <img class="nav-arrow" src="../../assets/images/right_arrow.svg" alt="Previous Day" @click="nextDay" :disabled="currentDayIndex === days.length - 1">
        </div>
        <div class="menu-items">
                <MenuItem 
                v-for="item in this.menu" 
                v-bind:key="item.id" 
                :id="item.id" 
                :name="item.name"
                :rating="item.avg_rating"
                :price="item.price"
                :menu_date="item.day" 
                :meat="item.meat" 
                :vegetarian="item.vegetarian"
                :available="item.available" 
                :unavailable="item.unavailable"
                :canteen_id="canteen_id"
                ></MenuItem>
        </div>
    </div>

</template>

<script>
import MenuItem from './MenuItem.vue';
import axios from 'axios';

export default {
    name: 'Menu',
    components: {
        MenuItem
    },
    props: [
        'menu',
        'canteen_id'
    ],
    data() {
        return {
            days: ['Pondelok', 'Utorok', 'Streda', 'Štvrtok', 'Piatok','Sobota', 'Nedeľa'],
            currentDayIndex: new Date().getDay()-2,
            currentDate: this.getCurrentDate(),
        };
    },
    methods: {
        getMenuItemsByDay(day) {
            return this.menu[day];
        },
        previousDay() {
            if (this.currentDayIndex > 0) {
                this.currentDayIndex--;
                this.decrementDate();
                var menuAPI = 'https://mupko.pythonanywhere.com/menus/' + this.$route.params.id + '/'+ this.formatDateForAPI(this.currentDate);
                axios.get(menuAPI, {headers: {'Content-Type': 'application/json'}}).then((response) => {
                    this.$emit('update-menu', response.data);
                })
            }
        },
        nextDay() {
            if (this.currentDayIndex < this.days.length - 1) {
                this.currentDayIndex++;
                this.incrementDate();
                axios.get('https://mupko.pythonanywhere.com/menus/' + this.$route.params.id + '/' + this.formatDateForAPI(this.currentDate), {headers: {'Content-Type': 'application/json'}}).then((response) => {
                    this.$emit('update-menu', response.data);
                })
            }
        },
        getCurrentDate(){
            var today = new Date();
            today.setDate(today.getDate() - 1); // yesterday
            return today;
        },
        formatDate(date) {
            var dd = date.getDate();
            var mm = date.getMonth()+1; 
            var yyyy = date.getFullYear();
            return dd+'.'+mm+'.'+yyyy;
        },
        formatDateForAPI(date) {
            var dd = date.getDate();
            var mm = date.getMonth()+1; 
            var yyyy = date.getFullYear();
            return yyyy+'-'+mm+'-'+dd;
        },
        incrementDate() {
            this.currentDate.setDate(this.currentDate.getDate() + 1);
        },
        decrementDate() {
            this.currentDate.setDate(this.currentDate.getDate() - 1);
        },
        currentDay() {
            if (this.currentDayIndex === -1) {
                this.currentDayIndex = 6;
            }
            return this.days[this.currentDayIndex];
        }
    }
};
</script>
