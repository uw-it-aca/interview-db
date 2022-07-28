// topic.vue
// shows a few student stories for one collection topic

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ collectionTitle }}</h1>
    </template>

     <template #content>
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
    </template>
  </layout>
</template>

<script>
import Layout from "../layout.vue";


export default {
  name: "Topic",
  components: {
    layout: Layout,

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
