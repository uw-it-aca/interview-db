// student-card.vue
// triplet of student interview cards to show on home page

<template>
  <div class="card border-0 rounded-0 bg-light">
    <img src="../../css/blossom.png" class="img-fluid mx-auto" style="border-radius:50%; height:95px; width:95px; object-fit:cover;">
    <div class="text-center">
      <h2 class="fw-normal">{{ firstName }}</h2>
      <h4 class="w-75 text-uppercase display-4 fs-6 text-info mx-auto">{{ year + "," + " " + major }}</h4>

      <p class="mx-4">"{{ quote }}"</p>
      
      <p><a class="btn btn-secondary" href="#">Read full story ></a></p>
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
      default: "Some quote about really cool things wow I want to make games for other people so they can enjoy them too"
    },
  },
  data() {
    return {};
  },
  methods: {},
};
</script>
