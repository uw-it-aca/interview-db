// interview.vue
// full student interview page

<template>

  <div class="mt-4">
    {{ studentInfo }}

    <div class="card border-0">
      <div class="row g-0">
        <div class="col-5">
          <img src="../../css/quad.png" class="img-fluid mx-auto d-block" style="object-fit: cover;" />
        </div>
        <div class="col-7 px-5">
          <h2 class="card-title display-6 mb-2 fw-bold">{{ studentInfo.student.first_name }}</h2>
          <div class="border-bottom border-primary">
            <p class="display-4 fs-6 mx-auto pb-4 mb-5">
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
            </p>
            <p class="fs-6 text-end">{{ interviewDate }}</p>
          </div>

          <!-- collection buttons -->
          <div class="border-bottom border-primary">
            <h2 class="text-start fs-5">They talk about...</h2>
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
              <div class="border-bottom border-primary ">
                <p class="display-6 fs-5">
                  {{ story.story }}
                </p>
              </div>
              <div class="ps-4 mb-5 border-start border-white border-4">
                <p class="text-secondary text-end">
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
