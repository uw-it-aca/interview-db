// interview.vue
// full individual student interview page

<template>

  <div>
    <div class="card border-0">
      <div class="row g-0 mx-auto interview-height">
        <div class="col-lg-6 col-12" style="height: inherit;">
          <img src="../../images/placeholder.png" class="img-fluid mx-auto position-sticky" style="height: 100%; object-fit: cover;" />
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
              <span v-for="story in stories" :key="story.id">
                <span v-for="collection in story.code" :key="collection.id">
                  <input type="checkbox" class="btn-check" :id=collection.id autocomplete="off">
                  <label class="btn btn-outline-success m-1" :for=collection.id>
                    {{ collection.code }}
                  </label>
                </span>
              </span>
              <button type="button" class="btn btn-outline-info interview-filter" data-bs-toggle="button" autocomplete="off">
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
import StudentCard from "./student-card.vue";
import { get } from "axios";
export default {
  name: "Interview",
  components: {
    StudentCard,
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
    }
  },
  methods: {
    async loadData() {
      const response = await get("/api/students/" + this.interviewId + "/");
      this.stories = response.data;
      this.interviewInfo = this.stories[0].interview;
      this.studentInfo = this.interviewInfo.student;
      this.interviewDate = new Date(this.interviewInfo.date).toLocaleDateString('en-US');
    }
  },
  created() {
    this.loadData();
  }
};
</script>
