// home.vue

<template>
  <layout>
    <!-- page content -->

    <template #content>
      <p>Hello World</p>
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
    "nancy-hello": HelloWorld,
  },
  data() {
    return {
      pageTitle: "Getting started",
    };
  },
  methods: {},
};
</script>
