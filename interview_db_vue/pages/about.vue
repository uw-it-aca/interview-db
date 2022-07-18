// about.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div class="row">
        <div class="col p-5 bg-info">
          <div class="py-5">
            <h2 class="display-3 fs-2 text-center mb-4">Real Students, Real Stories</h2>
            <h5 class="text-center display-4 fs-4">
              
            </h5>
          </div>
        </div>
      </div>
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
