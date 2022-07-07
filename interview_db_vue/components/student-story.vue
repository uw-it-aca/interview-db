// student-story.vue
// to be shown on Collection Page on one topic

<template>
  <div>
    <h1>{{ Name }}</h1>
  </div>
  <div>
    <h5>{{ Grade, Major}}</h5>
  </div>
</template>

<script>
export default {
  name: "StudentStory",
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
