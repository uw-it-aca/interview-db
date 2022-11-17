// interview.vue
// full student interview page

<template>

  <div class="mt-4">
    <div class="row w-75 mx-auto mb-5">
      <div class="col-3 justify-content-center">
        <img src="../../css/quad.png" class="img-fluid mx-auto d-block" style="
              border-radius: 50%;
              height: 150px;
              width: 150px;
              object-fit: cover;" />
      </div>
      {{ studentInfo }}
      <div class="col-9 justify-content-start py-3">
        <h2 class="display-4">{{ studentInfo.student.first_name }}</h2>
        <h5 class="display-3 fs-3 text-info text-uppercase">
          {{ studentInfo.standing }}
          <span v-for="major in studentInfo.major" :key="major.id">
            {{ ", " + major.full_title }}
          </span>
          <span v-for="trait in studentInfo.student_type" :key="trait.id">
            {{ ", " + trait.type }}
          </span>
        </h5>
      </div>
    </div>

    <div class="row w-75 mx-auto mb-4">
      <div class="col-2 justify-content-center py-2">
        <p class="text-end"><strong>Filtering on:</strong></p>
      </div>
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
    </div>

    <div class="row w-75 mx-auto mb-5 ps-3">
      <div v-for="story in stories" :key="story.id">
        <div class="ps-4 mb-1 border-start border-dark border-4">
          <p class="display-6 fs-5 lh-base">
            {{ story.story }}
          </p>
        </div>
        <div class="ps-4 mb-5 border-start border-white border-4">
          <p class="text-secondary">Collection:
            <span v-for="collection in story.code" :key="collection.id">
              #{{ collection.code }}
            </span>
          </p>
        </div>
      </div>
    </div>

    <div class="row justify-content-center mx-auto">
      <span v-for="student in randomStudents" :key="student.id">
        <div class="col-3 mx-2">
          <StudentCard :studentInfo="student" />
        </div>
      </span>
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
      randomStudents: [],
    }
  },
  methods: {
    async loadData() {
      const response = await get("/api/students/" + this.interviewId + "/");
      this.stories = response.data;
      const random = await get("api/random/");
      this.randomStudents = random.data;
    }
  },
  created() {
    this.loadData();
  }
};
</script>
