// interview-listing.vue 
// shown on full students page, individual topic page, or as carousel on home page

<template>
  <button type="button" class="shadow-sm btn-card mt-5" style="height:fit-content;" @click="$router.push({
    name: 'Students',
    params: {
      id: interviewInfo.id,
    },
  })
    ">
    <div class="d-flex card-clickable">
      <div class="row p-0 m-x-0">
        <div class="col-md-4 col-sm-5 row-xs mx-auto ps-4 img-div shift-up">
          <img v-if="image" :src="image" style="width:100%; object-fit:cover" class="listing-img img-fluid"
            :alt="altText" />
          <img v-else src="../../images/placeholder.png" style="width:100%; object-fit:cover" class="listing-img img-fluid" alt="a placeholder image" />
        </div>

        <div class="col-md-8 col-sm-7 p-4 m-0">
          <div class="row">
            <p v-if="!carousel && !(mq.mobile || mq.tablet)"  class="fs-6 text-end">{{ interviewDate }}</p>
            <h2 class="card-title fw-bold text-purple" :class="(carousel || (mq.mobile || mq.tablet)) ? 'display-4 fs-3 mb-2' : 'display-6 mb-2'">
              {{ interviewInfo.student.first_name }}
            </h2>
            <p class="pb-4 border-bottom border-primary" :class="(carousel || (mq.mobile || mq.tablet)) ? '' : 'display-4 fs-5'">
              <span v-if="interviewInfo.standing">
                {{ interviewInfo.standing + ", studying" }}
              </span>
              <span v-else> Studying </span>
              {{ interviewInfo.declared_major }}
            </p>
          </div>
        </div>

        <div class="card-text px-4">
          <p v-if=story class="lh-base">"{{ story }}"</p>
          <p v-else class="lh-base">"{{ interviewInfo.pull_quote }}"</p>
        </div>

        <div class="d-flex justify-content-end">
          <p class="text-purple" style="display:inline;">Read More</p>
          <p>&nbsp;</p>
          <i class="bi bi-chevron-right"></i>
        </div>
      </div>
    </div>
  </button>
</template>

<script>
import axios from 'axios';
export default {
  name: "StudentListing",
  inject: ["mq"],
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
      if (this.interviewInfo.image == null) return;
      this.altText = this.interviewInfo.image_alt_text;

      // create blob for image
      try {
        const blob = await axios.get("/api/students/" + this.interviewInfo.id + "/image/", { responseType: 'blob' });
        this.image = URL.createObjectURL(blob.data);
      } catch (err) {
        console.log(err);
      }
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

<style>
</style>