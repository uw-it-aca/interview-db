// carousel.vue
// cards for home page's carousel

<template>
  <button
    type="button"
    class="btn-card mt-5"
    style="height:20rem; width:25rem"
    @click="
      $router.push({
        name: 'Students',
        params: {
          id: studentInfo.id,
        },
      })
    "
  >
    <div class="card-clickable">
      <div class="row p-0 m-0">
        <div class="col-4 mx-auto ps-4">
          <img src="../css/blossom.png" class="listing-img" />
        </div>

        <div class="col-8 ps-4 m-0">
          <h2 class="card-title fw-bold display-6 text-purple mb-2">
            {{ studentInfo.student.first_name }}
          </h2>
          <div class="row">
            <div class="col-11">
              <p class="mx-auto pb-4">
                <span v-if="studentInfo.standing">
                  {{ studentInfo.standing + ", studying" }}
                </span>
                <span v-else> Studying </span>
                {{ studentInfo.declared_major }}
              </p>
            </div>
          </div>
        </div>

        <div class="card-text ps-4 pt-33">
          <p>"{{ studentInfo.pull_quote }}"</p>
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
