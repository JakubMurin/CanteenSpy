import { createRouter, createWebHistory } from "vue-router";
import MainPage from '../components/mainPage/MainPage.vue';
import DetailPage from '../components/detailPage/DetailPage.vue';
import CommentPage from '../components/commentPage/CommentPage.vue';

const router = createRouter({
    mode: 'History',
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'Home',
            component: MainPage
        },
        {
            path: '/detail/:id',
            name: 'Detail',
            component: DetailPage
        },
        {
            path: '/comments/:canteen_id/:menu_id',
            name: 'Comments',
            component: CommentPage
        }
    ]
});

export default router
