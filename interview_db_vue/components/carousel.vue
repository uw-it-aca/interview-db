// carousel.vue
// carousel cards for home page

<template>
  <div class="row justify-content-center">
    <div class="col-9 mx-auto">
      <div class="card overflow-hidden border-0 rounded-0 mx-auto">
        <div class="row g-0">
          <div class="col">
            <img src="../css/quad.png" class="img-fluid embed-responsive-item"
              style="height:100%; width:100%; object-fit:cover;">
          </div>
          <div class="col bg-light p-5" style="height:400px">
            <div class="card-body text-center pt-5">
              <div class="mb-5">
                <h2 class="display-4 fs-3 mb-3">{{ studentInfo.student.first_name }}</h2>
                <h5 class="text-uppercase display-4 fs-6 text-info mx-auto">
                  {{ studentInfo.standing }}
                  <span v-for="major, index in studentInfo.major" :key="major.id">
                    {{ ", " + major.full_title }}
                  </span>
                </h5>
              </div>
              <p><em>"{{ studentInfo.pull_quote }}"</em></p>
            </div>
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
