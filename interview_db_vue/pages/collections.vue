// collections.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div v-bind="$attrs">
        <div v-if="topicId">
          <Topic />
        </div>

        <div v-else>
          <div style="position: relative">
            <img class="banner-image" src="../images/collectionsImage.png" />
            <div class="title-div">
              <h1 class="text-gold fw-bold display-5 mb-0">Collections</h1>
            </div>
          </div>
          <div class="mx-auto p-5">
            <p class="fs-5 mb-4">Stories categorized by similar themes, collected from a diverse group of
              students.</p>
            <div class="mb-5 row d-flex">
              <div v-for="collection in collections" :key="collection.id"
                class="col-lg-4 col-md-6 col-12 d-flex align-items-stretch">
                <div class="d-flex align-items-stretch flex-fill">
                  <button type="button" class="btn-card p-4 mx-2 my-3 flex-fill" @click="$router.push({
                    name: 'Collections',
                    params: { id: collection.id },
                    // query: { topic: collection.slug }
                  })">
                    <div class="text-start d-flex row">
                      <div class="col-lg-10 col-md-11 col-12">
                        <h2 class="fw-bold display-4 fs-3 mb-4 text-purple">{{ collection.topic }}</h2>
                        <p class="display-4 fs-6 mx-auto">
                          {{ collection.question }}
                        </p>
                      </div>
                      <div class="align-items-center d-flex col-md-1 col-lg-2 justify-content-end">
                        <i class="bi bi-chevron-right"></i>
                      </div>
                    </div>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
  </layout>
</template>

<script>
import Layout from "../layout.vue";
import Topic from "../components/topic.vue";
import { get } from "axios";

export default {
  name: "PagesCollections",
  inject: ["mq"],
  components: {
    layout: Layout,
    Topic,
  },
  props: {
  },
  data() {
    return {
      pageTitle: "Collections",
      collections: [],
    };
  },
  computed: {
    topicId() {
      return this.$route.params.id;
    },
    topicSlug() {
      return this.$route.query.topic;
    },
  },
  created() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await get("/api/collections/");
      this.collections = response.data;
    }
  },
};
</script>
<style>
</style>