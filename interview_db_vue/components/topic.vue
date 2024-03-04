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
              <p v-if="filtered.length > 1" class="align-middle fw-bold opacity-75">
              {{ resultsLength }} of {{filtered.length }} Results
              </p>
              <p v-else-if="filtered.length > 0" class="align-middle fw-bold opacity-75">
                {{ filtered.length }} Result </p>
            </div>
            <div v-if="mq.tablet || mq.mobile" class="d-flex justify-content-end col-6">
              <u v-if="filtersLength > 0" class="align-middle fw-bold"
                @click="$router.push({ name: 'Filters', params: {type: 'topic', id: topicId}, query: { ...this.$route.query } })">Filter
                ({{ filtersLength }})</u>
              <u v-else class="align-middle fw-bold"
                @click="$router.push({ name: 'Filters', params: {type: 'topic', id: topicId}, query: { ...this.$route.query } })">Filter</u>
            </div>
          </div>

          <div v-if="filteredStories.length > 0">
            <div class="card-columns justify-content-end" v-for="story in filteredStories" :key="story">
              <InterviewListing :interviewInfo="story.interview" :story="story.story"
                :class="(mq.mobile || mq.tablet) ? 'mb-3' : 'mb-5'" />
            </div>
            <vue-awesome-paginate v-if="filtered.length > perPage" class="mt-2 justify-content-center d-flex"
              v-model="currentPage" :total-items="filtered.length" :items-per-page="perPage" :current-page="1"
              :hide-prev-next-when-ends="true" :on-click="paginateHandler" />
          </div>
          <div v-else-if="stories.length > 0 && filteredStories.length == 0">
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
import { get } from "axios";

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
      perPage: 8,
      currentPage: 1,
      count: 0,
    };
  },
  computed: {
    updateFilters() {
      this.filters.year = this.$route.query.year;
      this.filters.major = this.$route.query.major;
    },
    filtersLength() {
      const arr = (obj) => !Array.isArray(obj) && obj !== undefined ? [obj] : obj;
      const length = (obj) => obj === undefined ? 0 : obj.length;
      return length(arr(this.filters.year)) + length(arr(this.filters.major)) + length(arr(this.filters.topic));
    },
    filteredStories() {
      this.filtered = this.stories;
      if (this.filters.year !== undefined && this.filters.year.length > 0) {
        // combine for Senior+
        if (this.filters.year.includes('Senior')) {
          this.filters.year.push('Masters', 'Alumni - undergrad', 'PhD');
        }
        this.filtered = this.filtered.filter(student => this.filters.year.includes(student.interview.standing));
      }

      if (this.filters.major !== undefined && this.filters.major.length > 0) {
        const included = (major) => this.filters.major.includes(major.full_title)
        this.filtered = this.filtered.filter(student => student.interview.major.some(included))
      }

      // pagination
      const start = this.perPage * (this.currentPage - 1);
      const end = start + this.perPage;
      return this.filtered.slice(start, end);
    },
    resultsLength() {
      return this.perPage * (this.currentPage - 1) + this.filteredStories.length;
    }
  },
  methods: {
    async loadData() {
      const response = await get("/api/collections/" + this.$route.params.id + "/stories/");
      this.stories = response.data;
      this.count = response.data.length;
      const info = await get("/api/collections/" + this.$route.params.id + "/");
      this.topicInfo = info.data;
      this.$router.replace({ query: { ...this.$route.query, 'page': this.currentPage } })
    },
    paginateHandler(page) {
      this.$router.push({ query: { ...this.$route.query, 'page': page } })
    }
  },
  watch: {
    "$route.query.page": {
      immediate: true,
      handler(n) {
        if (n !== undefined) {
          this.currentPage = JSON.parse(n)
        }
      }
    }
  },
  created() {
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