// interview.vue
// full individual student interview page

<template>

  <div class="mt-4 pt-4">
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
          <div class="row">
            <div class="col">
              <span v-if="interviewInfo.standing">
                {{ interviewInfo.standing + ", studying" }}
              </span>
              <span v-else>
                Studying
              </span>
              {{ interviewInfo.declared_major }}
            </div>
            <div class="col">
              <p class="fs-6 text-end">{{ interviewDate }}</p>
            </div>
          </div>

          <div class="border-top border-primary py-4">
            <p class="text-start">They talk about...</p>
            <div class="justify-content-start col-12">
              <span v-for="topic in topics">
                <input type="checkbox" class="btn-check" :id="topic.id" :value="topic.topic"
                v-model="filters" autocomplete="off">
                <label class="btn btn-outline-success button-outline m-1" :for="topic.id">
                  {{ topic.topic }}
                </label>
              </span>
              <input type="checkbox" class="btn-check" id="clear-all" autocomplete="off">
              <label class="btn m-1" for="clear-all" @click="clearFilters">
                Clear All
              </label>
            </div>

            <div v-for="story in filteredStories" :key="story.id">
              <div class="border-top border-primary pt-4 pb-2">
                <p class="display-6 fs-5">
                  {{ story.story }}
                </p>
                <p class="fst-italic text-end">
                  <span v-for="collection in story.collections" :key="collection.id">
                    #{{ collection.topic }}
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
