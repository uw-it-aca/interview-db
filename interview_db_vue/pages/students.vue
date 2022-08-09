// students.vue

<template>
  <layout :page-title="pageTitle">
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div v-if="interviewId">
        <div class="mt-4">
          <div class="row w-75 mx-auto mb-5">
            <div class="col-3 justify-content-center">
              <img src="../css/quad.png" class="img-fluid mx-auto d-block" style="
              border-radius: 50%;
              height: 150px;
              width: 150px;
              object-fit: cover;" />
            </div>
            <div class="col-9 justify-content-start py-3">
              <h2 class="display-4">{{ singleStudentInfo.student.first_name }}</h2>
              <h5 class="display-3 fs-3 text-info text-uppercase">
                <div v-for="major in singleStudentInfo.major" :key="major.id">
                  {{ major.full_title + ", " }}
                </div>
                {{ singleStudentInfo.standing }}
              </h5>
            </div>
          </div>
          <Interview :studentInfo="singleStudentInfo" />
        </div>
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
              <div v-for="student in students" :key="student.id">
                <StudentListing :studentInfo="student" />
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
import StudentListing from "../components/student/interview-listing.vue";
import StudentFilter from "../components/student-filter.vue";
import Interview from "../components/student/interview.vue";
import { get } from "axios";

export default {
  name: "PagesStudents",
  components: {
    layout: Layout,
    StudentListing,
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
    };
  },
  computed: {
    interviewId() {
      return this.$route.params.id;
    },
    singleStudentInfo() {
      return JSON.parse(this.$route.params.singleStudent);
    }
  },
  created() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await get("/api/students/");
      this.students = response.data;
    }
  },
};
</script>
