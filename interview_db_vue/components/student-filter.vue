// student-filter.vue
// to filter student interviews

<template>
  <div class="card">
    <h2 class="m-3 fw-bold display-6 text-purple">Filter Stories</h2>
    <div class="card-body">
      <div class="mb-4">
        <p class="display-4 fw-bold fs-5 mb-0" href="#year" aria-expanded="false" aria-controls="year">
          Student Year
        </p>
        <div class="mt-0" id="year">
          <div class="card card-body border-0">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="Freshman" id="Freshman" v-model="filters.year"
                @change="updateQuery($event)">
              <label class="form-check-label display-6 fs-6" for="freshman">
                Freshman
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="Sophomore" id="Sophomore" v-model="filters.year"
                @change="updateQuery($event)">
              <label class="form-check-label display-6 fs-6" for="sophomore">
                Sophomore
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="Junior" id="Junior" v-model="filters.year"
                @change="updateQuery($event)">
              <label class="form-check-label display-6 fs-6" for="Junior">
                Junior
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="Senior" id="Senior" v-model="filters.year"
                @change="updateQuery($event)">
              <label class="form-check-label display-6 fs-6" for="Senior">
                Senior
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="Alumni - undergrad" id="Alumni"
                v-model="filters.year" @change="updateQuery($event)">
              <label class="form-check-label display-6 fs-6" for="Alumni">
                Alumni
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="Masters" id="Masters" v-model="filters.year"
                @change="updateQuery($event)">
              <label class="form-check-label display-6 fs-6" for="Masters">
                Masters
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="PhD" id="PhD" v-model="filters.year"
                @change="updateQuery($event)">
              <label class="form-check-label display-6 fs-6" for="PhD">
                PhD
              </label>
            </div>
          </div>
        </div>
      </div>

      <div class="mb-4">
        <p class="display-4 fs-5 fw-bold mb-0" href="#major" aria-expanded="false" aria-controls="major">
          Major
        </p>
        <div id="major">
          <div class="card card-body border-0 mt-0">
            <div class="form-group">
              <select multiple class="form-select" id="major" data-live-search="true" v-model="filters.major"
                @change="updateQuery($event)">
                <option v-for="major in data.majors" :key="major">
                  {{ major.full_title }}</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <div v-if=!story class="mb-4">
        <p class="display-4 fs-5 fw-bold mb-0" href="#collections" aria-expanded="false" aria-controls="collections">
          Story Collection
        </p>
        <div class="mt-0" id="collections">
          <div class="card card-body border-0 mt-0">
            <div v-for="topic in data.topics" :key="topic.id">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" :value=topic.slug id="topic" v-model="filters.topic"
                  @change="updateQuery($event)">
                <label class="form-check-label display-6 fs-6" for="topic">
                  {{ topic.topic }}
                </label>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button type="button" class="btn btn-gold" @click="clearFilters">
        Clear All
      </button>
    </div>
  </div>
</template>

<script>
import { get } from "axios";
export default {
  name: "StudentFilter",
  props: {
    story: Boolean,
  },
  data() {
    return {
      data: {
        majors: [],
        topics: [],
      },
      filters: {
        year: [],
        major: [],
        topic: [],
      },
    };
  },
  methods: {
    async loadData() {
      const majors = await get('/api/majors/');
      this.data.majors = majors.data;
      const collections = await get('/api/collections/');
      this.data.topics = collections.data;
    },
    updateQuery(event) {
      const query = {};
      Object.entries(this.filters).forEach(([key, value]) => {
        if (value) {
          query[key] = (value);
        }
      })
      this.$router.push({ query })
    },
    clearFilters() {
      this.filters.year = [];
      this.filters.major = [];
      this.filters.topic = [];
      this.$router.push({});
    }
  },
  created() {
    this.loadData();
    this.$router.push({});
  }
};
</script>