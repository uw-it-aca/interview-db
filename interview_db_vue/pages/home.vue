// home.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div class="row">
        <div class="col p-5 mb-4 bg-info">
          <div class="py-5">
            <h2 class="display-5 fw-bold text-center">Husky Voices</h2>
            <h5 class="text-center">
              Telling the stories of UW Students<br />through authentic,
              personal,<br />spontaneous interviews
            </h5>
          </div>
        </div>
      </div>

      <div class="row justify-content-center mb-4">
        <div class="col-3"><StudentCard :first-name="'Amanda'"/></div>
        <div class="col-3"><StudentCard :first-name="'Anna'"/></div>
        <div class="col-3"><StudentCard :first-name="'Caleb'"/></div>
      </div>

      <div class="container">
        <div class="row">
          <!-- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png" alt=""> -->
          <div class="col bg-info p-5">
            <div class="row">
              <div class="col">
                <h2 class="text-center mb-4">Our Interviews</h2>
              </div>
            </div>
            <div class="row justify-content-center mb-4">
              <div class="col-3 text-center mb-2">
                <h4 class="mb-4">01.<br>Meet a stranger</h4>
                <p>We like to go to the HUB and ByGeorge, or the Quad on a sunny day. Bonus points if the student isn't wearing headphones</p>
              </div>
              <div class="col-3 text-center mb-2">
                <h4 class="mb-4">02.<br>Have a chat</h4>
                <p>We work from a bank of questions but we make up others on the fly. We want to hear about your experiences at the University.</p>
              </div>
              <div class="col-3 text-center mb-2">
                <h4 class="mb-4">03.<br>Transcribe</h4>
                <p>We take out the "likes" and "ums" to edit for clarity and readability. We share the final transcripts on the website.</p>
              </div>
            </div>
            <h5 class="text-center"><router-link to="/about">Read more about our process ></router-link></h5>
          </div>
        </div>
      </div>

      <div class="row justify-content-center mb-4 text-center">
        <div class="col-4">
          <router-link to="/students"></router-link>
          <div class="h-100 p-3 bg-light">
            <div class="pb-5">
              <p class="mb-1">Filter interviews by</p>
              <h2>Student</h2>
            </div>
            <p class="mx-2">
              Filter student interviews by major, year, or characteristics
            </p>
          </div>
        </div>
        <div class="col-4">
          <router-link to="/collections"></router-link>
          <div class="h-100 p-3 bg-light">
            <div class="pb-5">
              <p class="mb-1">Read a</p>
              <h2>Collection</h2>
              </div>
            <p class="mx-2">
              Stories from diverse students with similar themes
            </p>
          </div>
        </div>
      </div>

    </template>
  </layout>
</template>

<script>
import Layout from "../layout.vue";
import StudentCard from "../components/student-card.vue";

export default {
  name: "PagesHome",
  components: {
    layout: Layout,
    StudentCard,
  },
  data() {
    return {
      pageTitle: "Home",
    };
  },
  methods: {},
};
</script>
