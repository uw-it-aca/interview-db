// interview.vue
// full student interview page

<template>
  <div class="row w-75 mx-auto mb-2 justify-content-center">
    <div class="ps-4">
      <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">Choosing a
        Major</button>
      <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">Coming to
        College</button>
      <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">Self
        Reflection</button>
      <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">Moving
        Forward</button>
    </div>
  </div>

  <div class="row w-75 mx-auto mb-5 pl-5 justify-content-center">
    <div class="ps-4">
      <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">Finding
        Community</button>
      <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">Advice</button>
    </div>
  </div>

  <div class="row w-75 mx-auto mb-5 ps-3">
    <div v-for="story in stories" :key="story.id">
      <p class="display-6 fs-5 mb-5 ps-4 lh-base border-start border-dark border-4">
        {{ story.story }}<b />
      </p>
    </div>
  </div>

  <div class="row justify-content-center mx-auto">
    <div class="col-3 mx-2">
      <StudentCard :first-name="'Amanda'" />
    </div>
    <div class="col-3 mx-2">
      <StudentCard :first-name="'Anna'" />
    </div>
    <div class="col-3 mx-2">
      <StudentCard :first-name="'Caleb'" />
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
  props: {
    studentInfo: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      stories: [],
    };
  },
  methods: {
    async loadData() {
      const response = await get("/api/students/" + this.studentInfo.id + "/");
      this.stories = response.data;
    },
  },
  created() {
    this.loadData();
  },
};
</script>
