// student-filter.vue
// to filter student interviews

<template>
  <div class="card" style="width: 18rem; border-radius:1.5rem">
    <h5 class="card-header border-0 border-top bg-white" style="border-radius:1.5rem">Filter by Student:</h5>
    <div class="card-body border-top">
      <div class="mb-4">
        <h2 class="display-4 fs-5 mb-0" data-bs-toggle="collapse" href="#year" aria-expanded="false"
          aria-controls="year">
          Year
        </h2>
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
                Other
              </label>
            </div>
          </div>
        </div>
      </div>

      <div class="mb-4">
        <h2 class="display-4 fs-5 mb-0" data-bs-toggle="collapse" href="#major" aria-expanded="false"
          aria-controls="major">
          Major
        </h2>
        <div class="collapse" id="major">
          <div class="card card-body border-0 mt-0">
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
                Other
              </label>
            </div>
          </div>
        </div>
      </div>

      <div class="mb-4">
        <h2 class="display-4 fs-5 mb-0" data-bs-toggle="collapse" href="#traits" aria-expanded="false"
          aria-controls="traits">
          Student Traits
        </h2>
        <div class="collapse" id="traits">
          <div class="card card-body border-0 mt-0">
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
                Other
              </label>
            </div>
          </div>
        </div>
      </div>

      <div class="mb-4">
        <h2 class="display-4 fs-5 mb-0" data-bs-toggle="collapse" href="#collections" aria-expanded="false"
          aria-controls="collections">
          Collections
        </h2>
        <div class="collapse" id="collections">
          <div class="card card-body border-0 mt-0">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                Choosing a Major
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                Advice
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                Coming to College
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                Finding Community
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                Getting Help
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                Self Reflection
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
              <label class="form-check-label display-6 fs-6" for="flexCheckDefault">
                Moving Forward
              </label>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StudentFilter",
  props: {},
  data() {
    return {};
  },
  methods: {},
};
</script>