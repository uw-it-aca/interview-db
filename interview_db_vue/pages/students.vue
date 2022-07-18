// students.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div class="row mb-4">
        <div class="col p-5 bg-info">
          <div class="py-5">
            <h2 class="display-3 text-center mb-4">Student Interviews</h2>
            <h5 class="text-center display-4 fs-4">
              Sort interviews by student<br>characteristics
            </h5>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-3 justify-content-center">
          <StudentFilter />
        </div>

        <div class="col-9 justify-content-end px-0">
          <div class="card-columns justify-content-end">
            <StudentListing :first-name="'Amanda'" class="justify-content-end" />
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-3 justify-content-center"></div>
        <div class="col-9 justify-content-end">
          <StudentListing :first-name="'Caleb'" />
          <StudentListing :first-name="'Anna'" />
        </div>
      </div>
    </template>
  </layout>
</template>

<script>
import { Card } from "axdd-components";
import Layout from "../layout.vue";
import StudentListing from "../components/student/student-listing.vue";
import StudentFilter from "../components/student-filter.vue";

export default {
  name: "PagesStudents",
  components: {
    layout: Layout,
    "axdd-card": Card,
    StudentListing,
    StudentFilter,
  },
  data() {
    return {
      pageTitle: "Students",
    };
  },
  methods: {},
};
</script>
