// topic.vue
// shows a few student stories for one collection topic

<template>
  <div class="row mb-5">
    <div class="col p-5" style="background-color: #172643; height:330px">
      <div class="text-white py-5">
        <h2 class="display-3 text-center mb-4">{{ collectionTitle }}</h2>
        <h5 class="text-center display-4 fs-4">
          {{ collectionQuestion }}
        </h5>
      </div>
    </div>
  </div>

  <div class="row mb-5 mx-auto">
    <div v-for="story in stories" :key="story.id">
      <CollectionListing />
    </div>
  </div>
</template>

<script>
import Layout from "../layout.vue";
import CollectionListing from "./student/collection-listing.vue";
import { get } from "axios";

export default {
  name: "Topic",
  components: {
    layout: Layout,
    CollectionListing,
  },
  props: {
    topicInfo: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      // pageTitle: this.topicInfo.topic,
      stories: [],
    };
  },
  methods: {
    async loadData(props) {
      const response = await get("api/collections/" + this.topicInfo.id + "/");
      this.stories = response.data;
    },
  },
  created() {
    this.loadData();
  },
};
</script>
