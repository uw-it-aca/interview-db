// carousel.vue
// cards for home page's carousel

<template>
  <button
    type="button"
    class="btn-card mt-5"
    style="height: 21rem"
    @click="
      $router.push({
        name: 'Students',
        params: {
          id: studentInfo.id,
        },
      })
    "
  >
    <div class="d-flex card-clickable">
      <div class="row p-0 m-x-0">
        <div class="row p-0 m-0">
          <div class="col-md-5 col-sm-6 col-4 row-xs ps-4 img-div shift-up">
            <img src="../css/quad.png" class="listing-img" />
          </div>

          <div class="col-md-7 col-sm-6  col-8 ps-4 m-0">
            <div class="row">
              <p class="fs-6 text-end">{{ interviewDate }}</p>
              <h2 class="card-title fw-bold text-purple display-6 mb-2">
                {{ studentInfo.student.first_name }}
              </h2>
              <p class="display-4 fs-6 mx-auto pb-4">
                <span v-if="studentInfo.standing">
                  {{ studentInfo.standing + ", studying" }}
                </span>
                <span v-else> Studying </span>
                <span v-for="(major, index) in studentInfo.major" :key="major.id">
                  <span v-if="index != 0">, </span>
                  {{ major.full_title }}
                </span>
              </p>
            </div>
          </div>
        </div>

        <div class="card-text pt-2 px-4 border-top border-primary">
          <p class="display-6 fs-6">"{{ studentInfo.pull_quote }}"</p>
        </div>
        <div class="d-flex justify-content-end">
            <u class="text-purple" style="display:inline;">Read More</u>
            <i class="bi bi-chevron-right"></i>
        </div>
      </div>
    </div>
    
  </button>
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
