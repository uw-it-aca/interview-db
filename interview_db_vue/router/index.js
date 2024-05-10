import { createWebHistory, createRouter } from "vue-router";
import { trackRouter } from "vue-gtag-next";

// page components
import Home from "../pages/home.vue";
import Collections from "../pages/collections.vue";
import Students from "../pages/students.vue";
import About from "../pages/about.vue";
import LayoutMobile from "../mobilelayout.vue";
import StudentFilter from "../components/student-filter.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    props: true,
    component: Home,
  },
  {
    path: "/collections/:id?/",
    name: "Collections",
    component: Collections,
    props: true,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/students/:id?/",
    name: "Students",
    component: Students,
    props: true,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/about",
    name: "About",
    component: About,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/menu",
    name: "Menu",
    component: LayoutMobile,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/filters/:id?",
    name: "Filters",
    component: StudentFilter,
    pathToRegexpOptions: { strict: true },
  },
];

const router = createRouter({
  scrollBehavior(to, from, savedPosition) {
    if (to.name != from.name || to.query.page != from.query.page) {
      return { top: 0 }
    }
    if (savedPosition) {
      return savedPosition
    }
  },
  history: createWebHistory(),
  routes,
});

// vue-gtag-next router tracking
trackRouter(router);

export default router;
