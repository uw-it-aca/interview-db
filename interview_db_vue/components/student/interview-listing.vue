// interview-listing.vue 
// shown on students page

<template>
  <div class="card mb-5 border-0 rounded-0">
    <div class="card-body">
      <div class="row g-0">
        <div class="col-2">
          <img src="../../css/doorway.png" class="img-fluid mx-auto d-block" style="
              border-radius: 50%;
              height: 75px;
              width: 75px;
              object-fit: cover;
            " />
        </div>

        <div class="col-9 pe-5">
          <div class="mb-3 px-3">
            <h2 class="card-title display-6 mb-2">{{ studentInfo.student.first_name }}</h2>
            <p class="card-subtitle text-uppercase display-6 fs-5 text-info">
              {{ studentInfo.standing }}
              <span v-for="major, index in studentInfo.major" :key="major.id">
                {{ ", " + major.full_title }}
              </span>
            </p>
          </div>
          <div class="mb-3 px-3">
            <p class="card-text display-6 fs-3">"{{ studentInfo.pull_quote }}"</p>
            <p class="card-text display-6 fs-5 mb-2">
              <router-link
                :to="{ name: 'Students', params: { id: studentInfo.id, singleStudent: JSON.stringify(studentInfo) } }"
                class="active-link" style="color: #5f5f5f">Read full interview >
              </router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StudentListing",
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
