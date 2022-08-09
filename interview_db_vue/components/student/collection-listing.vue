// collection-listing.vue 
// listings to be shown on topic page

<template>
  <div class="card mb-5 border-0 rounded-0">
    <div class="card-body">
      <div class="row g-0 px-4 justify-content-center">
        <div class="col-2">
          <img src="../../css/quad.png" class="img-fluid mx-auto d-block" style="
              border-radius: 50%;
              height: 80px;
              width: 80px;
              object-fit: cover;
            " />
        </div>

        <div class="col-9 border-start border-dark border-4">
          <div class="px-3">
            <div class="mb-4 px-3">
              <h2 class="card-title display-6 mb-2">{{ studentInfo.student.first_name }}</h2>
              <p class="card-subtitle text-uppercase display-6 fs-5 text-info">
              <div v-for="major in studentInfo.major" :key="major.id">
                {{ major.full_title + ", "}}
              </div>
              {{ studentInfo.standing }}
              </p>
            </div>
            <div class="mb-3 px-3">
              <p class="card-text lh-base display-6 fs-4">"{{ story }}"</p>
              <p class="card-text display-6 fs-5 mb-2">
                <router-link to="/students/1234" class="active-link" style="color: #5f5f5f">Read full interview >
                </router-link>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CollectionListing",
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
