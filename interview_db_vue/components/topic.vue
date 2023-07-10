// topic.vue
// shows all student stories for one collection topic

<template>
  <div class="mx-auto p-5 mb-4">
    <div class="p-auto">
      <h2 class="display-5 fw-bold text-gold mb-4">{{ topicInfo.topic }}</h2>
      <p class="fs-5 mb-5">{{ topicInfo.question }}</p>
      <div class="row">
        <div class="col-4 d-none d-lg-block">
          <StudentFilter story="True" @clicked="updateFilters" />
        </div>
        <div class="col-sm-12 col-lg-7 mx-auto d-flex flex-column">
          <router-link active-class="active" aria-current="page" to="/filters">
            <div class="d-flex d-lg-none justify-content-end">
              <u class="text-purple fs-5" style="display: inline;">Filters</u>
              <i class="bi bi-filter" style="font-size: 22px"></i>
            </div>
          </router-link>

          <div v-if="filteredStories.length > 0">
            <vue-awesome-paginate v-model="currentPage" :total-items="filtered.length" :items-per-page="perPage"
              :current-page="1" :on-click="onClickHandler" />
            <div class="card-columns justify-content-end" v-for="story in filteredStories" :key="story">
              <InterviewListing :interviewInfo="story.interview" :story="story.story" class="mb-5" />
            </div>
            <vue-awesome-paginate v-model="currentPage" :total-items="filtered.length" :items-per-page="perPage"
              :current-page="1" :on-click="onClickHandler" />
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
  components: {
    InterviewListing,
    StudentFilter
  },
  props: {
  },
  data() {
    return {
      stories: [],
      topicInfo: [],
      filters: {
        year: this.$route.query.year,
        major: this.$route.query.major,
      },
      filtered: [],
      perPage: 18,
      currentPage: 1,
      count: 0,
    };
  },
  computed: {
    updateFilters() {
      this.filters.year = this.$route.query.year;
      this.filters.major = this.$route.query.major;
    },
    filteredStories() {
      this.filtered = this.stories;

      if (this.filters.year !== undefined && this.filters.year.length > 0) {
        this.filtered = this.filtered.filter(student => this.filters.year.includes(student.interview.standing));
      }

      if (this.filters.major !== undefined && this.filters.major.length > 0) {
        const included = (major) => this.filters.major.includes(major.full_title)
        this.filtered = this.filtered.filter(student => student.interview.major.some(included))
      }

      // pagination
      const start = this.perPage * (this.currentPage - 1);
      const end = start + this.perPage;
      if (this.currentPage > this.filtered.length / this.perPage + 1) {
        this.currentPage = 1;
        return this.filtered.slice(0, this.perPage)
      }
      return this.filtered.slice(start, end);
    }
  },
  methods: {
    async loadData() {
      const response = await get("/api/collections/" + this.$route.params.id + "/stories/");
      this.stories = response.data;
      this.count = response.data.length;
      const info = await get("/api/collections/" + this.$route.params.id + "/");
      this.topicInfo = info.data;
    },
    onClickHandler(page) {
      this.currentPage = page;
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
  background-color: #eeeaf3;
}

.active-page {
  background-color: #4B2E83;
  border: 1px solid #4B2E83;
  color: white;
}

.active-page:hover {
  background-color: #5b3d98;
}
</style>
