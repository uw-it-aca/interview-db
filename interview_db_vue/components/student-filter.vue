// student-filter.vue
// to filter student interviews

<template>
  <div class="card" style="width: 25rem;">
    <h2 class="card-header fw-bold fs-3">Filter Stories</h2>
    <div class="card-body">
      <div class="mb-4">
        <p class="display-4 fw-bold fs-5 mb-0" data-bs-toggle="collapse" href="#year" aria-expanded="false"
          aria-controls="year">
          Student Year
        </p>
        <div class="collapse mt-0" id="year">
          <div class="card card-body border-0">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                Freshman
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                Sophomore
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                Junior
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                Senior
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                Alumni
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                Masters
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                PhD
              </label>
            </div>
          </div>
        </div>
      </div>

      <div class="mb-4">
        <p class="display-4 fs-5 fw-bold mb-0" data-bs-toggle="collapse" href="#major" aria-expanded="false"
          aria-controls="major">
          Major
        </p>
        <div class="collapse" id="major">
          <div class="card card-body border-0 mt-0">
            <div v-for="major in majors" :key="major.id">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                  {{ major.full_title }}
                </label>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- <div class="mb-4">
        <p class="display-4 fs-5 mb-0" data-bs-toggle="collapse" href="#traits" aria-expanded="false"
          aria-controls="traits">
          Student Traits
        </p>
        <div class="collapse" id="traits">
          <div class="card card-body border-0 mt-0">
            <div v-for="trait in traits" :key="trait.id">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" :value="trait" id="trait" v-model="checkedFilters"
                  @change="onClick($event)">
                <label class="form-check-label display-6 fs-6" for="trait.id">
                  {{ trait.type }}
                  {{ checkedFilters }}
                </label>
              </div>
            </div>
          </div>
        </div>
      </div> -->

      <div class="mb-4">
        <p class="display-4 fs-5 fw-bold mb-0" data-bs-toggle="collapse" href="#collections" aria-expanded="false"
          aria-controls="collections">
          Story Collection
        </p>
        <div class="collapse" id="collections">
          <div class="card card-body border-0 mt-0">
            <div v-for="topic in topics" :key="topic.id">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                  {{ topic.topic }}
                </label>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { get } from "axios";
export default {
  name: "StudentFilter",
  props: {},
  data() {
    return {
      checkedFilters: [],
      majors: [],
      traits: [],
      topics: [],
    };
  },
  methods: {
    async loadData() {
      const response = await get('api/majors/');
      this.majors = response.data;
      const types = await get('api/types/');
      this.traits = types.data;
      const collections = await get('api/collections/');
      this.topics = collections.data;
    },
    onClick(event) {
      this.$emit('clicked', this.checkedFilters)
    }
  },
  created() {
    this.loadData();
  }
};
</script>