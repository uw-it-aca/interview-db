// home.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1><i class="bi-alarm"></i> Husky Voices</h1>
    </template>

    <template #description>
      <p class="bg-foo p-3 text-white rounded bg-bar-hover text-warning-hover shadow-sm">Telling the stories of UW Students<br>through authentic, personal,<br>spontaneous interviews</p>
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
