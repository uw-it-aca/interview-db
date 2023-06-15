// interview-listing.vue 
// shown on full students page, individual topic page, or home page as random carousel cards

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
        <div v-if="story" class="col-md-3 col-sm-3 row-xs mx-auto ps-4 img-div shift-up">
          <img v-if="image" :src="image" style="width:100%; object-fit:cover" class="listing-img img-fluid"
            :alt="altText" />
          <img v-else src="../../images/placeholder.png" style="width: 100%; object-fit:cover;"
            class="listing-img img-fluid" alt="a placeholder image" />
        </div>

        <div v-else class="col-md-5 col-sm-6 row-xs mx-auto ps-4 img-div shift-up">
          <img v-if="image" :src="image" style="width:100%; object-fit:cover" class="listing-img img-fluid"
            :alt="altText" />
          <img v-else src="../../images/placeholder.png" style="width: 100%; object-fit:cover;"
            class="listing-img img-fluid" alt="a placeholder image" />
        </div>

        <div v-if="story" class="col-md-9 col-sm-9 ps-4 m-0">
          <div class="row">
            <p v-if="!carousel" class="fs-6 text-end">{{ interviewDate }}</p>
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

        <div v-else class="col-md-7 col-sm-6 ps-4 m-0">
          <div class="row">
            <p v-if="!carousel" class="fs-6 text-end">{{ interviewDate }}</p>
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
          <p v-if="carousel" class="display-6 fs-6">"{{ interviewInfo.pull_quote }}"</p>
          <p v-else-if=story class="display-6 fs-5">"{{ story }}"</p>
          <p v-else class="display-6 fs-5">"{{ interviewInfo.pull_quote }}"</p>
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
    story: {
      type: String,
      required: false,
    },
    carousel: {
      type: Boolean,
      required: false,
    }
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
