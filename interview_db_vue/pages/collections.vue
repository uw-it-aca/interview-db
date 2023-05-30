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
        <div style="position: relative">
          <img class="banner-image" src="../images/collectionsImage.png"/>
          <div class="title-div">
            <h1 class="text-gold fw-bold display-5">Collections</h1>
          </div>
        </div>
        <div class="mb-5 row">
          <div v-for="collection in collections" :key="collection.id" class = "col-4">
            <div>
              <button type="button" class="bg-light p-4 mx-2 my-3 collection-btn" @click="$router.push({
                name: 'Collections', params: {
                  id: collection.id, topic: collection.topic,
                  slug: collection.slug, singleCollection: JSON.stringify(collection)
                }
              })">
                <div class="text-start collection-button">
                  <h2 class="fw-bold display-6 mb-4 text-purple">{{ collection.topic }}</h2>
                  <i class="bi bi-chevron-right justify-self-end"></i>
                  <p class="display-4 fs-6 mx-auto">
                    {{ collection.question }}
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
