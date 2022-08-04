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
              <h2 class="card-title display-6 mb-2">{{ firstName }}</h2>
              <p class="card-subtitle text-uppercase display-6 fs-5 text-info">
                {{ major + "," + " " + year }}
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
    firstName: {
      type: String,
      required: true,
      default: "Joe",
    },
    year: {
      type: String,
      required: true,
      default: "Freshman",
    },
    major: {
      type: Array,
      required: true,
      default: "Communications",
    },
    story: {
      type: String,
      required: true,
      default:
        "I would have liked to have traveled before college. I think Germany requires you to take a gap year before you go to college… it could have been somewhere else… and I think that that would be very, very beneficial. I mean, we’re too young to go into college at age eighteen, understanding what we want to do for the rest of our lives. So, yeah, maybe having a gap year that could be partially funded by the school… maybe that’s too idealistic… but it would be useful because in school you’re really in a bubble, so going out to explore the world would be beneficial. (11)",
    },
  },
  data() {
    return {};
  },
  methods: {},
};
</script>
