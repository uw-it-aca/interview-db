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
          <div class="pt-5 ps-5 mx-auto">
            <h2 class="display-5 fw-bold mb-5">Student Stories</h2>
            <p class="fs-5 mb-4">Sort interviews by student characteristics.</p>
            <div class="row">
              <div class="col-4 justify-content-center">
                <StudentFilter @clicked="updateFilters" />
                <!-- {{ filters }} -->
              </div>

              <div class="col-7 ms-4 justify-content-end">
                <div class="card-columns justify-content-end">
                  <div v-for="student in filteredStudents" :key="student.id">
                    <StudentListing :studentInfo="student" class="mb-5" />
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
      filters: [],
    };
  },
  computed: {
    interviewId() {
      return this.$route.params.id;
    },
    singleStudentInfo() {
      return JSON.parse(this.$route.params.singleStudent);
    },
    filteredStudents() {
      if (!this.filters.length) return this.students
      const out = this.students.filter(student =>
        student.student_type.filter(trait =>
          trait.id > 1))

      return out

      // const out
      // for (let i = 0; i < this.filters.length; i++) {
      //   out += this.filters[i]
      // }

      // const checkFilter = (stu = [], filters = []) =>  {
      //   let res = [];
      //   for (let i = 0; i < stu.length; i++) {
      //     for (let j = 0; j < stu.student_type.length; j++) {
      //       if (!this.filters.includes(stu.student_type[j])) {
      //         break
      //       }
      //     }
      //     res += stu[i]
      //   }
      //   return res
      // }
      // return checkFilter(this.students, this.filters)
    }
  },
  created() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await get("/api/students/");
      this.students = response.data;
    },
    updateFilters(value) {
      this.filters = value;
    }
  },
};
</script>
