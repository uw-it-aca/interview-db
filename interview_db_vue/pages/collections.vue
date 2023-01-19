// collections.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div v-if="collectionsTopic">
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
              <button type="button" class="bg-light p-4 m-4"
                @click="$router.push({ name: 'Collections', params: { topic:  collection.topic, singleCollection: JSON.stringify(collection) } })">
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


          <!-- <div v-for="collection, index in collections" :key="collection.id">
          <div v-if="index % 2 == 0">
            <div class="card w-100 border-0 overflow-hidden" style="height: 380px">
              <div class="row g-0">
                <div class="col-7">
                  <img src="../css/major.png" class="w-100 h-100 img-fluid" style="object-fit: cover" />
                </div>
                <div class="col-5 p-5 justify-content-center text-white" style="background-color: #172643">
                  <div class="text-center mx-auto">
                    <h5 class="card-title mb-4 pt-5 display-6">{{ collection.topic }}</h5>
                    <p class="card-text w-75 mb-4 mx-auto display-4 fs-4">
                      {{ collection.question }}
                    </p>
                    <p class="card-text display-4 fs-4">
                      <router-link
                        :to="{ name: 'Collections', params: { id: collection.id, singleCollection: JSON.stringify(collection) } }"
                        class="active-link" style="color: inherit">
                        Read Collection >
                      </router-link>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div> -->
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
    collectionsTopic() {
      return this.$route.params.topic;
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
