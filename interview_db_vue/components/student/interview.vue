// interview.vue
// full individual student interview page

<template>
  <div>
    <div class="card border-0">
      <div class="row g-0 mx-auto interview-height">
        <div class="col-lg-6 col-12" style="height: inherit;">
          <span v-if="image" style="width: 100%">
            <img :src="image" class="img-fluid mx-auto position-sticky" style="height: 100%; object-fit: cover;"
              :alt="altText" />
          </span>
          <span v-else style="width: 100%">
            <img src="../../images/placeholder.png" class="img-fluid mx-auto position-sticky"
              style="height: 100%; object-fit: cover; width: 100%" />
          </span>
        </div>

        <div class="col-lg-6 col-12 p-5 scroll-area">
          <h2 class="card-title display-4 mb-2 text-gold fw-bold">{{ studentInfo.first_name }}</h2>
          <div class="row mb-2">
            <div :class="mq.mobile ? '': 'col-9'">
              <span v-if="interviewInfo.standing">
                {{ interviewInfo.standing + ", studying" }}
              </span>
              <span v-else>
                Studying
              </span>
              {{ interviewInfo.declared_major }}
            </div>
            <div  :class="mq.mobile ? 'mt-2': 'col text-end'">
              <p class="fs-6">{{ interviewDate }}</p>
            </div>
          </div>

          <div class="border-top border-success pt-4 mb-4">
            <p class="text-start">They talk about...</p>
            <div class="justify-content-start col-12 mb-4">
              <span v-for="topic in topics" :key="topic.id">
                <input type="checkbox" class="btn-check" :id="topic.id" :value="topic.topic" v-model="filters"
                  autocomplete="off">
                <label class="btn btn-outline-success m-1" :for="topic.id">
                  {{ topic.topic }}
                </label>
              </span>
              <a v-if="filters !== undefined && filters.length > 0" class="btn border-0 text-secondary active-link active-link-hover" @click="clearFilters">Clear All
              </a>
            </div>

            <div v-for="story in filteredStories" :key="story.id">
              <div class="border-top border-success pt-4 pb-2">
                <p class="display-6 fs-6 lh-base">
                  {{ story.story }}
                </p>
                <p class="fst-italic text-secondary" :class="mq.mobile ? 'text-start' : 'text-end'">
                  <span v-for="collection in story.collections" :key="collection.id">
                    <router-link :to="{ name: 'Collections', params: { id: collection.id } }" class="active-link">
                      #{{ collection.topic }}
                    </router-link>
                    &nbsp;
                  </span>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { get } from "axios";

export default {
  name: "Interview",
  inject: ["mq"],
  components: {
  },
  computed: {
    interviewId() {
      return this.$route.params.id;
    },
    filteredStories() {
      this.filtered = this.stories;
      if (this.filters !== undefined && this.filters.length > 0) {
        const included = (collection) => this.filters.includes(collection.topic)
        this.filtered = this.filtered.filter(story => story.collections.some(included))
      }
      return this.filtered;
    }
  },
  data() {
    return {
      stories: [],
      filtered: [],
      filters: [],
      interviewInfo: [],
      topics: [],
      studentInfo: [],
      interviewDate: null,
      image: null,
      altText: null,
    }
  },
  methods: {
    async loadData() {
      const response = await get("/api/students/" + this.interviewId + "/");
      this.stories = response.data;
      this.interviewInfo = this.stories[0].interview;
      this.studentInfo = this.interviewInfo.student;
      this.interviewDate = new Date(this.interviewInfo.date).toLocaleDateString('en-US');

      const topics = await get("/api/students/" + this.interviewId + "/topics/");
      this.topics = topics.data;

      if (this.interviewInfo.image != null) {
        this.loadImage();
      }
    },
    async loadImage() {
      if (this.interviewInfo.no_identifying_photo && !this.interviewInfo.image_is_not_identifying) {
        return;
      }

      this.altText = this.interviewInfo.image_alt_text;

      // create blob for image
      try {
        const blob = await get("/api/students/" + this.interviewInfo.id + "/image/", { responseType: 'blob' });
        this.image = URL.createObjectURL(blob.data);
      } catch (err) {
        console.log(err);
      }
    },
    clearFilters() {
      this.filters = [];
    }
  },
  created() {
    this.loadData();
  },
};
</script>

<style>
.btn-outline-success {
  --bs-btn-bg: white !important;
  --bs-btn-border-color: #1E1E1E !important;
  --bs-btn-color: #1E1E1E !important;
}
a.active-link {
  text-decoration: none;
  color: #827252;
  white-space: nowrap;
}
a.active-link:hover{
  color: #827252;
  text-decoration: underline;
}
</style>
