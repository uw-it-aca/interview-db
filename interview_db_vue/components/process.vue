// process.vue
// to be shown on home page

<template>
  <div class="card overflow-hidden border-0 rounded-0">
    <img class="card-img rounded-0" src="../css/blossom.png" alt="Image of cherry blossoms">
    <div class="card-img-overlay d-flex flex-column justify-content-center">
      <div class="row justify-content-center">
        <div class="col-9 bg-white py-5 mx-auto">
          <h2 class="text-center my-5 display-4 fs-1">Our Interviews</h2>
          <div class="row justify-content-center mb-5">
            <div class="col-3 text-center mx-4">
              <h4 class="mb-4 display-4 fs-4">01.<br>Meet a stranger</h4>
              <p>We like to go to the HUB and ByGeorge, or the Quad on a sunny day. Bonus points if the student
                isn't wearing headphones.</p>
            </div>
            <div class="col-3 text-center mx-4">
              <h4 class="mb-4 display-4 fs-4">02.<br>Have a chat</h4>
              <p>We work from a bank of questions but we make up others on the fly. We want to hear about your
                experiences at the University.</p>
            </div>
            <div class="col-3 text-center mx-4">
              <h4 class="mb-4 display-4 fs-4">03.<br>Transcribe</h4>
              <p>We take out the "likes" and "ums" to edit for clarity and readability. We share the final
                transcripts on the website.</p>
            </div>
          </div>
          <h5 class="display-4 fs-4 text-center">
            <router-link to="/about">Read more about our process ></router-link>
          </h5>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "ProcessCard",
  components: {},
  data() {
    return {};
  },
  methods: {},
};
</script>
