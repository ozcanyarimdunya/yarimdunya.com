import HomeView from "@/views/HomeView.vue";
import {createRouter, createWebHistory} from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    }
  ]
})

export default router;
