// about.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1>{{ pageTitle }}</h1>
    </template>

    <template #description>
      <p></p>
    </template>

    <template #content>
    </template>
  </layout>
</template>

<script>
import { Card } from "axdd-components";
import Layout from "../layout.vue";

export default {
  name: "PagesAbout",
  components: {
    layout: Layout,
    "axdd-card": Card,
  },
  data() {
    return {
      pageTitle: "About Us",
    };
  },
  methods: {},
};
</script>
