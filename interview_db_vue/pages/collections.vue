// collections.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div v-if="topicSlug">
        <Topic />
      </div>

      <div v-else>
        <div style="position: relative">
          <img class="banner-image" src="../images/collectionsImage.png"/>
          <div class="title-div">
            <h1 class="text-gold fw-bold display-5">Collections</h1>
          </div>
        </div>
        <div class="mb-5 row d-flex">
          <div v-for="collection in collections" :key="collection.id" class = "col-lg-4 col-md-6 col-12 d-flex align-items-stretch">
            <div class="d-flex align-items-stretch flex-fill">
              <button type="button" class="bg-light p-4 mx-2 my-3 flex-fill" @click="$router.push({
                name: 'Collections', 
                params: {id: collection.id},
                query: {topic: collection.slug}
              })">
                <div class="text-start collection-button d-flex justify-content-end row">
                  <div class="col-11">
                    <h2 class="fw-bold fs-3 mb-4 text-purple col-12">{{ collection.topic }}</h2>
                    <p class="display-4 fs-6 mx-auto col-12">
                      {{ collection.question }}
                    </p>
                  </div>
                  <div class="d-flex align-items-center col-1">
                    <i class="bi bi-chevron-right"></i>
                  </div>
                </div>
              </button>
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
    collectionsId() {
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
