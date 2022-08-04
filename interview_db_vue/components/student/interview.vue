// interview.vue
// full student interview page

<template>
  <div class="row w-75 mx-auto mb-5">
    <div class="col-3 justify-content-center">
      <img src="../../css/quad.png" class="img-fluid mx-auto d-block" style="
              border-radius: 50%;
              height: 150px;
              width: 150px;
              object-fit: cover;" />
    </div>
    <div class="col-9 justify-content-start py-3">
      <h2 class="display-4">{{ firstName }}</h2>
      <h5 class="display-3 fs-3 text-info text-uppercase">{{ year + ", " + major }}</h5>
    </div>
  </div>

  <div class="row w-75 mx-auto mb-2 justify-content-center">
    <div class="ps-4">
      <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">Choosing a
        Major</button>
      <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">Coming to
        College</button>
      <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">Self
        Reflection</button>
      <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">Moving
        Forward</button>
    </div>
  </div>

  <div class="row w-75 mx-auto mb-5 pl-5 justify-content-center">
    <div class="ps-4">
      <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">Finding Community</button>
      <button type="button" class="btn btn-outline-info ms-3" data-bs-toggle="button" autocomplete="off">Advice</button>
    </div>
  </div>

  <div class="row w-75 mx-auto mb-5 ps-3">
      <p class="display-6 fs-5 mb-5 ps-4 lh-base border-start border-dark border-4">I’m a freshman here, and I’m planning to study computer science.  Freshman year has been pretty good. It takes a little getting used to at first but it’s been pretty well so far. [The hardest thing has been] getting used to the routine, I commute here everyday from Bonnie Lake. That’s about 45 miles south. So just getting used to having to travel so far for school. I take the train so it’s a bit nicer, and I don’t have to drive through the traffic.  [The biggest struggle is] just making sure to get up on time to get here because the trains go at 7:30 and I have to wake up at 6:00 or earlier for that. And then having to go to sleep at like nine o’clock just to get up in the morning, I guess has been something to get used to.</p>
      <p class="display-6 fs-5 mb-5 ps-4 lh-base border-start border-dark border-4">I’m a freshman here, and I’m planning to study computer science.  Freshman year has been pretty good. It takes a little getting used to at first but it’s been pretty well so far. [The hardest thing has been] getting used to the routine, I commute here everyday from Bonnie Lake. That’s about 45 miles south. So just getting used to having to travel so far for school. I take the train so it’s a bit nicer, and I don’t have to drive through the traffic.  [The biggest struggle is] just making sure to get up on time to get here because the trains go at 7:30 and I have to wake up at 6:00 or earlier for that. And then having to go to sleep at like nine o’clock just to get up in the morning, I guess has been something to get used to.</p>
  </div>

  <div class="row justify-content-center mx-auto">
    <div class="col-3 mx-2">
      <StudentCard :first-name="'Amanda'" />
    </div>
    <div class="col-3 mx-2">
      <StudentCard :first-name="'Anna'" />
    </div>
    <div class="col-3 mx-2">
      <StudentCard :first-name="'Caleb'" />
    </div>
  </div>
</template>

<script>
import StudentCard from "./student-card.vue";
export default {
  name: "Interview",
  components: {
    StudentCard,
  },
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
