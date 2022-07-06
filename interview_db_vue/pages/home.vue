// home.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1>Husky Voices</h1>
    </template>
  </layout>
</template>

<script>
import Layout from "../layout.vue";
import HelloWorld from "../components/hello-world.vue";

export default {
  name: "PagesHome",
  components: {
    layout: Layout,
    "some-component": HelloWorld,
  },
  data() {
    return {
      pageTitle: "Home",
    };
  },
  methods: {},
};
</script>
