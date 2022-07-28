// students.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div v-if="studentInterview">
        <Interview />
        <p>student interview #: {{ studentInterview }}</p>
      </div>
      
      <div v-else>
        <div class="row mb-5">
          <div class="col p-5" style="background-color: #172643; height: 330px">
            <div class="text-white py-5">
              <h2 class="display-3 text-center mb-4">Student Interviews</h2>
              <h5 class="text-center display-4 fs-4">
                Sort interviews by student<br />characteristics
              </h5>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-3 justify-content-center">
            <StudentFilter />
          </div>

          <div class="col-9 justify-content-end">
            <div class="card-columns justify-content-end">
              <StudentListing :first-name="'Amanda'" />
              <StudentListing :first-name="'Caleb'" />
              <StudentListing :first-name="'Anna'" />
            </div>
          </div>
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
import Interview from "../components/student/interview.vue";

export default {
  name: "PagesStudents",
  components: {
    layout: Layout,
    StudentListing,
    StudentFilter,
    Interview,
  },
  data() {
    return {
      pageTitle: "Students",
    };
  },
  computed: {
    studentInterview() {
      return this.$route.params.id;
    },
  },
  methods: {},
};
</script>
