// students.vue

<template>
  <layout :page-title="pageTitle">
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div v-if="interviewId">
        <Interview :studentInfo="singleStudentInfo" />
      </div>

      <div v-else>
        <div class="mx-auto p-5 mb-4">
          <div class="pt-5 ps-5">
            <h2 class="display-5 fw-bold mb-5">Student Stories</h2>
            <p class="fs-5 mb-5">Sort interviews by student characteristics.</p>
            <div class="row">
              <div class="col-4">
                <StudentFilter @clicked="updateFilters" />
                {{ filters }}
                <!-- {{ test }} -->
              </div>

              <div class="col-7 mx-auto">
                <div class="card-columns justify-content-end">
                  <div v-for="student in filteredStudents" :key="student.id">
                    <InterviewListing :studentInfo="student" class="mb-5" />
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
      type: Object,
      required: false,
    }
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
      for (var key in this.filters) {
        return this.filters.key;
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
      if (this.students.filter.major === undefined) {
        return this.students;
      }
      return this.students.filter(student => this.filters.major.includes(student.major.full_title));
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
