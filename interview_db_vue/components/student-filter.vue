// student-filter.vue
// to filter student interviews

<template>
  <div class="card" style="width: 18rem;">
    <h5 class="card-header bg-white">Filter by Student:</h5>
    <div class="card-body">
      <p>
        <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false"
          aria-controls="collapseExample">
          Link with href
        </a>
      </p>
      <div class="collapse" id="collapseExample">
        <div class="card card-body">
          <div class="form-check">
            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
            <label class="form-check-label" for="flexCheckDefault">
              Freshman
            </label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
            <label class="form-check-label" for="flexCheckDefault">
              Sophomore
            </label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
            <label class="form-check-label" for="flexCheckDefault">
              Junior
            </label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
            <label class="form-check-label" for="flexCheckDefault">
              Senior
            </label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
            <label class="form-check-label" for="flexCheckDefault">
              Other
            </label>
          </div>
        </div>
      </div>


      <div class="btn-group">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton"
          data-bs-toggle="dropdown" aria-expanded="false">
          Year
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
          <li><a class="dropdown-item" href="#">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                <label class="form-check-label" for="flexCheckDefault">
                  Freshman
                </label>
              </div>
            </a></li>
          <li><a class="dropdown-item" href="#">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                <label class="form-check-label" for="flexCheckDefault">
                  Sophomore
                </label>
              </div>
            </a></li>
          <li><a class="dropdown-item" href="#">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                <label class="form-check-label" for="flexCheckDefault">
                  Junior
                </label>
              </div>
            </a></li>
          <li><a class="dropdown-item" href="#">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                <label class="form-check-label" for="flexCheckDefault">
                  Senior
                </label>
              </div>
            </a></li>
          <li><a class="dropdown-item" href="#">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                <label class="form-check-label" for="flexCheckDefault">
                  Other
                </label>
              </div>
            </a></li>
        </ul>
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