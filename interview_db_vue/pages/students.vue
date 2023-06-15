// students.vue

<template>
  <layout :page-title="pageTitle">
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div v-bind="$attrs">
        <div v-if="interviewId">
          <Interview />
        </div>

        <div v-else>
          <div class="mx-auto p-5 mb-4">
            <div class="p-auto">
              <h2 class="display-5 fw-bold mb-5 text-gold">Student Stories</h2>
              <div class="row">
                <div class="col-4 d-none d-lg-block">
                  <StudentFilter @clicked="updateFilters" />
                  <!-- {{ filters }} -->
                </div>

                <div class="col-sm-12 col-lg-7 mx-auto d-flex flex-column">
                  <router-link active-class="active" aria-current="page" to="/filters">
                    <div class="d-flex d-lg-none justify-content-end">
                      <u class="text-purple fs-5" style="display: inline;">Filters</u>
                      <i class="bi bi-filter" style="font-size: 22px"></i>
                    </div>
                  </router-link>
                  <div class="card-columns justify-content-end" v-for="student in filteredStudents" :key="student.id">
                    <InterviewListing :interviewInfo="student" class="mb-5" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
  </layout>
</template>

<script>
import Layout from "../layout.vue";
import InterviewListing from "../components/student/interview-listing.vue";
import StudentFilter from "../components/student-filter.vue";
import Interview from "../components/student/interview.vue";
import { get } from "axios";

export default {
  name: "PagesStudents",
  components: {
    layout: Layout,
    InterviewListing,
    StudentFilter,
    Interview,
  },
  props: {
    singleStudent: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      pageTitle: "Students",
      students: [],
      filters: {
        year: this.$route.query.year,
        major: this.$route.query.major,
        trait: this.$route.query.trait,
        topic: this.$route.query.topic,
      },
    };
  },
  computed: {
    console: () => console,
    interviewId() {
      return this.$route.params.id;
    },
    singleStudentInfo() {
      return JSON.parse(this.$route.params.singleStudent);
    },
    updateFilters() {
      this.filters.year = this.$route.query.year;
      this.filters.major = this.$route.query.major;
      this.filters.trait = this.$route.query.trait;
      this.filters.topic = this.$route.query.topic;
    },
    test() {
      if (this.filters.major !== undefined) {
        return JSON.parse(this.filters.major);
      }
    },
    filteredStudents() {
      // students = this.students.filter(student => {
      //   for (var key in this.filters) {
      //     if (this.filters.key.includes(student.key)) {
      //       return true;
      //     }
      //     return false;
      //   }
      // });
      
      // return this.students.filter(student => this.filters.year.includes(student.standing));
      if (this.filters.year !== undefined || this.filters.major !== undefined || this.filters.topic !== undefined) {
        return this.students.filter(student => this.filters.major.includes(student.major.full_title));
      }
      return this.students;
    },
  },
  created() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await get("/api/students/");
      this.students = response.data;
    },
  },
};
</script>
