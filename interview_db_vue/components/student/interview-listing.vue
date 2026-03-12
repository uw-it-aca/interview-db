<template>
  <div
    class="student-card"
    role="button"
    @click="navigateToInterview"
  >
    <!-- Top tag bar -->
    <div class="tag-bar">
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
    </div>

    <!-- Card body -->
    <div class="card-inner">
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

      <div class="content-wrapper">
        <blockquote class="pull-quote">
          “{{ story || interviewInfo.pull_quote }}”
        </blockquote>

        <button
          type="button"
          class="read-more-btn"
          @click.stop="navigateToInterview"
        >
          Read {{ interviewInfo.student.first_name }}'s Story
          <i class="bi bi-chevron-right"></i>
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

<style scoped>
.student-card {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.12);
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
  margin-bottom: 2rem;
}

.student-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.18);
}

.tag-bar {
  background-color: #4b2e83;
  padding: 0.5rem 0.5rem;
  display: flex;
  align-items: center;
}

.tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
  height: 100%;
  margin-bottom: 0px;
}

.tag {
  display: inline-flex;
  align-items: center;
  background-color: #6b4ba8;
  color: #ffffff;
  font-size: 0.8rem;
  padding: 0.3rem 0.9rem;
  border-radius: 24px;
  font-weight: 550;
}

.card-inner {
  display: flex;
  flex-direction: row;
  align-items: stretch;
  padding: 1.5rem 2rem;
  gap: 1.5rem;
  margin-top: 0;
  overflow: hidden;
}

.image-wrapper {
  flex: 0 0 220px;
  max-width: 220px;
}

.student-image {
  width: 100%;
  height: 100%;
  border-radius: 4px;
  object-fit: cover;
  display: block;
}

.content-wrapper {
  flex: 1 1 0;
  display: flex;
  flex-direction: column;
}

.student-name {
  font-size: 1.6rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
  color: #3d3d3d;
}

.pull-quote {
  font-size: 1.1rem;
  line-height: 1.6;
  color: #333333;
  margin: 0 0 0.75rem 0;
}

.read-more-btn {
  align-self: flex-start;
  background-color: #e7e3d5;
  color: #4b2e83;
  border: none;
  padding: 0.6rem 1.4rem;
  border-radius: 3px;
  font-weight: 600;
  font-size: 0.95rem;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  margin-top: 0;
}

.read-more-btn:hover {
  background-color: #dcd6c4;
}

@media (max-width: 768px) {
  .card-inner {
    flex-direction: column;
    padding: 1.25rem 1.5rem 1.5rem;
  }

  .image-wrapper {
    flex: 0 0 auto;
    max-width: 100%;
  }

  .student-image {
    max-height: 260px;
  }

  .student-name {
    margin-top: 0.75rem;
  }
}
</style>
