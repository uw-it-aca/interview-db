// about.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div class="row mb-0">
        <img class="d-block" src="../css/about.png" style="z-index: -1" alt="Image of UW quad">
      </div>
      <div class="w-75 h-75 p-5 bg-light mx-auto mb-0 d-block" style="position:relative; bottom:300px;">
        <div class="text-center p-5">
          <h2 class="display-6 py-5">Real Students, Real Stories</h2>
          <h5 class="display-6 fs-3 px-5">We collect the true stories of UW students and<br/>share them with others on campus</h5>
        </div>
      </div>

      <div class="w-75 bg-light mx-auto px-5 mb-5">
        <div class="text-center p-5 mx-auto">
          <h2 class="display-6 mb-5">Who We Are</h2>
          <h5 class="display-6 px-5 fs-3 mb-5">Our team operates out of the Academic Experience Design and Delivery (AXDD) Department at UW-IT.</h5>
          <img class="mb-5" src="../css/team.png" style="z-index: -1" alt="Image of UW quad">
        </div>
      </div>

      <div class="w-75 bg-light mx-auto mb-5">
        <div class="w-50 mx-auto text-center py-5">
          <h2 class="display-6 fs-3 mb-5">Are you interested in adding<br/>to our collection?</h2>
          <p class="display-4 fs-5">
            Schedule a 15-30 minute appointment with an interviewer to talk about your UW experience and add to our collection.
          </p>
        </div>
      </div>

      <div class="w-75 bg-light mx-auto px-5 mb-5">
        <div class="p-5">
          <h2 class="text-center display-6 mb-5">FAQ</h2>
          <p>
            <strong>Q: How do you choose the students you interview?</strong><br/>
            A: We walk around busy spaces like the HUB Cafeteria or By George and look for students who look like they might have a little extra time to talk.<br/><br/>

            <strong>Q: Who conducts these interviews?</strong><br/>
            A: Most interviews are conducted by student staff at UW-IT.<br/><br/>

            <strong>Q: How are the interviews transcribed?</strong><br/>
            A: We make edits for clarity and concision as well as re-organize the conversation to make student stories more readable. We are trained to take special care of conserving the original interviewee intent.<br/><br/>
            
            <strong>Q: How do you ensure data privacy for the students you interview?</strong><br/>
            A: After each interview, we are obliged to give an additional form for the students to complete. This form clarifies whether they only want their information used for internal UW research or if they are willing to release their story to be shared.
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
