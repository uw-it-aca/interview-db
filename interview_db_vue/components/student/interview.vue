// interview.vue
// full student interview page

<template>
  <div class="row w-75 mx-auto mb-5">
    <div class="col-3 justify-content-center">
      <img src="../../css/quad.png" class="img-fluid" style="
              border-radius: 50%;
              height: 150px;
              width: 150px;
              object-fit: cover;" />
    </div>
    <div class="col-9 justify-content-start">
      <h2 class="display-4">{{ firstName }}</h2>
      <h5 class="display-3 fs-2 text-info text-uppercase">{{ year + ", " + major }}</h5>
    </div>

    <div>
      <p>I'm a freshman here</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Interview",
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
