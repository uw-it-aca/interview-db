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
          <img class="banner-image" src="../images/aboutUsImage.png"/>
          <div class="title-div">
            <h1 class="text-gold fw-bold display-5 mb-0">About Us</h1>
          </div>
        </div>
        <div class="mx-auto p-5">
          <div class="mx-auto mb-5">
            <h2 class="text-purple fw-bold mb-4">What is Husky Voices</h2>
            <p>
              Husky Voices is a growing collection of UW student interviews that highlight the diverse experiences of our undergraduate student body. 
            </p>
            <p>
              Interviews are collected, edited, and published by student researchers from UWIT's Student Educational Technology Services (SETS) unit. 
            </p>
          </div>

          <div class="mx-auto pt-2 mb-5">
            <h2 class="text-purple fw-bold mb-4">Our Mission</h2>
            <p>Husky Voices helps students find 
              <strong>direction, support, and inspiration</strong> through the 
              <strong>stories of their fellow students</strong> 
              while helping UW decision makers better understand and support students.</p>
          </div>

          <div class="mx-auto pt-2 mb-5">
            <h2 class="text-purple fw-bold mb-4">What We Learn by Listening</h2>
            <p>
              At UWIT, we're committed to designing technology services that reflect and support 
              the real needs of students. Husky Voices was created to allow student stories to 
              inform the development of UW technology and support services.
            </p>
            <p>
              Instead of relying solely on abstract data, we talk directly with students to pair 
              this data with personal experiences. Student stories help us discover new problem areas,
              give context to the data, and keep our understanding of student life current.
            </p>
            <p>
              Unlike formal research that focuses on what we want to understand, we take inspiration
              from interviewers and oral historians like Brandon Stanton, Studs Terkel, and Linda Shopes,
              who let the interviewees lead the conversation. Through this methodology, we give students
              space to share their current challenges, successes, and hopes in their own words. With a 
              broader understanding of the student experience, we can better design our services to meet
              students where they are and support them where it matters most.
            </p>

            <ul class="list-unstyled">
              <li>Learn more about the interviewers who inspired our process:</li>
              <li><a href="https://brandonstanton.com/humans-of-new-york">
                 Humans of New York - Brandon Stanton</a></li>
              <li><a href="https://www.amazon.com/Studs-Terkel-Listening-Eric-Simonson/dp/B01MY8YT86/ref=sr_1_26?s=movies-tv&ie=UTF8&qid=1512188629&sr=1-26&keywords=hbo+movies&refinements=p_n_format_browse-bin%3A2650306011">
                 Talking to America - Studs Terkel</a></li>
              <li><a href="https://orbiscascade-washington.primo.exlibrisgroup.com/permalink/01ALLIANCE_UW/1juclfo/alma99326078421501451">
                 The Oral History Reader [UW Library, digital access]</a></li>
            </ul>

            <ul class="list-unstyled">
              <li>Understand the process we use to edit interviews:</li>
              <li><a href="https://www.oralhistoryforum.ca/index.php/ohf/article/view/385/index.html">
                Editing Oral History for Publication - Linda Shopes</a></li>
            </ul>
          </div>

          <div class="mx-auto pt-2 mb-5">
            <h2 class="text-purple fw-bold mb-4">
              Frequently Asked Questions
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
