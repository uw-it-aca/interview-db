// topic.vue
// shows all student stories for one collection topic

<template>
  <div class="row mb-5">
    <div class="col p-5" style="background-color: #172643; height:330px">
      <div class="text-white py-5">
        <h2 class="display-3 mb-4 mx-auto">{{ topicInfo.topic }}</h2>
        <div class="row w-50 mx-auto">
          <h5 class="text-start display-4 fs-4">
            {{ topicInfo.question }}
          </h5>
        </div>
      </div>
    </div>
  </div>

  <div class="row mb-5 mx-auto">
    <div v-for="story in stories" :key="story.id">
      <CollectionListing :studentInfo="story" />
    </div>
  </div>
</template>

<script>
import CollectionListing from "./student/collection-listing.vue";
import { get } from "axios";

export default {
  name: "Topic",
  components: {
    CollectionListing,
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
      const response = await get("/api/collections/" + this.topicInfo.id + "/");
      this.stories = response.data;
    },
  },
  created() {
    this.loadData();
  },
};
</script>
