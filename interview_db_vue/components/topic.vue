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
      <CollectionListing :first-name="'Amanda'" />
      <CollectionListing :first-name="'Caleb'" />
      <CollectionListing :first-name="'Anna'" />
    </div>
</template>

<script>
import Layout from "../layout.vue";
import CollectionListing from "./student/collection-listing.vue";


export default {
  name: "Topic",
  components: {
    layout: Layout,
    CollectionListing,
  },
  props: {
    collectionTitle: {
      type: String,
      required: true,
      default: "Choosing a Major",
    },
    collectionQuestion: {
      type: String,
      required: true,
      default: "How did you find your major and why did you choose it?",
    }
  },
  data() {
    return {
      pageTitle: "Topic",
    };
  },
  methods: {},
};
</script>
