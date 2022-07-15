// carousel.vue
// carousel cards for home page

<template>
  <div class="card w-50">
    <div class="row">
      <div class="col-2">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png" class="img-fluid">
      </div>
      <div class="col-4 mx-0">
        <div class="card-body text-center">
          <h2 class="fw-normal">{{ firstName }}</h2>
          <h5 class="text-uppercase">{{ year + "," + " " + major }}</h5>

          <p><em>"{{ quote }}"</em></p>
        
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
