// carousel.vue
// carousel cards for home page

<template>
  <div>
    <div class="card w-75 overflow-hidden border-0 rounded-0 mx-auto">
      <div class="row g-0">
        <div class="col-4">
          <img src="../css/quad.png"
          class="img-fluid embed-responsive-item" style="height:100%; width:100%; object-fit:cover;">
        </div>
        <div class="col-5 bg-light p-5">
          <div class="card-body text-center">
            <div class="mb-4">
              <h2 class="display-4 fs-3 mb-1">{{ firstName }}</h2>
              <h5 class="text-uppercase display-4 fs-6 text-info mx-auto">{{ major + "," + " " + year }}</h5>
            </div>
            <p><em>"{{ quote }}"</em></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StudentCarousel",
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
