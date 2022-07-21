// home.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div class="card overflow-hidden border-0 rounded-0 mb-5">
        <img class="card-img rounded-0" src="../css/quad.png" alt="Image of UW quad">
        <div class="card-img-overlay d-flex flex-column justify-content-center">
          <div class="row justify-content-center text-center text-white">
            <h2 class="display-5 fw-bold mb-4"><em>Husky Voices</em></h2>
            <h6 class="display-4 fs-4">
              Telling the stories of UW Students<br />through authentic,
              personal,<br />spontaneous interviews
            </h6>
          </div>
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

      <div class="row mb-5">
        <ProcessCard />
      </div>

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
      </div>

      <div class="row justify-content-center">
        <div id="carouselExampleControls" class="carousel slide justify-content-center mx-auto" data-bs-ride="carousel">
          <div class="carousel-inner justify-content-cente mx-auto">
            <div class="carousel-item active justify-content-center">
              <StudentCarousel :first-name="'Kevin'" class="d-block justify-content-center mx-auto" />
            </div>
            <div class="carousel-item">
              <StudentCarousel :first-name="'Kevin'" />
            </div>
            <div class="carousel-item">
              <StudentCarousel :first-name="'Kevin'" />
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
    };
  },
  methods: {},
};
</script>
