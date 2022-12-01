// carousel.vue
// carousel cards for home page

<template>
  <div class="row justify-content-center">
    <div class="col-9 mx-auto">
      <div class="card overflow-hidden rounded-0 border-primary mx-auto h-100">
        <div class="row g-0">
          <div class="col">
            <img src="../css/quad.png" class="img-fluid embed-responsive-item"
              style="height:100%; width:100%; object-fit:cover;">
          </div>
          <div class="col bg-light p-5">
            <div class="card-body">
              <div class="mb-4">
                <h1 class="display-5 mb-3 fw-bold">{{ studentInfo.student.first_name }}</h1>
                <p class="display-4 fs-6 mx-auto pb-4 mb-5 border-bottom border-primary">
                  {{ studentInfo.standing + ", studying "}}
                  <span v-for="major, index in studentInfo.major" :key="major.id">
                    {{ major.full_title }}
                  </span>
                </p>
              </div>
              <p class="mt-2">{{ studentInfo.pull_quote }}</p>
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
