// interview-listing.vue // shown on full students page

<template>
  <button type="button" class="btn-card mt-5" style="height:fit-content;" @click="$router.push({
    name: 'Students',
    params: {
      id: interviewInfo.id,
    },
  })
    ">
    <div class="d-flex card-clickable">
      <div class="row p-0 m-x-0">
        <div class="col-md-5 col-sm-6 row-xs mx-auto ps-4 img-div shift-up">
          <span v-if="image" style="width: 100%;">
            <img :src="image" style="object-fit:cover" class="listing-img img-fluid" :alt="altText" />
          </span>
          <span v-else style="width: 100%;">
            <img src="../../images/placeholder.png" style="object-fit:cover;" class="listing-img img-fluid" alt="a placeholder image" />
          </span>
        </div>

        <div class="col-md-7 col-sm-6 ps-4 m-0">
          <div class="row">
            <p class="fs-6 text-end">{{ interviewDate }}</p>
            <h2 class="card-title fw-bold text-purple display-6 mb-2">
              {{ interviewInfo.student.first_name }}
            </h2>
            <p class="display-4 fs-6 mx-auto pb-4 border-bottom border-primary">
              <span v-if="interviewInfo.standing">
                {{ interviewInfo.standing + ", studying" }}
              </span>
              <span v-else> Studying </span>
              {{ interviewInfo.declared_major }}
            </p>
          </div>
        </div>

        <div class="card-text px-4">
          <p class="display-6 fs-5">"{{ interviewInfo.pull_quote }}"</p>
        </div>
        <div class="d-flex justify-content-end">
          <u class="text-purple" style="display:inline;">Read More</u>
          <i class="bi bi-chevron-right"></i>
        </div>
      </div>
    </div>

  </button>
</template>

<script>
import { get } from "axios";
export default {
  name: "StudentListing",
  props: {
    interviewInfo: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      image: null,
      altText: null,
    };
  },
  created() {
    this.loadImage();
  },
  methods: {
    async loadImage() {
      if (this.interviewInfo.no_identifying_photo && !this.interviewInfo.image_is_not_identifying) {
        return;
      }
      
      if (this.interviewInfo.image == null) return;

      this.altText = this.interviewInfo.image_alt_text;
      // create blob for image
      const blob = await get("/api/students/" + this.interviewInfo.id + "/image/", { responseType: 'blob' });
      this.image = blob.data;
      this.image = URL.createObjectURL(this.image);
    },
  },
  computed: {
    interviewDate() {
      return new Date(this.interviewInfo.date).toLocaleDateString("en-US");
    },
    interviewId() {
      return this.interviewInfo.id;
    }
  },
};
</script>
