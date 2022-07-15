// student-interview.vue
// full student interview page

<template>
  <div>
    <h1>{{ firstName }}</h1>
  </div>
  <div><h5>{{ year }}</h5></div>
</template>

<script>
export default {
  name: "StudentInterview",
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
  data() {
    return {};
  },
  methods: {},
};
</script>
