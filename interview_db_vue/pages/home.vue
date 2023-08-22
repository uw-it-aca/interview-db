// home.vue

<template>
  <layout :page-title="pageTitle">
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div class="row g-0 mb-5" style="background: linear-gradient(#FBFBFB, #f8f9fa)">
        <div class="col-12 col-md-6 col-lg-5 col-xl-5 d-flex align-items-center justify-content-start">
          <div class="card bg-light p-4 mx-auto my-4 border-1 border-light shadow">
            <div class="card-body">
              <h2 class="display-5 mb-4 fw-bold text-gold">REAL STUDENTS<br>REAL STORIES</h2>
              <p class="mb-4">
                Sharing the stories of UW students through a series of authentic and personal interviews.
              </p>
              <button type="button" class="btn btn-purple" @click="$router.push('students')">
                Explore Student Stories <i class="bi bi-chevron-right"></i>
              </button>
            </div>
          </div>
        </div>
        <div class="col-12 col-lg-7 col-md-6 col-xl-7 pr-2 justify-content-center">
          <div class="row justify-content-center mx-auto my-auto">
            <div id="carousel" class="h-100 carousel slide justify-content-center mx-auto col-12 col-lg-8" data-bs-ride="carousel">
              <div class="carousel-inner justify-content-center mx-auto">
                <div v-for="student, index in randomStudents" :key="student.id">
                  <div v-if="index == 0" class="carousel-item active justify-content-center">
                    <InterviewListing :interviewInfo="student" :carousel=true class="h-100 justify-content-center mx-auto" />
                  </div>
                  <div v-else class="carousel-item justify-content-center">
                    <InterviewListing :interviewInfo="student" :carousel=true class="h-100 justify-content-center mx-auto" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="card border-0 mb-5">
        <img class="home-img" src="../images/homequad.png" alt="The quad during cherry blossom season">
        <div class="card-img-overlay text-center justify-content-center">
          <div class="pt-2 row justify-content-center">
            <span class="col-md-2 col-6">
              <h2 class="text-gold display-4 fw-bold">{{ studentCount }}</h2>
              <p class="text-gold fw-bold">Students Interviewed</p>
            </span>
            <span class="col-md-2 col-6">
              <h2 class="text-gold display-4 fw-bold">{{ storyCount }}</h2>
              <p class="text-gold fw-bold">Stories Shared</p>
            </span>
          </div>
        </div>
      </div>

      <div class="row g-0 justify-content-center mb-5">
        <div class="col-md-4 col-12 mx-5 pt-5 text-center">
          <h2 class="display-4 fw-bold mb-5 text-gold">About Us</h2>
          <p class="mb-4">
            Find out more about who we are, our <br> interview process, and get involved by telling <br> your story!
          </p>
          <button type="button" class="btn btn-purple justify-content-end" @click="$router.push('about')">
            Learn more <i class="bi bi-chevron-right"></i>
          </button>
        </div>
        <div class="col-md-4 col-12 pt-5 mx-5 text-center">
          <h2 class="display-4 fw-bold mb-5 text-gold">Collections</h2>
          <p class="mb-4">
            Navigate common themes among students on topics such as<br>
            transitioning to college, finding community, and <br> moving forward after graduation.
          </p>
          <button type="button" class="btn btn-purple" @click="$router.push('collections')">
            Browse Collections <i class="bi bi-chevron-right"></i>
          </button>
        </div>
      </div>

    </template>
  </layout>
</template>

<script>
import Layout from "../layout.vue";
import InterviewListing from "../components/student/interview-listing.vue";
import { get } from "axios";

export default {
  name: "PagesHome",
  components: {
    layout: Layout,
    InterviewListing,
  },
  props: {
  },
  data() {
    return {
      pageTitle: "Home",
      randomStudents: [],
      storyCount: 0,
      studentCount: 0,
    };
  },
  created() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const random = await get("/api/random/");
      this.randomStudents = random.data;
      const students = await get("/api/students/count/");
      this.studentCount = students.data;
      const stories = await get("/api/stories/count/");
      this.storyCount = stories.data;
    },
  },
};
</script>

<style>
img.home-img {
  height: 500px;
  object-fit: cover;
}
</style>