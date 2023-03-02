// home.vue

<template>
  <layout :page-title="pageTitle">
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div class="row g-0 mb-4">
        <div class="col-6">
          <div class="card bg-light p-4 mx-auto border-1 border-light">
            <h2 class="display-4 mb-4 fw-bold text-gold">REAL STUDENTS<br>REAL STORIES</h2>
            <p class="mb-4">
              Sharing the stories of UW students through a <br />
              series of authentic and personal interviews.
            </p>
            <button type="button" class="btn btn-purple" @click="$router.push('students')">
              Explore Student Stories >
            </button>
          </div>
        </div>
      </div>

      <div class="card border-0 mb-5">
        <img class="card-img" src="../images/homeimage.png" alt="The quad during cherry blossom season">
        <div class="card-img-overlay text-center justify-content-center">
          <div class="pt-5 row justify-content-center">
            <span class="col-2">
              <h2 class="display-4 fw-bold">874</h2>
              <p>Stories Shared</p>
            </span>
            <span class="col-2">
              <h2 class="display-4 fw-bold">66</h2>
              <p>Students Interviewed</p>
            </span>
          </div>
        </div>
      </div>

      <div class="row g-0 justify-content-center mb-5">
        <span class="col mx-4">
          <div class="pt-5 ps-5 mx-auto text-center">
            <h2 class="display-4 fw-bold mb-5 text-gold">About Us</h2>
            <p class="mb-4">
              Find out more about who we are, our interview process, and get involved by telling your story!
            </p>
            <button type="button" class="btn btn-purple" @click="$router.push('students')">
              Learn more >
            </button>
          </div>
        </span>
        <span class="col mx-4">
          <div class="pt-5 ps-5 mx-auto text-center">
            <h2 class="display-4 fw-bold mb-5 text-gold">Collections</h2>
            <p class="mb-4">
              Navigate common themes among students on topics such as
              transitioning to college and finding community, and moving forward after graduation.
            </p>
            <button type="button" class="btn btn-purple" @click="$router.push('collections')">
              Browse Collections >
            </button>
          </div>
        </span>
      </div>

    </template>
  </layout>
</template>

<script>
import Layout from "../layout.vue";
import StudentCard from "../components/student/student-card.vue";
import ProcessCard from "../components/process.vue";
import StudentCarousel from "../components/carousel.vue";
import { get } from "axios";

export default {
  name: "PagesHome",
  components: {
    layout: Layout,
    StudentCard,
    ProcessCard,
    StudentCarousel,
  },
  data() {
    return {
      pageTitle: "Home",
      randomStudents: [],
      recentStudents: [],
    };
  },
  created() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const random = await get("api/random/");
      this.randomStudents = random.data;
      const recent = await get("api/recent/");
      this.recentStudents = recent.data;
    },
  },
};
</script>
