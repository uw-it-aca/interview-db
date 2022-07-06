// collection-page.vue
// shows a few student stories for one collection topic

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1>{{ collectionTitle }}</h1>
    </template>

    <template #description>
      <p>{{ collectionQuestion}}</p>
    </template>
  </layout>
</template>

<script>
import Layout from "../layout.vue";
import StudentStory from "../student-story.vue";

export default {
  name: "PagesCollectionPage",
  components: {
    layout: Layout,
    "student-story": StudentStory,
  },
  props: {
    collectionTitle: {
      type: String,
      required: true,
    },
    collectionQuestion: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      pageTitle: collectionTitle,
    };
  },
  methods: {},
};
</script>
