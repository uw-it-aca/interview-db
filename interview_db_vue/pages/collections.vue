// collections.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div class="row">
        <div class="col p-5 mb-4 bg-info">
          <div class="py-5">
            <h2 class="display-5 fw-bold text-center">Collections</h2>
            <h5 class="text-center">
              Collections of stories collected from diverse<br>groups of students
            </h5>
          </div>
        </div>
      </div>
      
      <!-- image on left side -->
      <div class="card">
        <div class="row g-0">
          <div class="col-md-5">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png" class="img-fluid">
          </div>
          <div class="col-md-7">
            <div class="card-body">
              <h5 class="card-title">Collection Topic</h5>
              <p class="card-text">Some question about the collection topic</p>
              <p class="card-text"><router-link to="/">Read full collection ></router-link></p>
            </div>
          </div>
        </div>
      </div>

      <!-- image on right side -->
      <div class="card">
        <div class="row g-0">
          <div class="col-md-7">
            <div class="card-body">
              <h5 class="card-title">Collection Topic</h5>
              <p class="card-text">Some question about the collection topic</p>
              <p class="card-text"><router-link to="/">Read full collection ></router-link></p>
            </div>
          </div>
          <div class="col-md-5">
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
