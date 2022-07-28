// student-card.vue
// triplet of student interview cards

<template>
  <div class="row justify-content-center">
      <img class="img-fluid p-0" 
      src="../../css/blossom.png"
      style="height: 110px; width: 110px; object-fit:cover; border-radius:50%">
    <div class="card border-0 rounded-0 bg-light" style="position: relative; z-index: -1; bottom: 50px; width: 300px">
      <div class="card-body text-center pt-5">
        <h2 class="card-title fw-normal pt-3">{{ firstName }}</h2>
        <h4 class="card-subtitle w-75 text-uppercase display-4 fs-6 text-info mx-auto mb-4">{{ year + "," + " " + major }}</h4>

        <p class="card-text mb-4">"{{ quote }}"</p>
        <p>
          <router-link to="/students/interview/" class="active-link" style="color: #5F5F5F">Read full story ></router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StudentCard",
  props: {
    firstName: {
      type: String,
      required: true,
      default: "Joe",
    },
    year: {
      type: String,
      required: true,
      default: "Freshman",
    },
    major: {
      type: Array,
      required: true,
      default: "Communications",
    },
    quote: {
      type: String,
      required: true,
      default: "Some quote about really cool things"
    },
  },
  data() {
    return {};
  },
  methods: {},
};
</script>
