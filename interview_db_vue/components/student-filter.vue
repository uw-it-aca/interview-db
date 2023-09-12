// student-filter.vue
// to filter student interviews

<template>
  <div class="card p-2" :class="(mq.tablet || mq.mobile) ? 'card-100 border-0' : 'card'">
    <div class="row mx-3 mt-3">
      <div class="col-6 justify-content-start d-flex p-0">
        <button v-if="mq.tablet || mq.mobile" type="button" class="btn-close" aria-label="Close"
          @click="$router.replace({ name: 'Students', query: { ...this.$route.query } })"></button>
      </div>
      <div class="col-6 justify-content-end d-flex">
        <a v-if="!emptyFilters" class="text-secondary active-link active-link-hover" @click="clearFilters">
          Clear All
        </a>
      </div>
    </div>
    <h2 class="m-3 fw-bold display-6 text-purple">Filter Stories</h2>
    <div class="card-body">
      <div class="mb-4">
        <p class="display-4 fw-bold fs-5 mb-0 dropdown-toggle" data-bs-toggle="collapse" href="#year" aria-expanded="true"
          aria-controls="year">
          Student Year
        </p>
        <div class="mt-0 collapse show" id="year">
          <div class="card card-body border-0">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="Freshman" id="Freshman" v-model="filters.year"
                @change="updateQuery()">
              <label class="form-check-label display-6 fs-6" for="freshman">
                Freshman
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="Sophomore" id="Sophomore" v-model="filters.year"
                @change="updateQuery()">
              <label class="form-check-label display-6 fs-6" for="sophomore">
                Sophomore
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="Junior" id="Junior" v-model="filters.year"
                @change="updateQuery()">
              <label class="form-check-label display-6 fs-6" for="Junior">
                Junior
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="Senior" id="Senior" v-model="filters.year"
                @change="updateQuery()">
              <label class="form-check-label display-6 fs-6" for="Senior">
                Senior
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="Alumni - undergrad" id="Alumni"
                v-model="filters.year" @change="updateQuery()">
              <label class="form-check-label display-6 fs-6" for="Alumni">
                Alumni
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="Masters" id="Masters" v-model="filters.year"
                @change="updateQuery()">
              <label class="form-check-label display-6 fs-6" for="Masters">
                Masters
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="PhD" id="PhD" v-model="filters.year"
                @change="updateQuery()">
              <label class="form-check-label display-6 fs-6" for="PhD">
                PhD
              </label>
            </div>
          </div>
        </div>
      </div>

      <div class="mb-4">
        <p class="display-4 fs-5 fw-bold mb-0 dropdown-toggle" data-bs-toggle="collapse" href="#major"
          aria-expanded="true" aria-controls="major">
          Major
        </p>
        <div class="mt-0 collapse show" id="major">
          <div class="card card-body border-0 mt-0">
            <Multiselect mode="tags" v-model="filters.major" :options="data.majors" :searchable="true"
              :close-on-select="false" @click="updateQuery()" @select="updateQuery()" @deselect="updateQuery()"
              @close="updateQuery()" />
          </div>
        </div>
      </div>

      <div v-if=!story class="mb-4">
        <p class="display-4 fs-5 fw-bold mb-0 dropdown-toggle" data-bs-toggle="collapse" href="#collections"
          aria-expanded="true" aria-controls="collections">
          Story Collection
        </p>
        <div class="mt-0 collapse show" id="collections">
          <div class="card card-body border-0 mt-0">
            <div class="justify-content-start col-12">
              <span v-for="topic in data.topics" :key="topic.id">
                <input type="checkbox" class="btn-check" :id="topic.id" :value=topic.slug v-model="filters.topic"
                  @change="updateQuery()">
                <label class="btn btn-outline-success m-1" :for="topic.id">
                  {{ topic.topic }}
                </label>
              </span>
            </div>
          </div>
        </div>
      </div>
      <div>
        <div v-if="mq.mobile || mq.tablet" class="row">
          <input type="checkbox" class="btn-check" id="clear-all" autocomplete="off">
          <label class="btn btn-success" for="clear-all"
            @click="$router.push({ name: 'Students', query: { ...this.$route.query } })">
            Apply Filters
          </label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { get } from "axios";
import Multiselect from '@vueform/multiselect';

export default {
  name: "StudentFilter",
  inject: ["mq"],
  components: {
    Multiselect,
  },
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
  watch: {
    "$route.query": {
      immediate: true,
      handler(n) {
        if (n.year === undefined) {
          this.filters.year = []
        } else {
          this.filters.year = n.year;
        }
        if (n.major === undefined) {
          this.filters.major = []
        } else {
          this.filters.major = n.major;
        }
        if (n.topic === undefined) {
          this.filters.topic = []
        } else {
          this.filters.topic = n.topic;
        }
      }
    }
  },
  methods: {
    async loadData() {
      const majors = await get('/api/majors/');
      majors.data.forEach(e => this.data.majors.push(e.full_title))
      const collections = await get('/api/collections/');
      this.data.topics = collections.data;
    },
    updateQuery() {
      const query = {};
      query['page'] = 1
      Object.entries(this.filters).forEach(([key, value]) => {
        if (value) {
          query[key] = (value);
        }
      })
      this.$router.replace({ query })
    },
    clearFilters() {
      this.filters.year = [];
      this.filters.major = [];
      this.filters.topic = [];
      this.$router.push({ query: { 'page': 1 } })
    },
  },
  created() {
    this.loadData();
  },
  computed: {
    emptyFilters() {
      return this.filters.year.length == 0 && this.filters.major.length == 0 && this.filters.topic.length == 0;
    },
  },
}
</script>

<style>
@import "@vueform/multiselect/themes/default.css";

.btn-outline-success {
  --bs-btn-bg: white !important;
  --bs-btn-border-color: #1E1E1E !important;
  --bs-btn-color: #1E1E1E !important;
}

.btn-check+.btn:hover {
  color: white !important;
  background-color: #4B2E83 !important;
}

.multiselect {
  --ms-line-height: 1;
  --ms-border-color: #1E1E1E;
  --ms-border-width: 1px;
  --ms-ring-color: #f6f4f8;
  --ms-radius: 0.1rem;
  --ms-py: 0.875rem;
  --ms-px: 0.875rem;

  --ms-caret-color: #1E1E1E;

  --ms-tag-font-size: 1rem;
  --ms-tag-line-height: 1.25rem;
  --ms-tag-font-weight: 400;
  --ms-tag-bg: #4B2E83;
  --ms-tag-color: #F8F9fA;
  --ms-tag-radius: 1.5px;
  --ms-tag-py: 0.5rem;
  --ms-tag-px: 0.5rem;
  --ms-tag-my: 0.5rem;
  --ms-tag-mx: 0.25rem;

  --ms-dropdown-bg: #FFFFFF;
  --ms-dropdown-border-color: #1E1E1E;
  --ms-dropdown-border-width: 1px;
  --ms-dropdown-radius: 0.1rem;
  width: 100%;
}

.multiselect-clear {
  margin: 0.25rem;
}

.multiselect-tag {
  white-space: normal;
}

.multiselect-tags-search {
  max-width: 100%;
  display: flex;
}

.dropdown-toggle[aria-expanded="true"]:after {
  transform: rotate(-180deg);
}

.dropdown-toggle:after {
  transition: 0.3s;
}

.dropdown-toggle-split {
  justify-content: flex-end;
}

a.active-link {
  text-decoration: none;
  cursor: pointer;
}

a.active-link-hover:hover {
  text-decoration: underline;
  cursor: pointer;
}
</style>
