import { createApp } from "vue";
import App from "./app.vue";
import router from "./router";
//import store from "./store";

import VueGtag from "vue-gtag-next";
import { Vue3Mq, MqResponsive } from "vue3-mq";
import VueAwesomePaginate from "vue-awesome-paginate";

// bootstrap js
import "bootstrap";

// custom bootstrap theming
import "./css/custom.scss";
import "vue-awesome-paginate/dist/style.css";

const app = createApp(App);

// MARK: google analytics data stream measurement_id
const gaCode = document.body.getAttribute("data-google-analytics");
const debugMode = document.body.getAttribute("data-django-debug");

app.config.productionTip = false;

// vue-gtag-next
app.use(VueGtag, {
  isEnabled: debugMode == "false",
  property: {
    id: gaCode,
    params: {
      anonymize_ip: true,
    },
  },
});

// vue-mq (media queries)
app.use(Vue3Mq, {
  breakpoints: {
    mobile: 0,
    tablet: 576,
    desktop: 992,
  }
});
app.component("mq-responsive", MqResponsive);

app.use(router);
//app.use(store);
app.use(VueAwesomePaginate);

app.mount("#app");

