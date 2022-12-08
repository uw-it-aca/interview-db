// interview-listing.vue 
// shown on students page

<template>
  <button type="button" class="btn-card"
    @click="$router.push({ name: 'Students', params: { id: studentInfo.id, singleStudent: JSON.stringify(studentInfo) } })">
    <div class="card-clickable">
      <div class="card-body">
        <div class="row mb-4">
          <div class="col-3">
            <img src="../../css/doorway.png" class="img-fluid mx-auto d-block" style="
              height: 150px;
              width: 150px;
              object-fit: cover;" />
          </div>
          <div class="col-9">
            <div class="mb-3 px-3 ">
              <h2 class="card-title display-6 mb-2">{{ studentInfo.student.first_name }}</h2>
              <p class="display-4 fs-6 mx-auto pb-4 mb-5 border-bottom border-primary">
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
          </div>

          <div class="card-text mt-5">
            <p class="display-6 fs-5">"{{ studentInfo.pull_quote }}"</p>
          </div>
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
