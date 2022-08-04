// about.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div class="row mb-0">
        <img class="rounded-0" src="../css/doorway.png" alt="Image of UW quad">
      </div>
      <div class="w-75 h-75 py-5 bg-light mx-auto px-5 mb-0" style="position:relative;bottom:300px;">
        <div class="text-center p-5">
          <h2 class="display-6 my-5 py-3">Real Students, Real Stories</h2>
          <h5 class="display-6 fs-3 px-5">We collect the true stories of UW students and<br/>share them with others on campus</h5>
        </div>
      </div>
      <div class="w-75 bg-light mx-auto px-5 mb-5">
        <div class="text-center px-5 py-5">
          <h2 class="display-6 my-5 py-3">Our Team</h2>
          <h5 class="display-6 fs-3 px-5">Our team operates out of the Academic Experience Design and Delivery (AXDD) Department at UW-IT.</h5>
        </div>
      </div>

      <div class="w-75 bg-light mx-auto px-5 mb-5">
        <div class="text-center px-5 py-5">
          <h2 class="display-6 fs-3">Are you interested in adding to our collection?</h2>
        </div>
      </div>

      <div class="row justify-content-center mb-5 text-center">
        <div class="col-4 mx-5">
          <div class="h-100 p-4 bg-light">
            <div class="py-5 display-4 fs-5">
              <p class="mb-1">Volunteer to</p>
              <h2 class="display-4 fs-1">Share Your Story</h2>
            </div>
            <p class="w-75 mx-auto display-4 fs-5">
              Schedule an appointment with an interview to talk about your UW experience and add to our collection.
            </p>
          </div>
        </div>
        <div class="col-4 mx-5">
          <div class="h-100 p-4 bg-light">
            <div class="py-5">
              <p class="mb-1 display-4 fs-5">Help Us</p>
              <h2 class="display-4 fs-1">Collect Interviews</h2>
            </div>
            <p class="w-75 mx-auto display-4 fs-5">
              Partner with us to interview more students on campus.
            </p>
          </div>
        </div>
      </div>

      <div class="w-75 bg-light mx-auto px-5 mb-5">
        <div class="px-5 py-5">
          <h2 class="text-center display-6 my-5">FAQ</h2>
          <p>
            <strong>Q: How do you choose the students you interview?</strong><br/>
            A: We walk around busy spaces like the HUB Cafeteria or By George and look for students who look like they might have a little extra time to talk.<br/><br/>

            <strong>Q: Who conducts these interviews?</strong><br/>
            A: Most interviews are conducted by student staff at UW-IT.<br/><br/>

            <strong>Q: How are the interviews transcribed?</strong><br/>
            A: We make edits for clarity and concision as well as re-organize the conversation to make student stories more readable. We are trained to take special care of conserving the original interviewee intent. 
          </p>
        </div>
      </div>

    </template>
  </layout>
</template>

<script>
import { Card } from "axdd-components";
import Layout from "../layout.vue";

export default {
  name: "PagesAbout",
  components: {
    layout: Layout,
    "axdd-card": Card,
  },
  data() {
    return {
      pageTitle: "About Us",
    };
  },
  methods: {},
};
</script>
