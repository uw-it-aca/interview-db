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
                </div>

                <div class="col-sm-12 col-lg-7 mx-auto d-flex flex-column">
                  <router-link active-class="active" aria-current="page" to="/filters">
                    <div class="d-flex d-lg-none justify-content-end">
                      <u class="text-purple fs-5" style="display: inline;">Filters</u>
                      <i class="bi bi-filter" style="font-size: 22px"></i>
                    </div>
                  </router-link>
                  <vue-awesome-paginate v-if="filtered.length > 0" v-model="currentPage" :total-items="filtered.length" :items-per-page="perPage"
                    :current-page="1" :on-click="onClickHandler" />
                  <div class="card-columns justify-content-end" v-for="student in filteredStudents" :key="student.id">
                    <InterviewListing :interviewInfo="student" class="mb-5" />
                  </div>
                  <vue-awesome-paginate v-if="filtered.length > 0" v-model="currentPage" :total-items="filtered.length" :items-per-page="perPage"
                    :current-page="1" :on-click="onClickHandler" />
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
      collections: [],
      filtered: [],
      filters: {
        year: this.$route.query.year,
        major: this.$route.query.major,
        topic: this.$route.query.topic,
      },
      perPage: 15,
      currentPage: 1,
      count: 0,
    };
  },
  computed: {
    interviewId() {
      return this.$route.params.id;
    },
    singleStudentInfo() {
      return JSON.parse(this.$route.params.singleStudent);
    },
    updateFilters() {
      this.filters.year = this.$route.query.year;
      this.filters.major = this.$route.query.major;
      this.filters.topic = this.$route.query.topic;
    },
    filteredStudents() {
      this.filtered = this.students;

      if (this.filters.year !== undefined && this.filters.year.length > 0) {
        this.filtered = this.filtered.filter(student => this.filters.year.includes(student.standing));
      }

      if (this.filters.major !== undefined && this.filters.major.length > 0) {
        const included = (major) => this.filters.major.includes(major.full_title)
        this.filtered = this.filtered.filter(student => student.major.some(included))
      }

      if (this.filters.topic !== undefined && this.filters.topic.length > 0) {
        this.filtered = this.filtered.filter(student => this.filters.topic.every(
          f => student.collections.some((collection) => f === collection.slug)))
      }

      // pagination
      const start = this.perPage * (this.currentPage - 1);
      const end = start + this.perPage;
      if (this.currentPage > this.filtered.length / this.perPage) {
        this.currentPage = 1;
        return this.filtered.slice(0, this.per)
      }
      return this.filtered.slice(start, end);
    },
  },
  created() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await get("/api/students/collections/");
      this.students = response.data;
      this.count = response.data.length;
    },
    onClickHandler(page) {
      this.currentPage = page;
    }
  },
};
</script>

<style>
.pagination-container {
  display: flex;
  column-gap: 10px;
}

.paginate-buttons {
  height: 40px;
  width: 40px;
  border-radius: 1px;
  cursor: pointer;
  background-color: #FAF8FC;
  border: 1px solid black;
  color: black;
}

.paginate-buttons:hover {
  background-color: #d8d8d8;
}

.active-page {
  background-color: #B4A67F;
  border: 1px solid #B4A67F;
  color: white;
}

.active-page:hover {
  background-color: #ccbc90;
}
</style>
