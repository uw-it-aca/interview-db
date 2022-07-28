import { createWebHistory, createRouter } from "vue-router";
import { trackRouter } from "vue-gtag-next";

// page components
import Home from "../pages/home.vue";
import Collections from "../pages/collections.vue";
import Topic from "../components/topic.vue";
import Students from "../pages/students.vue";
import Interview from "../components/student/interview.vue";
import About from "../pages/about.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/collections/:topic?",
    name: "Collections",
    component: Collections,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/students/:id?",
    name: "Students",
    component: Students,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/about",
    name: "About",
    component: About,
    pathToRegexpOptions: { strict: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// vue-gtag-next router tracking
trackRouter(router);

export default router;
