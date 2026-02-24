<template>
  <div
    class="student-card shadow-sm"
    role="button"
    @click="navigateToInterview"
  >
    <div class="card-inner d-flex flex-column flex-md-row">

      <div class="image-wrapper">
        <img
          v-if="image"
          :src="image"
          class="student-image"
          :alt="altText"
        />
        <img
          v-else
          src="../../images/placeholder.png"
          class="student-image"
          alt="placeholder image"
        />
      </div>

      <!-- Content -->
      <div class="content-wrapper">
        <h2 class="student-name">
          {{ interviewInfo.student.first_name }}
        </h2>

        <!-- Tags -->
        <div class="tag-row">
          <span v-if="interviewInfo.standing" class="tag">
            {{ interviewInfo.standing }}
          </span>

          <span class="tag">
            {{ interviewInfo.declared_major }}
          </span>

          <span v-if="interviewInfo.minor" class="tag">
            {{ interviewInfo.minor }}
          </span>
        </div>

        <!-- Quote -->
        <blockquote class="pull-quote">
          “{{ story || interviewInfo.pull_quote }}”
        </blockquote>

        <!-- Read More button -->
        <button
          type="button"
          class="btn btn-purple"
          @click.stop="$router.push({
            name: 'Students',
            params: { id: interviewInfo.id }
          })"
        >
          Read More <i class="bi bi-chevron-right"></i>
        </button>

      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "StudentListing",
  inject: ["mq"],

  props: {
    interviewInfo: { type: Object, required: true },
    story: { type: String, required: false },
    carousel: { type: Boolean, required: false }
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
    navigateToInterview() {
      if (this.interviewInfo?.id) {
        this.$router.push({
          name: 'Students',
          params: { id: this.interviewInfo.id }
        });
      }
    },
    async loadImage() {
      if (this.interviewInfo.no_identifying_photo && !this.interviewInfo.image_is_not_identifying) return;
      if (!this.interviewInfo.image) return;

      this.altText = this.interviewInfo.image_alt_text;

      try {
        const blob = await axios.get(
          "/api/students/" + this.interviewInfo.id + "/image/",
          { responseType: "blob" }
        );
        this.image = URL.createObjectURL(blob.data);
      } catch (err) {
        // Image not available or failed to load
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
