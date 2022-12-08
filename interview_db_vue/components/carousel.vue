// carousel.vue
// carousel cards for home page

<template>
  <div class="row justify-content-center d-flex">
    <div class="col-9 mb-3 d-flex align-items-stretch">
      <div class="card overflow-hidden d-flexborder-primary mx-5 h-100">
        <div class="row g-0">
          <div class="col">
            <img src="../css/quad.png" class="img-fluid embed-responsive-item"
              style="height:100%; width:100%; object-fit:cover;">
          </div>
          <div class="col bg-light p-5">
            <div class="card-body">
              <div class="mb-4">
                <h2 class="display-5 mb-3 fw-bold">{{ studentInfo.student.first_name }}</h2>
                <p class="display-4 fs-6 mx-auto pb-4 mb-3 border-bottom border-primary">
                  <span v-if="studentInfo.standing">
                    {{ studentInfo.standing + ", studying" }}
                  </span>
                  <span v-else>
                    Studying
                  </span>
                  <span v-for="major, index in studentInfo.major" :key="major.id">
                    <span v-if="index != 0">, </span>
                    {{ major.full_title }}
                  </span>
                </p>
              </div>
              <div class="mb-5" v-if="studentInfo.pull_quote != 0">
                <img src="../css/openquote.svg" />
                <p class="my-2">{{ studentInfo.pull_quote }}</p>
                <img src="../css/closequote.svg" class="ms-5 ps-5 float-end" />
              </div>
              <button type="button" class="btn btn-secondary"
                @click="$router.push({ name: 'Students', params: { id: studentInfo.id, singleStudent: JSON.stringify(studentInfo) } })">
                Read {{ studentInfo.student.first_name }}'s Story >
              </button>
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
