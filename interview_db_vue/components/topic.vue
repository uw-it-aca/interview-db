// topic.vue
// shows all student stories for one collection topic

<template>
  <div class="row mb-5">
    <div class="col p-5" style="background-color: #172643; height:330px">
      <div class="text-white mx-auto py-5">
        <div class="row w-50 mx-auto">
          <h2 class="text-start display-3 mb-4">{{ topicInfo.topic }}</h2>
        </div>
        <div class="row w-50 mx-auto ps-5">
          <h5 class="text-start display-4 fs-4">
            {{ topicInfo.question }}
          </h5>
        </div>
      </div>
    </div>
  </div>

  <div class="row mb-5 mx-auto">
    <div v-for="story in stories" :key="story.id">
      <InterviewListing :studentInfo="story" />
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
    topicInfo: {
      type: Object,
      required: false,
    },
  },
  data() {
    return {
      stories: [],
    };
  },
  methods: {
    async loadData() {
      const response = await get("/api/collections/" + this.topicInfo.id + "/" + this.topicInfo.topic + "/");
      this.stories = response.data;
    },
  },
  created() {
    this.loadData();
  },
};
</script>
