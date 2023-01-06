// interview.vue
// full individual student interview page

<template>

  <div class="mt-4 pt-4">
    <!-- {{ studentInfo }} -->

    <div class="card border-0">
      <div class="row g-0 mx-auto">
        <div class="col-5">
          <img src="../../css/quad.png" class="img-fluid mx-auto d-block" />
        </div>
        <div class="col-7 p-5">
          <h2 class="card-title display-6 mb-2 fw-bold">{{ studentInfo.student.first_name }}</h2>
          <div class="row">
            <div class="col">
              <span v-if="studentInfo.standing">
                {{ studentInfo.standing + ", studying" }}
              </span>
              <span v-else>
                Studying
              </span>
              <span v-for="major, index in studentInfo.major" :key="major.id">
                <span v-if="index != 0">, </span>
                {{ major.full_title }}
              </span>
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
    },
    interviewDate() {
      return new Date(this.studentInfo.date).toLocaleDateString('en-US');
    }
  },
  props: {
    studentInfo: {
      type: Object,
      required: true,
    },
  },
  //   collections: {
  //     type: Object,
  //     required: false,
  //   }
  // },
  data() {
    return {
      stories: [],
    }
  },
  methods: {
    async loadData() {
      const response = await get("/api/students/" + this.interviewId + "/");
      this.stories = response.data;
    }
  },
  created() {
    this.loadData();
  }
};
</script>
