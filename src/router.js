import HomeView from "@/views/HomeView.vue";
import {createRouter, createWebHashHistory} from "vue-router";

const router = createRouter({
  history: createWebHashHistory(),
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
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import("@/views/NotFoundView.vue"),
    }
  ]
})

export default router;
