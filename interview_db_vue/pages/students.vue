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
          <StudentFilter @change="loadData" />
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
                  <StudentFilter @change="loadData" />
                </div>

                <div class="col-sm-12 col-md-12 col-lg-7 mx-auto d-flex flex-column">
                  <div class="row mb-4">
                    <div class="col-6 justify-content-start">
                      <p v-if="students.length > 1" class="align-middle fw-bold opacity-75">{{ students.length + (currentPage - 1) * perPage }} of {{
                        totalCount }} Results
                      </p>
                      <p v-else-if="students.length > 0" class="align-middle fw-bold opacity-75">1 of 1
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
                  
                  <!-- remove filter buttons for mobile -->
                  <div v-if="filtersLength > 0 && (mq.mobile || mq.tablet)"
                    class="container scroll-group d-flex flex-nowrap mb-4 align-content-start justify-content-start">
                    <button type="button" class="btn btn-success me-2 inline-block justify-content-start"
                      v-for="filter in filters.year" @click="removeYear(filter)">
                      <span v-if="filter == 'Senior'">Senior +</span>
                      <span v-else>{{ filter }}</span>
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x"
                        viewBox="0 0 16 16">
                        <path
                          d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />
                      </svg>
                    </button>
                    <button type="button" class="btn btn-success me-2 inline-block" v-for="filter in filters.major"
                      @click="removeMajor(filter)">{{ filter }}
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x"
                        viewBox="0 0 16 16">
                        <path
                          d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />
                      </svg>
                    </button>
                    <button type="button" class="btn btn-success me-2 inline-block" v-for="filter in filters.topic"
                      @click="removeTopic(filter)">{{ filter }}
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x"
                        viewBox="0 0 16 16">
                        <path
                          d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />
                      </svg>
                    </button>
                  </div>

                  <div v-if="students.length > 0">
                    <div class="card-columns justify-content-end" v-for="student in students" :key="student.id">
                      <InterviewListing :interviewInfo="student" :class="(mq.mobile || mq.tablet) ? 'mb-3' : 'mb-5'" />
                    </div>
                    <vue-awesome-paginate v-if="totalPages > 1" class="mt-2 justify-content-center d-flex"
                      v-model="currentPage" :total-items="totalCount" :items-per-page="perPage" :current-page="1"
                      :hide-prev-next-when-ends="true" :on-click="updatePage" />
                  </div>
                  <div v-else-if="students.length == 0">
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
import axios from 'axios';

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
      filters: {
        year: [],
        major: [],
        topic: [],
      },
      perPage: 0,
      currentPage: 1,
      totalCount: 0,
      totalPages: 0,
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
    // makes new api call when query changes
    "$route.query": {
      immediate: true,
      handler(n) {
        this.loadData();
      }
    }
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
  },
  methods: {
    async loadData() {
      const url = this.$route.fullPath;
      const response = await axios.get("/api" + url);
      this.students = response.data['results'];
      this.perPage = response.data['page_size'];
      this.totalCount = response.data['count'];
      this.totalPages = response.data['page_count'];

      // updating stored filters, fix for bug/hv-56 to treat single filter as array
      // parsing then stringifying to make a deep copy so that url query updates with changes
      if (this.$route.query.year !== undefined) {
        if (Array.isArray(this.$route.query.year)) {
          this.filters.year = JSON.parse(JSON.stringify(this.$route.query.year));
        } else {
          this.filters.year = [];
          this.filters.year.push(JSON.parse(JSON.stringify(this.$route.query.year)));
        }
      }
      if (this.$route.query.major !== undefined) {
        if (Array.isArray(this.$route.query.major)) {
          this.filters.major = JSON.parse(JSON.stringify(this.$route.query.major));
        } else {
          this.filters.major = [];
          this.filters.major.push(JSON.parse(JSON.stringify(this.$route.query.major)));
        }
      }
      if (this.$route.query.topic !== undefined) {
        if (Array.isArray(this.$route.query.topic)) {
          this.filters.topic = JSON.parse(JSON.stringify(this.$route.query.topic));
        } else {
          this.filters.topic = [];
          this.filters.topic.push(JSON.parse(JSON.stringify(this.$route.query.topic)));
        }
      }
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
      const query = {};
      Object.entries(this.filters).forEach(([key, value]) => {
        if (value) {
          query[key] = (value);
        }
      })
      query['page'] = this.currentPage;
      this.$router.replace({ query: query });
    },
    updatePage() {
      this.$router.push({ query: { ...this.$route.query, 'page': this.currentPage } });
    },
  },
  created() {
    // set page to 1 if not set
    if (this.$route.query.page === undefined) {
      this.updatePage();
    }
    this.loadData();
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
