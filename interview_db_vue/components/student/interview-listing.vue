// interview-listing.vue // shown on full students page

<template>
  <button
    type="button"
    class="btn-card mt-5"
    style="height:21rem"
    @click="
      $router.push({
        name: 'Students',
        params: {
          id: studentInfo.id,
          singleStudent: JSON.stringify(studentInfo),
        },
      })
    "
  >
    <p class="fs-6 text-end">{{ interviewDate }}</p>
    <div class="card-clickable">
      <div class="row p-0 m-0">
        <div class="col-4 mx-auto ps-4">
          <img src="../../css/blossom.png" class="listing-img" />
        </div>

        <div class="col-8 ps-4 m-0">
          <h2 class="card-title fw-bold display-6 mb-2">
            {{ studentInfo.student.first_name }}
          </h2>
          <div class="row">
            <div class="col-11">
              <p
                class="display-4 fs-6 mx-auto pb-4 border-bottom border-primary"
              >
                <span v-if="studentInfo.standing">
                  {{ studentInfo.standing + ", studying" }}
                </span>
                <span v-else> Studying </span>
                {{ studentInfo.declared_major }}
              </p>
            </div>
            <div class="col-1">
              <i class="bi bi-chevron-right"></i>
            </div>
          </div>
        </div>

        <div class="card-text ps-4">
          <p class="display-6 fs-5">"{{ studentInfo.pull_quote }}"</p>
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
  computed: {
    interviewDate() {
      return new Date(this.studentInfo.date).toLocaleDateString("en-US");
    },
  },
};
</script>
