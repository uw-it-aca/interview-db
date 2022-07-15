// student-listing.vue
// listings to be shown on Collection Page on one topic 
// and full student interviews page

<template>
  <div class="card w-50">
    <div class="row">
      <div class="col-1">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png" class="img-fluid">
      </div>
      <div class="col-5">
        <div class="card-body">
          <h2 class="fw-normal">{{ firstName }}</h2>
          <h4 class="text-uppercase">{{ year + "," + " " + major }}</h4>

          <p>"{{ quote }}"</p>
        
          <p><a class="btn btn-secondary" href="#">Read full story ></a></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StudentListing",
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
    quote: {
      type: String,
      required: true,
      default: "Some quote about really cool things wow I want to make games for other people so they can enjoy them too"
    },
  },
  data() {
    return {};
  },
  methods: {},
};
</script>
