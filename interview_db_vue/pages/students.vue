// students.vue

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
            <h2 class="display-5 fw-bold text-center">Student Interviews</h2>
            <h5 class="text-center">
              Sort interviews by student<br>characteristics
            </h5>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="row justify-content-end"><StudentListing :first-name="'Amanda'"/></div>
        <div class="row justify-content-end"><StudentListing :first-name="'Anna'"/></div>
        <div class="row justify-content-end"><StudentListing :first-name="'Caleb'"/></div>
      </div>
    </template>
  </layout>
</template>

<script>
import { Card } from "axdd-components";
import Layout from "../layout.vue";
import StudentListing from "../components/student-listing.vue"

export default {
  name: "PagesStudents",
  components: {
    layout: Layout,
    "axdd-card": Card,
    StudentListing,
  },
  data() {
    return {
      pageTitle: "Students",
    };
  },
  methods: {},
};
</script>
