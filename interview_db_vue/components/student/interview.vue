// interview.vue
// full individual student interview page

<template>

  <div class="mt-4 pt-4">
    <div class="card border-0">
      <div class="row g-0 mx-auto">
        <div class="col-4">
          <span v-if="image">
            <img :src="image" class="img-fluid mx-auto d-block" alt={{altText}}/>
          </span>
          <span v-else>
            <img src="../../css/quad.png" class="img-fluid mx-auto d-block" alt="a placeholder image"/>
          </span>
        </div>

        <div class="col-8 p-5">
          <h2 class="card-title display-6 mb-2 fw-bold">{{ studentInfo.first_name }}</h2>
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
            <div class="justify-content-start col-10">
              <span v-for="story in stories" :key="story.id">
                <span v-for="collection in story.code" :key="collection.id">
                  <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">
                    {{ collection.code }}
                  </button>
                </span>
              </span>
              <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">
                Clear All
              </button>
            </div>

            <div v-for="story in stories" :key="story.id">
              <div class="border-top border-primary pt-4 pb-2">
                <p class="display-6 fs-5">
                  {{ story.story }}
                </p>
                <p class="fst-italic text-end">
                  <span v-for="collection in story.code" :key="collection.id">
                    #{{ collection.code }}
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
    }
  },
  data() {
    return {
      stories: [],
      interviewInfo: [],
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

      if (this.interviewInfo.image) {
        this.loadImage();
      }
    },
    async loadImage() {
      if (this.interviewInfo.no_identifying_photo && !this.interviewInfo.image_is_not_identifying) {
        return;
      }
      this.altText = this.interviewInfo.image_alt_text;

      // create blob for image
      const blob = await get("/api/students/"+ this.interviewId + "/image/", {responseType: 'blob'});
      this.image = blob.data;
      this.image = URL.createObjectURL(this.image);
    },
  },
  created() {
    this.loadData();
  }
};
</script>
