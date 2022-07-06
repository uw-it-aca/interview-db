// students.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1>{{ pageTitle }}</h1>
    </template>

    <template #description>
      <p>Sort interviews by student<br>characteristics</p>
    </template>

    <template #content>
      <p class="p-0 col-md-8 lead">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eget
        pulvinar est. Sed gravida neque justo, pellentesque finibus velit
        scelerisque eu. Curabitur et dolor luctus, convallis magna at, mollis
        purus. Nunc tincidunt risus quis nisl bibendum volutpat. Praesent ut
        tincidunt ex.
      </p>
    </template>
  </layout>
</template>

<script>
import { Card } from "axdd-components";
import Layout from "../layout.vue";

export default {
  name: "PagesStudents",
  components: {
    layout: Layout,
    "axdd-card": Card,
  },
  data() {
    return {
      pageTitle: "Students",
    };
  },
  methods: {},
};
</script>
