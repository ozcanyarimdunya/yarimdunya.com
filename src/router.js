import HomeView from "@/views/HomeView.vue";
import {createRouter, createWebHistory} from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/blog",
      name: "blog",
      component: () => import("@/views/BlogView.vue"),
    },
    {
      path: "/blog/:slug",
      name: "blog-detail",
      component: () => import("@/views/BlogDetailView.vue"),
    }
  ]
})

export default router;
