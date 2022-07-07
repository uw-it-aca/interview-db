// home.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div class="row">
        <div class="col p-5 mb-4 bg-light rounded-3">
          <div class="py-5">
            <h2 class="display-5 fw-bold">Husky Voices</h2>
            <p class="col-8 fs-4">
              Telling the stories of UW Students<br />through authentic,
              personal,<br />spontaneous interviews
            </p>
            <button class="btn btn-primary btn-lg" type="button">
              Example button
            </button>
          </div>
        </div>
      </div>

      <div class="row justify-content-center mb-4">
        <div class="col-3"><StudentCard :first-name="'Amanda'"/></div>
        <div class="col-3"><StudentCard :first-name="'Anna'"/></div>
        <div class="col-3"><StudentCard :first-name="'Caleb'"/></div>
      </div>

      <div class="row">
        <div class="col bg-info p-5">
          <div class="row">
            <div class="col">
              <h2 class="text-center">Our Interviews</h2>
            </div>
          </div>
          <div class="row justify-content-center mb-4">
            <div class="col-3"><h3>01.</h3></div>
            <div class="col-3"><h3>02.</h3></div>
            <div class="col-3"><h3>03.</h3></div>
          </div>
        </div>
      </div>

      <div class="row align-items-md-stretch">
        <div class="col-md-6">
          <div class="h-100 p-5 text-white bg-dark rounded-3">
            <h2>Change the background</h2>
            <p>
              Swap the background-color utility and add a `.text-*` color
              utility to mix up the jumbotron look. Then, mix and match with
              additional component themes and more.
            </p>
            <button class="btn btn-outline-light" type="button">
              Example button
            </button>
          </div>
        </div>
        <div class="col-md-6">
          <div class="h-100 p-5 bg-light border rounded-3">
            <h2>Add borders</h2>
            <p>
              Or, keep it light and add a border for some added definition to
              the boundaries of your content. Be sure to look under the hood at
              the source HTML here as we've adjusted the alignment and sizing of
              both column's content for equal-height.
            </p>
            <button class="btn btn-outline-secondary" type="button">
              Example button
            </button>
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
