// student-filter.vue
// to filter student interviews

<template>
  <div class="card p-3" :class="(mq.tablet || mq.mobile) ? 'card-100 border-0' : 'card'">
    <div v-if="!mq.tablet && !mq.mobile" class="row m-3">
      <div class="justify-content-end d-flex">
        <a v-if="!emptyFilters" class="text-secondary active-link active-link-hover" @click="clearFilters">
          Clear All
        </a>
      </div>
    </div>

    <div class="card-body">
      <div class="row mb-4">
        <h2 class="d-flex fw-bold display-6 text-gold justify-content-start"
          :class="mq.tablet || mq.mobile ? 'col-9' : ''">Filter Stories</h2>
        <div v-if = "(mq.tablet || mq.mobile)" class="d-flex col-3 justify-content-end p-0">
          <button v-if="topicId == undefined" 
            type="button" class="btn-close" aria-label="Close"
            @click="$router.replace({ path: '/students/', query: { ...this.$route.query } })"></button>
          <button v-else type="button" class="btn-close" aria-label="Close"
          @click="$router.push({ name: 'Collections', params: {id: topicId}, query: { ...this.$route.query } })"></button>
        </div>
      </div>
      <div class="mb-5">
        <p class="display-4 fw-bold fs-5 mb-3">
          Student Year
        </p>
        <div class="mt-0" id="year">
          <div class="justify-content-start col-12">
            <input type="checkbox" class="btn-check" id="Freshman" value="Freshman" v-model="filters.year"
              @change="updateQuery()">
            <label class="btn btn-outline-success m-1" for="Freshman">
              Freshman
            </label>
            <input type="checkbox" class="btn-check" id="Sophomore" value="Sophomore" v-model="filters.year"
              @change="updateQuery()">
            <label class="btn btn-outline-success m-1" for="Sophomore">
              Sophomore
            </label>
            <input type="checkbox" class="btn-check" id="Junior" value="Junior" v-model="filters.year"
              @change="updateQuery()">
            <label class="btn btn-outline-success m-1" for="Junior">
              Junior
            </label>
            <input type="checkbox" class="btn-check" id="Senior" value="Senior" v-model="filters.year"
              @change="updateQuery()">
            <label class="btn btn-outline-success m-1" for="Senior">
              Senior +
            </label>
          </div>
        </div>
      </div>

      <div class="mb-5">
        <p class="display-4 fs-5 fw-bold mb-3">
          Major
        </p>
        <div class="mt-0" id="major">
          <Multiselect mode="tags" v-model="filters.major" :options="data.majors" :searchable="true"
            :close-on-select="false" @click="updateQuery()" @select="updateQuery()" @deselect="updateQuery()"
            @close="updateQuery()" />
        </div>
      </div>

      <!-- do not filter on collections if navigated from or on a topic page-->
      <div v-if="story || topicId != undefined" class="mb-5">
        </div>
      <div v-else class="mb-5">
        <p class="display-4 fs-5 fw-bold mb-3">
          Story Collection
        </p>
        <div class="mt-0" id="collections">
          <div class="mt-0" id="major">
          <Multiselect mode="tags" v-model="filters.topic" :options="data.topics" :searchable="true"
            :close-on-select="false" @click="updateQuery()" @select="updateQuery()" @deselect="updateQuery()"
            @close="updateQuery()" />
          </div>
        </div>
      </div>
      <div>
        <div v-if="mq.mobile || mq.tablet" class="row fixed-bottom">
          <button class="btn btn-light btn-block w-50" for="clear-all" @click="clearFilters">
            Clear All
          </button>
          
          <!-- navigate back to students or topic page, using topicId, if any -->
          <button v-if="topicId == undefined" class="btn btn-gold btn-block fw-bold w-50"
            @click="$router.push({ name: 'Students', query: { ...this.$route.query } })">
            Apply
          </button>
          <button v-else class="btn btn-gold btn-block fw-bold w-50"
            @click="$router.push({ name: 'Collections', params: {id: topicId}, query: { ...this.$route.query } })">
            Apply
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
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
      topicId: this.$route.params.topicId,
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
          if (!Array.isArray(n.major)) {
            this.filters.major = []
            this.filters.major.push(n.major)
          } else {
            this.filters.major = n.major;
          }
        }
        if (n.topic === undefined) {
          this.filters.topic = []
        } else {
          if (!Array.isArray(n.topic)) {
            this.filters.topic = []
            this.filters.topic.push(n.topic)
          } else {
            this.filters.topic = n.topic
          }
        }
      }
    }
  },
  methods: {
    async loadData() {
      const majors = await axios.get('/api/majors/');
      majors.data.forEach(e => this.data.majors.push(e.full_title));
      const collections = await axios.get('/api/collections/');
      collections.data.forEach(e => this.data.topics.push(e.topic))
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
      this.$router.replace({ query: { 'page': 1 } })
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
  --bs-btn-color: #1E1E1E !important;
  --bs-btn-border-color: #1E1E1E !important;
  padding: 0.5rem !important;
}

.btn-check+.btn:hover {
  color: #1E1E1E !important;
  background-color: #f6f4f8 !important;
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
