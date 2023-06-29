// topic.vue
// shows all student stories for one collection topic

<template>
  <div class="mx-auto p-5 mb-4">
    <div class="p-auto">
      <h2 class="display-5 fw-bold text-gold mb-4">{{ topicInfo.topic }}</h2>
      <p class="fs-5 mb-5">{{ topicInfo.question }}</p>
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
          <div class="card-columns justify-content-end" v-for="story in stories" :key="story.id">
            <InterviewListing :interviewInfo="story.interview" :story="story.story" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import InterviewListing from "./student/interview-listing.vue";
import StudentFilter from "../components/student-filter.vue";
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
    };
  },
  methods: {
    async loadData() {
      const response = await get("/api/collections/" + this.$route.params.id + "/stories/");
      this.stories = response.data;
      const info = await get("/api/collections/" + this.$route.params.id + "/");
      this.topicInfo = info.data;
    },
  },
  created() {
    this.loadData();
  },
};
</script>
