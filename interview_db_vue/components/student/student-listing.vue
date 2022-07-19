// student-listing.vue
// listings to be shown on Collection Page on one topic 
// and full student interviews page

<template>
  <div class="card w-50 mb-5 rounded-0">
    <div class="card-body">
      <div class="row g-0">
        <div class="col-2">
          <img src="../../css/quad.png"
          class="img-fluid"
          style="border-radius:50%; height:70px; width:70px; object-fit:cover;">
        </div>
        <div class="col-9">
            <div class="mb-3">
              <h2 class="card-title display-3 fs-2 mb-1">{{ firstName }}</h2>
              <p class="card-subtitle text-uppercase display-6 fs-6 text-info">{{ major + "," + " " + year }}</p>
            </div>
            <p class="card-text display-4 fs-4">"{{ quote }}"</p>
            <p class="card-text mb-2"><router-link to="/">Read full interview ></router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StudentListing",
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
