// collections.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div v-if="collectionsId">
        <Topic :topicInfo="singleCollection" />
      </div>

      <div v-else>

        <div class="mx-auto p-5 mb-5">
          <div class="pt-5 ps-5 mx-auto">
            <h2 class="display-5 fw-bold mb-4">Collections</h2>
            <p class="fs-5 mb-5">Stories categorized by similar themes, collected from a diverse group of students.</p>
          </div>

          <div v-for="collection in collections" :key="collection.id">
            <div>
              <button type="button" class="bg-light p-4 m-4 collection-btn" @click="$router.push({
                name: 'Collections', params: {
                  id: collection.id, topic: collection.topic,
                  slug: collection.slug, singleCollection: JSON.stringify(collection)
                }
              })">
                <div class="text-start collection-button">
                  <h2 class="fw-bold display-6 mb-4">{{ collection.topic }}</h2>
                  <p class="display-4 fs-6 mx-auto">
                    {{ collection.question }}
                    <i class="ms-4 bi bi-chevron-right"></i>
                  </p>
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
    singleCollection: {
      type: Object,
      required: false,
    }
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
    singleCollection() {
      return JSON.parse(this.$route.params.singleCollection);
    }
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
