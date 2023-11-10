// student-card.vue
// triplet of student interview cards

<template>
  <div class="row justify-content-center">
    <img class="img-fluid p-0" src="../../css/blossom.png"
      style="height: 110px; width: 110px; object-fit:cover; border-radius:50%">
    <div class="card border-0 bg-light" style="position: relative; z-index: -1; bottom: 70px; width: 300px">
      <div class="card-body text-center pt-5">
        <h2 class="card-title fw-normal pt-4">{{ studentInfo.student.first_name }}</h2>
        <h4 class="card-subtitle w-75 text-uppercase display-4 fs-6 text-info mx-auto mb-4">
          {{ studentInfo.standing }}
          <span v-for="major in studentInfo.major" :key="major.id">
            {{ ", " + major.full_title }}
          </span>
        </h4>

        <p class="card-text mb-4 display-6 fs-6 px-4">"{{ studentInfo.pull_quote }}"</p>
        <p class="card-text mb-2 display-6 fs-6">
          <router-link
            :to="{ name: 'Students', params: { id: studentInfo.id, singleStudent: JSON.stringify(studentInfo) } }"
            class="active-link" style="color: #5f5f5f">Read full interview >
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StudentCard",
  props: {
    studentInfo: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {};
  },
  methods: {},
};
</script>
