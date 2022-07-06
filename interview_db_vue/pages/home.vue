// home.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1>Husky Voices</h1>
    </template>

    <template #description>
      <p>Telling the stories of UW Students<br>through authentic, personal,<br>spontaneous interviews</p>
    </template>
  </layout>
</template>

<script>
import Layout from "../layout.vue";

export default {
  name: "PagesHome",
  components: {
    layout: Layout,
  },
  data() {
    return {
      pageTitle: "Home",
    };
  },
  methods: {},
};
</script>
