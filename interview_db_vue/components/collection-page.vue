// collection-page.vue
// shows a few student stories for one collection topic

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ collectionTitle }}</h1>
    </template>

     <template #content>
      <div class="row">
        <div class="col p-5 mb-4 bg-info">
          <div class="py-5">
            <h2 class="display-5 fw-bold text-center text-uppercase">Collection Topic</h2>
            <h5 class="text-center">
              {{ collectionQuestion }}
            </h5>
          </div>
        </div>
      </div>
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
