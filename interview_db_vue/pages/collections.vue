// collections.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1>{{ pageTitle }}</h1>
    </template>

    <template #description>
      <p>Collections of stories collected from diverse<br>groups of students</p>
    </template>

    <template #content>
      <axdd-card>
        <template #heading>
        <axdd-card-heading :level="2">Collection Topic</axdd-card-heading>
        </template>
        <template #body>
          <p>How did you find your major<br>and why did you choose it?</p>
        </template>
        <template #footer>
          <p>Read Collection</p>
        </template>
      </axdd-card>
    </template>
  </layout>
</template>

<script>
import { Card, CardHeading, CardAction } from "axdd-components";
import Layout from "../layout.vue";

export default {
  name: "PagesCollections",
  components: {
    layout: Layout,
    "axdd-card": Card,
    "axdd-card-heading": CardHeading,
    "axdd-card-action": CardAction,
  },
  data() {
    return {
      pageTitle: "Collections",
    };
  },
  methods: {},
};
</script>
