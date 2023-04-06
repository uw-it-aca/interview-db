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
              <input class="form-check-input" type="checkbox" value="Alumni - undergrad" id="Alumni" v-model="filters.year"
                @change="updateQuery($event)">
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
        <p class="display-4 fs-5 fw-bold mb-0" data-bs-toggle="collapse" href="#major" aria-expanded="false"
          aria-controls="major">
          Major
        </p>
        <div class="collapse" id="major">
          <div class="card card-body border-0 mt-0">
            <div v-for="major in data.majors" :key="major.id">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" :value="major" id="major" v-model="filters.major"
                  @change="updateQuery($event)">
                <label class="form-check-label display-6 fs-6" for="major">
                  {{ major.full_title }}
                </label>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- <div class="mb-4">
        <p class="display-4 fs-5 fw-bold mb-0" data-bs-toggle="collapse" href="#traits" aria-expanded="false"
          aria-controls="traits">
          Student Traits
        </p>
        <div class="collapse" id="traits">
          <div class="card card-body border-0 mt-0">
            <div v-for="trait in data.traits" :key="trait.id">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" :value="trait.type" id="trait" v-model="filters.trait"
                  @change="updateTrait($event)">
                <label class="form-check-label display-6 fs-6" for="trait">
                  {{ trait.type }}
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
    </div>
  </div>
</template>

<script>
import { get } from "axios";
export default {
  name: "StudentFilter",
  props: {
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
      const majors = await get('api/majors/');
      this.data.majors = majors.data;
      const types = await get('api/types/');
      this.data.traits = types.data;
      const collections = await get('api/collections/');
      this.data.topics = collections.data;
    },
    updateQuery(event) {
      const query = {}
      Object.entries(this.filters).forEach(([key, value]) => {
        if (value) {
          query[key] = value
        }
      })
      this.$router.push({ query })
    }
  },
  // updateFilters(event) {
  //   this.$router.push({
  //     name: 'Students', query: {
  //       major : JSON.stringify(this.filters.major),
  //       trait: JSON.stringify(this.filters.trait),
  //       topic: JSON.stringify(this.filters.topic),
  //     }
  //   });
  // },
  // updateYear(event) {
  //   this.$router.replace({ name: 'Students', query: Object.assign({}, this.$route.query, { year: JSON.stringify(this.filters.year) }) });
  // },
  // updateMajor(event) {
  //   this.$router.replace({ name: 'Students', query: Object.assign({}, this.$route.query, { major: JSON.stringify(this.filters.major) }) });
  // },
  // updateTrait(event) {
  //   this.$router.replace({ name: 'Students', query: Object.assign({}, this.$route.query, { trait: JSON.stringify(this.filters.trait) }) });
  // },
  // updateTopic(event) {
  //   this.$router.replace({ name: 'Students', query: Object.assign({}, this.$route.query, { topic: JSON.stringify(this.filters.topic) }) });
  // },
  created() {
    this.loadData();
  }
};
</script>