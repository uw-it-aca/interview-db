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

      <!-- <div class="row">
        <div class="row">
          
          <div class="col-3 justify-content-center">
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Dropdown button
              </button>
              <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <a class="dropdown-item" href="#">Action</a>
                <a class="dropdown-item" href="#">Another action</a>
                <a class="dropdown-item" href="#">Something else here</a>
              </div>
            </div>
          </div>

          <div class="col-9 justify-content-end">
            <StudentListing :first-name="'Amanda'"/>
          </div>
        </div> -->

        <div class="row justify-content-end"><StudentListing :first-name="'Anna'"/></div>
        <div class="row justify-content-end"><StudentListing :first-name="'Caleb'"/></div>
      <!-- </div> -->
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
