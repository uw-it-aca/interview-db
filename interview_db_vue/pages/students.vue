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

        <div v-else-if="filter">
          <StudentFilter @clicked="updateFilters" />
        </div>

        <div v-else>
          <div style="position: relative">
            <img class="banner-image" src="../images/mich.jpg" />
            <div class="title-div">
              <h1 class="text-gold fw-bold display-5 mb-0">Student Stories</h1>
            </div>
          </div>

          <div class="mx-auto p-5 mb-4">
            <div class="p-auto">
              <div class="row">
                <div class="col-4 d-none d-lg-block">
                  <StudentFilter @clicked="updateFilters" />
                </div>

                this.$route.query: {{ this.$route.query }}
                <div class="col-sm-12 col-md-12 col-lg-7 mx-auto d-flex flex-column">
                  <div class="row mb-4">
                    <div class="col-6 justify-content-start">
                      <p v-if="filtered.length > 1" class="align-middle fw-bold opacity-75">{{ resultsLength }} of {{
                        filtered.length }} Results
                      </p>
                      <p v-else-if="filtered.length > 0" class="align-middle fw-bold opacity-75">{{ filtered.length }}
                        Result </p>
                    </div>

                    <div v-if="mq.tablet || mq.mobile" class="d-flex justify-content-end col-6">
                      <u v-if="filtersLength > 0" class="align-middle fw-bold"
                        @click="$router.push({ name: 'Filters', query: { ...this.$route.query } })">Filter
                        ({{ filtersLength }})</u>
                      <u v-else class="align-middle fw-bold"
                        @click="$router.push({ name: 'Filters', query: { ...this.$route.query } })">Filter</u>
                    </div>
                  </div>

                  <div v-if="filtersLength > 0 && (mq.mobile || mq.tablet)"
                    class="container scroll-group d-flex flex-nowrap mb-4 align-content-start justify-content-start">
                    <span v-for="filter in Array.isArray(filters.year) ? filters.year : [filters.year]">
                      <button type="button" class="btn btn-success me-2 inline-block justify-content-start"
                        @click="removeYear(filter)">
                        <span v-if="filter == 'Senior'">Senior +</span>
                        <span v-else>{{ filter }}</span>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x"
                          viewBox="0 0 16 16">
                          <path
                            d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />
                        </svg>
                      </button>
                    </span>
                    <button type="button" class="btn btn-success me-2 inline-block" v-for="filter in filters.major"
                      @click="removeMajor(filter)">{{ filter }}
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x"
                        viewBox="0 0 16 16">
                        <path
                          d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />
                      </svg>
                    </button>
                    {{ console.log("topics is array: ", Array.isArray(filters.topic) + ", with length " + filters.topic.length )}}
                    <span v-if="Array.isArray(filters.topic) && filters.topic.length > 1">
                      <button type="button" class="btn btn-success me-2 inline-block" @click="removeTopic(filter)" v-for="filter in filters.topic">{{
                        filter }}
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x"
                          viewBox="0 0 16 16">
                          <path
                            d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />
                        </svg>
                      </button>
                    </span>
                    <span v-else>
                      <span v-for="filter in filters.topic">
                        <button type="button" class="btn btn-success me-2 inline-block"
                          @click="removeTopic(filter)">{{ filter }}
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-x" viewBox="0 0 16 16">
                            <path
                              d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />
                          </svg>
                        </button>
                      </span>
                    </span>
                  </div>

                  <div v-if="filteredStudents.length > 0">
                    <div class="card-columns justify-content-end" v-for="student in filteredStudents" :key="student.id">
                      <InterviewListing :interviewInfo="student" :class="(mq.mobile || mq.tablet) ? 'mb-3' : 'mb-5'" />
                    </div>
                    <vue-awesome-paginate v-if="filtered.length > perPage" class="mt-2 justify-content-center d-flex"
                      v-model="currentPage" :total-items="filtered.length" :items-per-page="perPage" :current-page="1"
                      :hide-prev-next-when-ends="true" :on-click="paginateHandler" />
                  </div>
                  <div v-else-if="students.length > 0 && filteredStudents.length == 0">
                    <p class="card-columns justify-content-end fw-bold fs-5 mb-5">No matching stories found.</p>
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
  inject: ["mq"],
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
        year: [],
        major: [],
        topic: [],
      },
      perPage: 12,
      currentPage: 1,
      count: 0,
    };
  },
  watch: {
    "$route.query.page": {
      immediate: true,
      handler(n) {
        if (n !== undefined) {
          this.currentPage = JSON.parse(n)
        }
      }
    },
  },
  computed: {
    filter() {
      return this.$route.query.filter;
    },
    interviewId() {
      return this.$route.params.id;
    },
    singleStudentInfo() {
      return JSON.parse(this.$route.params.singleStudent);
    },
    filtersLength() {
      const arr = (obj) => !Array.isArray(obj) && obj !== undefined ? [obj] : obj;
      const length = (obj) => obj === undefined ? 0 : obj.length;
      return length(arr(this.filters.year)) + length(arr(this.filters.major)) + length(arr(this.filters.topic));
    },
    filteredStudents() {
      this.filtered = this.students;
      if (this.filters.year !== undefined && this.filters.year.length > 0) {
        // check for Senior+
        if (this.filters.year.includes('Senior')) {
          this.filters.year.push('Masters', 'Alumni - undergrad', 'PhD');
        }
        this.filtered = this.filtered.filter(student => this.filters.year.includes(student.standing));
      }

      if (this.filters.major !== undefined && this.filters.major.length > 0) {
        const included = (major) => this.filters.major.includes(major.full_title)
        this.filtered = this.filtered.filter(student => student.major.some(included))
      }

      if (this.filters.topic !== undefined && this.filters.topic.length > 0) {
        if (Array.isArray(this.filtered.topic)) {
          this.filtered = this.filtered.filter(student => this.filters.topic.every(
            f => student.collections.some((collection) => f === collection.topic)))
        } else {
          this.filtered = this.filtered.filter(student => student.collections.some((collection) => this.filtered.topic === collection.topic))
        }
      }

      // remove Senior+ from filters
      if (this.filters.year !== undefined && this.filters.year.includes('Masters')) {
        this.filters.year.splice(this.filters.year.length - 3, this.filters.year.length);
      }

      // pagination
      const start = this.perPage * (this.currentPage - 1);
      const end = start + this.perPage;
      return this.filtered.slice(start, end);
    },
    resultsLength() {
      return this.perPage * (this.currentPage - 1) + this.filteredStudents.length;
    }
  },
  methods: {
    async loadData() {
      const response = await get("/api/students/collections/");
      this.students = response.data;
      this.count = response.data.length;
      this.$router.replace({ query: { ...this.$route.query, 'page': this.currentPage } })
    },
    paginateHandler(page) {
      this.$router.push({ query: { ...this.$route.query, 'page': page } })
    },
    removeYear(filter) {
      const index = this.filters.year.indexOf(filter);
      if (index > -1) {
        this.filters.year.splice(index, 1);
      }
      this.updateQuery();
    },
    removeMajor(filter) {
      const index = this.filters.major.indexOf(filter);
      if (index > -1) {
        this.filters.major.splice(index, 1);
      }
      this.updateQuery();
    },
    removeTopic(filter) {
      const index = this.filters.topic.indexOf(filter);
      if (index > -1) {
        this.filters.topic.splice(index, 1);
      }
      this.updateQuery();
    },
    updateQuery() {
      console.log("update query called: ", this.$route.query)
      const query = {};
      query['page'] = 1
      Object.entries(this.filters).forEach(([key, value]) => {
        if (value) {
          query[key] = (value);
        }
      })
      this.$router.replace({ query: query });
    },
    updateFilters() {
      console.log("update filters");
      if (this.$route.query.year !== undefined) {
        this.filters.year = JSON.parse(JSON.stringify(this.$route.query.year));
      } else {
        this.filters.year = [];
      }
      if (this.$route.query.major !== undefined) {
        this.filters.major = JSON.parse(JSON.stringify(this.$route.query.major));
      } else {
        this.filters.major = [];
      }
      if (this.$route.query.topic !== undefined) {
        this.filters.topic = JSON.parse(JSON.stringify(this.$route.query.topic));
      } else {
        this.filters.topic = [];
      }
    },
  },
  created() {
    this.loadData();
    this.updateFilters();
  },
};
</script>

<style>
.pagination-container {
  display: flex;
  column-gap: 5px;
}

.paginate-buttons {
  height: 2.2rem;
  width: 2.2rem;
  border-radius: 0.1rem;
  cursor: pointer;
  background-color: inherit;
  border: none;
  color: black;
}

.paginate-buttons:hover {
  background-color: #f6f4f8;
}

.active-page {
  background-color: #4B2E83;
  border: none;
  color: white;
}

.active-page:hover {
  background-color: #583b92;
}

.scroll-group {
  white-space: nowrap;
  overflow-x: scroll;
}
</style>
