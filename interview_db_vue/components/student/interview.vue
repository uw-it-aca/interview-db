// interview.vue
// full individual student interview page

<template>
  <div class="interview-page">
    <div class="interview-card" v-if="interviewInfo && studentInfo">
      <!-- Main body: image + content -->
      <div class="interview-body">
        <div class="interview-image-wrapper">
          <img
            v-if="image"
            :src="image"
            class="interview-image"
            :alt="altText"
          />
          <img
            v-else
            src="../../images/placeholder.png"
            class="interview-image"
            alt="placeholder image"
          />
        </div>

        <div class="interview-content">
          <!-- Name + meta -->
          <h1 class="interview-name">
            {{ studentInfo.first_name }}
          </h1>

          <div class="interview-meta">
            <span class="interview-meta-main">
              <span v-if="interviewInfo.standing">
                {{ interviewInfo.standing + ", studying" }}
              </span>
              <span v-else>
                Studying
              </span>
              {{ " " + interviewInfo.declared_major }}
            </span>
            <span class="interview-meta-date">
              {{ interviewDate }}
            </span>
          </div>

          <!-- Topics filter row -->
          <div class="interview-topics">
            <p class="interview-topics-label">They talk about...</p>
            <div class="interview-topics-chips">
              <span v-for="topic in topics" :key="topic.id">
                <input
                  type="checkbox"
                  class="btn-check"
                  :id="topic.id"
                  :value="topic.topic"
                  v-model="filters"
                  autocomplete="off"
                />
                <label class="topic-chip" :for="topic.id">
                  {{ topic.topic }}
                </label>
              </span>
              <button
                v-if="filters && filters.length > 0"
                type="button"
                class="interview-clear-filters"
                @click="clearFilters"
              >
                Clear all
              </button>
            </div>
          </div>

          <!-- Stories -->
          <div class="interview-stories">
            <div
              v-for="story in filteredStories"
              :key="story.id"
              class="interview-story"
            >
              <p class="interview-story-text">
                {{ story.story }}
              </p>
              <p
                class="interview-story-topics"
                :class="mq.mobile ? 'text-start' : 'text-end'"
              >
                <span v-for="collection in story.topics" :key="collection.id">
                  <router-link
                    :to="{ name: 'Collections', params: { id: collection.id } }"
                    class="active-link"
                  >
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

    <!-- Loading state -->
    <div v-else class="interview-loading">
      Loading interview data...
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Interview",
  inject: ["mq"],
  components: {
  },
  computed: {
    interviewId() {
      const id = this.$route.params.id;
      if (!id || id === 'students') {
        return null;
      }
      const numId = parseInt(id, 10);
      if (isNaN(numId) || numId <= 0) {
        return null;
      }
      return numId;
    },
    filteredStories() {
      this.filtered = this.stories;
      // consider changing to AND filters, not OR
      if (this.filters !== undefined && this.filters.length > 0) {
        const included = (collection) => this.filters.includes(collection.topic)
        this.filtered = this.filtered.filter(story => story.topics.some(included))
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
  watch: {
    '$route.params.id': {
      handler() {
        if (this.interviewId) {
          this.loadData();
        }
      }
    }
  },
  methods: {
    async loadData() {
      let response;
      try {
        response = await axios.get("/api/students/" + this.interviewId + "/");
        // Check if response is HTML (error page) instead of JSON
        if (typeof response.data === 'string' && response.data.trim().startsWith('<!DOCTYPE')) {
          return;
        }
      } catch (error) {
        return;
      }
      this.stories = response.data;
      if (!Array.isArray(this.stories) || this.stories.length === 0 || !this.stories[0]?.interview) {
        return;
      }
      this.interviewInfo = this.stories[0].interview;
      if (!this.interviewInfo?.student) {
        return;
      }
      this.studentInfo = this.interviewInfo.student;
      this.interviewDate = new Date(this.interviewInfo.date).toLocaleDateString('en-US');

      // get all topics mentioned in this interview
      const topics = await axios.get("/api/students/" + this.interviewId + "/topics/");
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
        const blob = await axios.get("/api/students/" + this.interviewInfo.id + "/image/", { responseType: 'blob' });
        this.image = URL.createObjectURL(blob.data);
      } catch (err) {
        // Image not available or failed to load
      }
    },
    clearFilters() {
      this.filters = [];
    }
  },
  created() {
    if (this.interviewId) {
      this.loadData();
    }
  },
};
</script>

<style scoped>
.interview-page {
  padding: 2rem 0;
}

.interview-card {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.12);
  overflow: hidden;
}

.interview-body {
  display: flex;
  flex-direction: row;
  gap: 2rem;
  padding: 2rem;
}

.interview-image-wrapper {
  flex: 0 0 320px;
  max-width: 320px;
}

.interview-image {
  width: 100%;
  height: 100%;
  max-height: 460px;
  border-radius: 4px;
  object-fit: cover;
  display: block;
}

.interview-content {
  flex: 1 1 0;
  display: flex;
  flex-direction: column;
}

.interview-name {
  font-size: 2rem;
  font-weight: 700;
  color: #3d3d3d;
  margin-bottom: 0.25rem;
}

.interview-meta {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 0.5rem;
  font-size: 0.95rem;
  color: #555555;
  margin-bottom: 1.5rem;
}

.interview-meta-main {
  font-weight: 500;
}

.interview-meta-date {
  font-size: 0.9rem;
}

.interview-topics {
  border-top: 1px solid #e0e0e0;
  padding-top: 1rem;
  margin-bottom: 1.5rem;
}

.interview-topics-label {
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.interview-topics-chips {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
}

.topic-chip {
  display: inline-flex;
  align-items: center;
  background-color: #6b4ba8;
  color: #ffffff;
  font-size: 0.85rem;
  padding: 0.3rem 0.9rem;
  border-radius: 24px;
  font-weight: 550;
  cursor: pointer;
}

.btn-check:checked + .topic-chip {
  background-color: #4b2e83;
}

.interview-clear-filters {
  border: none;
  background: none;
  color: #6b4ba8;
  font-size: 0.9rem;
  font-weight: 500;
  text-decoration: underline;
  padding: 0.25rem 0.5rem;
}

.interview-stories {
  border-top: 1px solid #e0e0e0;
  padding-top: 1.25rem;
}

.interview-story + .interview-story {
  margin-top: 1.25rem;
  padding-top: 1.25rem;
  border-top: 1px solid #f0f0f0;
}

.interview-story-text {
  font-size: 1rem;
  line-height: 1.7;
  color: #333333;
  margin-bottom: 0.35rem;
}

.interview-story-topics {
  font-style: italic;
  color: #777777;
}

.interview-loading {
  text-align: center;
  padding: 3rem 1rem;
  color: #555555;
}

@media (max-width: 992px) {
  .interview-body {
    flex-direction: column;
    padding: 1.5rem;
  }

  .interview-image-wrapper {
    flex: 0 0 auto;
    max-width: 100%;
  }

  .interview-image {
    max-height: 320px;
  }
}

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
