// about.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      <h1 class="visually-hidden">{{ pageTitle }}</h1>
    </template>

    <template #content>
      <div>
        <div style="position: relative">
          <img class="card-img" src="../images/aboutUsImage.png"/>
          <div class="card" style="position: absolute; top: 40%">
            <h1 class="display-3 text-gold fw-bold my-4 mx-4">About Us</h1>
          </div>
        </div>
        <div class="mx-auto p-5">
          <div class="pt-5 ps-5 mx-auto mb-5">
            <h2 class= "fs-1 text-gold fw-bold mb-4">Who We Are</h2>
            <p class="mb-4">
              We collect the real stories of UW students and share them with
              others on campus.
            </p>
            <p class="mb-4">
              Our team operates out of the
              <b>Academic Experience Design and Delivery (AXDD)</b> department at
              UW-IT.
            </p>
          </div>


        <div class="mx-auto pt-2 ps-5 mb-5">
          <h2 class="fs-1 text-gold fw-bold mb-4">Our Interview Process</h2>
          <p class="mb-4">1. Meet a stranger</p>
          <p class="mb-4">2. Have a chat</p>
          <p class="mb-4">3. Transcribe and share</p>
        </div>

        <div class="mx-auto pt-2 ps-5 mb-5">
          <h2 class="fs-1 text-gold fw-bold mb-4">Help Grow Our Collection</h2>
          <p class="mb-4">
            Schedule a 15-30 minute appointment with us to talk about your UW
            experience.
          </p>
          <a href="mailto:ux@uw.edu?subject=Husky Voices" title="Husky Voices">
            <button type="button" class="btn btn-purple">
              Share Your Story >
            </button>
          </a>
        </div>

        <div class="mx-auto pt-2 ps-5 mb-5">
          <h2 class="fs-1 text-gold fw-bold mb-4">
            Frequently Asked Questions (FAQ)
          </h2>

          <div class="mx-auto pt-2 mb-5">
            <div class="accordion" id="faq">
              <div class="accordion-item">
                <p class="accordion-header fs-5" id="headingOne">
                  <button
                    class="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#collapseOne"
                    aria-expanded="false"
                    aria-controls="collapseOne"
                  >
                    How do you choose the students you interview?
                  </button>
                </p>
                <div
                  id="collapseOne"
                  class="accordion-collapse collapse"
                  aria-labelledby="headingOne"
                  data-bs-parent="#faq"
                >
                  <div class="accordion-body">
                    <p>
                      We walk around busy spaces like the HUB Cafeteria or By
                      George and look for students who look like they might have
                      a little extra time to talk.
                    </p>
                  </div>
                </div>
              </div>
              <div class="accordion-item">
                <p class="accordion-header fs-5" id="headingTwo">
                  <button
                    class="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#collapseTwo"
                    aria-expanded="false"
                    aria-controls="collapseTwo"
                  >
                    Who conducts these interviews?
                  </button>
                </p>
                <div
                  id="collapseTwo"
                  class="accordion-collapse collapse"
                  aria-labelledby="headingTwo"
                  data-bs-parent="#faq"
                >
                  <div class="accordion-body">
                    <p>
                      Most interviews are conducted by student staff at UW-IT.
                    </p>
                  </div>
                </div>
              </div>
              <div class="accordion-item">
                <p class="accordion-header fs-5" id="headingThree">
                  <button
                    class="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#collapseThree"
                    aria-expanded="false"
                    aria-controls="collapseThree"
                  >
                    How are the interviews transcribed?
                  </button>
                </p>
                <div
                  id="collapseThree"
                  class="accordion-collapse collapse"
                  aria-labelledby="headingThree"
                  data-bs-parent="#faq"
                >
                  <div class="accordion-body">
                    <p>
                      We make edits for clarity and concision as well as
                      re-organize the conversation to make student stories more
                      readable. We are trained to take special care of
                      conserving the original interviewee intent.
                    </p>
                  </div>
                </div>
              </div>
              <div class="accordion-item">
                <p class="accordion-header fs-5" id="headingFour">
                  <button
                    class="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#collapseFour"
                    aria-expanded="false"
                    aria-controls="collapseFour"
                  >
                    How are the interviews transcribed?
                  </button>
                </p>
                <div
                  id="collapseFour"
                  class="accordion-collapse collapse"
                  aria-labelledby="headingFour"
                  data-bs-parent="#faq"
                >
                  <div class="accordion-body">
                    <p>
                      After each interview, we are obliged to give an additional
                      form for the students to complete. This form clarifies
                      whether they only want their information used for internal
                      UW research or if they are willing to release their story
                      to be shared.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      </div>
    </template>
  </layout>
</template>

<script>
import Layout from "../layout.vue";

export default {
  name: "PagesAbout",
  components: {
    layout: Layout,
  },
  data() {
    return {
      pageTitle: "About Us",
    };
  },
  methods: {},
};
</script>
