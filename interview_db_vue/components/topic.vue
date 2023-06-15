// topic.vue
// shows all student stories for one collection topic

<template>
  <div class="mx-auto p-5 mb-4">
    <div class="p-auto">
      <h2 class="display-5 fw-bold text-gold mb-4">{{ topicInfo.topic }}</h2>
      <p class="fs-5 mb-5">{{ topicInfo.question }}</p>
    </div>


    <div class="row w-75 mb-5 mx-auto">
      <div v-for="story in stories" :key="story.id">
        <InterviewListing :interviewInfo="story.interview" :story="story.story" />
      </div>
    </div>
  </div>
</template>

<script>
import InterviewListing from "./student/interview-listing.vue";
import { get } from "axios";

export default {
  name: "Topic",
  components: {
    InterviewListing,
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
