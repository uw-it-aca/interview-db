// home.vue

<template>
  <layout :page-title="pageTitle">
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div class="card mb-5 mt-0 pt-0 rounded-0 border-primary w-100">
        <div class="row g-0">
          <div class="col-7 pt-5 ps-5">
            <div class="card-body mt-5 pt-5 ps-5 mx-auto">
              <h1 class="display-4 pt-5 mb-4 fw-bold">REAL STUDENTS</h1>
              <h1 class="display-4 mb-4 fw-bold">REAL STORIES</h1>
              <p class="fs-5 mb-4">
                Telling the stories of UW students through a <br/>
                series of authentic and personal interviews.
              </p>
              <button type="button" class="btn btn-secondary">
                <router-link to="/students" class="active-link">Read a Story ></router-link>
              </button>
            </div>
          </div>
          <div class="col-5">
            <img src="../css/homeimage.png" class="img-fluid embed-responsive-item"
              style="height:100%; width:100%; object-fit:cover;" alt="UW Quad on a Fall Day">
          </div>
        </div>
      </div>
<!-- 
      <div class="row justify-content-center mb-5 text-center">
        <div class="col-4 mx-5">
          <router-link to="/students" class="active-link">
            <div class="h-100 p-5 bg-light">
              <div class="py-5 display-4 fs-5">
                <p class="mb-1">Filter interviews by</p>
                <h2 class="display-4 fs-1">Student</h2>
              </div>
              <p class="w-75 mx-auto display-4 fs-5">
                Filter student interviews by major, year, or characteristics
              </p>
            </div>
          </router-link>
        </div>
        <div class="col-4 mx-5">
          <router-link to="/collections" tag="div" class="active-link">
            <div class="h-100 p-5 bg-light">
              <div class="py-5">
                <p class="mb-1 display-4 fs-5">Read a</p>
                <h2 class="display-4 fs-1">Collection</h2>
              </div>
              <p class="w-75 mx-auto display-4 fs-5">
                Stories from diverse students with similar themes
              </p>
            </div>
          </router-link>
        </div>
      </div> -->

      <div class="row justify-content-center">
        <div id="carouselExampleControls" class="carousel slide justify-content-center mx-auto" data-bs-ride="carousel">
          <div class="carousel-inner justify-content-cente mx-auto">
            <div v-for="student, index in randomStudents" :key="student.id">
              <div v-if="index == 0">
                <div class="carousel-item active justify-content-center">
                  <StudentCarousel :studentInfo="student" class="d-block justify-content-center mx-auto" />
                </div>
              </div>
              <div v-else>
                <div class="carousel-item">
                  <StudentCarousel :studentInfo="student"/>
                </div>
              </div>
            </div>
          </div>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls"
            data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
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
    }
  },
};
</script>
