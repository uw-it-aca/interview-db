// collections.vue

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
            <h2 class="display-3 text-center text-uppercase mb-4">Collections</h2>
            <h5 class="text-center display-4 fs-4">
              Stories with similar themes collected from diverse<br>groups of students
            </h5>
          </div>
        </div>
      </div>
      
      <!-- image on left side -->
      <div class="card w-100 border-0 rounded-0">
        <div class="row g-0">
          <div class="col-8">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png"
            class="w-100 h-100 img-fluid">
          </div>
          <div class="col-4 bg-primary justify-content-center text-white">
            <div class="card-body text-center justify-content-center">
              <h5 class="card-title my-5 display-4 fs-1">Collection Topic</h5>
              <p class="w-75 card-text mb-4 mx-auto display-4 fs-4">Some question about the collection topic</p>
              <p class="card-text mb-4 display-4 fs-4"><router-link to="/">Read Collection ></router-link></p>
            </div>
          </div>
        </div>
      </div>

      <!-- image on right side -->
      <div class="card overflow-hidden border-0 rounded-0">
        <div class="row g-0">
          <div class="col-5">
            <div class="card-body">
              <h5 class="card-title">Collection Topic</h5>
              <p class="card-text">Some question about the collection topic</p>
              <p class="card-text text-white"><router-link to="/">Read Collection ></router-link></p>
            </div>
          </div>
          <div class="col-7">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png" class="img-fluid">
          </div>
        </div>
      </div>

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
