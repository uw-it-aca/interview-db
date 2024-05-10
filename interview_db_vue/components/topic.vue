// topic.vue
// shows all student stories for one collection topic

<template>
  <div class="mx-auto p-5 mb-4">
    <div class="p-auto">
      <h2 class="display-5 fw-bold text-gold mb-4">{{ topicInfo.topic }}</h2>
      <p class="fs-5 mb-5">{{ topicInfo.question }}</p>
      <div class="row">
        <div class="col-4 d-none d-lg-block">
          <StudentFilter :story="true" @clicked="updateFilters" />
        </div>
        <div class="col-sm-12 col-lg-7 mx-auto d-flex flex-column">
          <div class="row mb-4">
            <div class="col-6 justify-content-start">
              <p v-if="stories.length > 1" class="align-middle fw-bold opacity-75">
              {{ stories.length + (currentPage - 1) * perPage }} of {{ totalCount}} Results
              </p>
              <p v-else-if="stories.length > 0" class="align-middle fw-bold opacity-75">
                1 of 1 Result </p>
            </div>
            <div v-if="mq.tablet || mq.mobile" class="d-flex justify-content-end col-6">
              <u v-if="filtersLength > 0" class="align-middle fw-bold"
                @click="$router.push({ name: 'Filters', params: {id: topicId}, query: { ...this.$route.query } })">Filter
                ({{ filtersLength }})</u>
              <u v-else class="align-middle fw-bold"
                @click="$router.push({ name: 'Filters', params: {id: topicId}, query: { ...this.$route.query } })">Filter</u>
            </div>
          </div>

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
          </div>


          <div v-if="stories.length > 0">
            <div class="card-columns justify-content-end" v-for="story in stories" :key="story">
              <InterviewListing :interviewInfo="story.interview" :story="story.story"
                :class="(mq.mobile || mq.tablet) ? 'mb-3' : 'mb-5'" />
            </div>
            <vue-awesome-paginate v-if="totalPages > 1" class="mt-2 justify-content-center d-flex"
              v-model="currentPage" :total-items="totalCount" :items-per-page="perPage" :current-page="1"
              :hide-prev-next-when-ends="true" :on-click="updateQuery" />
          </div>
          <div v-else-if="stories.length == 0">
            <p class="card-columns justify-content-end fw-bold fs-5 mb-5">No matching stories were found.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import InterviewListing from "./student/interview-listing.vue";
import StudentFilter from "./student-filter.vue";
import axios from 'axios';

export default {
  name: "Topic",
  inject: ["mq"],
  components: {
    InterviewListing,
    StudentFilter
  },
  data() {
    return {
      stories: [],
      topicInfo: [],
      topicId: this.$route.params.id,
      filtered: [],
      filters: {
        year: this.$route.query.year,
        major: this.$route.query.major,
      },
      perPage: 0,
      currentPage: 1,
      totalCount: 0,
      totalPages: 0,
    };
  },
  computed: {
    filtersLength() {
      const arr = (obj) => !Array.isArray(obj) && obj !== undefined ? [obj] : obj;
      const length = (obj) => obj === undefined ? 0 : obj.length;
      return length(arr(this.filters.year)) + length(arr(this.filters.major)) + length(arr(this.filters.topic));
    },
  },
  methods: {
    async loadData() {
      // get stories for this topic
      const url = this.$route.fullPath;
      const response = await axios.get("/api" + url);
      this.stories = response.data['results'];
      this.perPage = response.data['page_size'];
      this.totalCount = response.data['count'];
      this.totalPages = response.data['page_count'];

      // get this topic's info
      const infoResponse = await axios.get("/api/collections/" + this.$route.params.id + "/info/");
      this.topicInfo = infoResponse.data;
      this.$router.replace({ query: { ...this.$route.query, 'page': this.currentPage } })
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
    async updateFilters() {
      this.loadData();
      // updating stored filters
      // if (this.$route.query.year !== undefined) {
      //   if (Array.isArray(this.$route.query.year)) {
      //     this.filters.year = JSON.parse(JSON.stringify(this.$route.query.year));
      //   } else {
      //     this.filters.year = [];
      //     this.filters.year.push(JSON.parse(JSON.stringify(this.$route.query.year)));
      //   }
      // } else {
      //   this.filters.year = [];
      // }
      // if (this.$route.query.major !== undefined) {
      //   if (Array.isArray(this.$route.query.major)) {
      //     this.filters.major = JSON.parse(JSON.stringify(this.$route.query.major));
      //   } else {
      //     this.filters.major = [];
      //     this.filters.major.push(JSON.parse(JSON.stringify(this.$route.query.major)));
      //   }
      // } else {
      //   this.filters.major = [];
      // }
    },
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
        console.log("called query watcher, reloading data")
        this.loadData();
      }
    }
  },
  created() {
    if (this.$route.query.page === undefined) {
      this.$router.push({ query: { ...this.$route.query, 'page': 1 } });
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