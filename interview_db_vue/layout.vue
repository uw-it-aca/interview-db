<template>
  <header>
    <nav class="bg-white border-0 p-2">
      <div class="d-flex flex-column flex-md-row text-purple">
        <img src="./css/w.svg" class="display-block" />
        <h2 class="fs-3 d-flex justify-content-center col-3 fw-bold">
          <router-link class="nav-link" active-class="active" aria-current="page" to="/">Husky Voices</router-link>
        </h2>

        <ul class="nav d-inline-flex mt-2 mx-auto p-2 col-9 justify-content-end">
          <li class="nav-item">
            <h6>
              <router-link class="nav-link text-purple" active-class="active" aria-current="page" to="/students">Student Stories
              </router-link>
            </h6>
          </li>
          <li class="nav-item">
            <h6>
              <router-link class="nav-link text-purple" active-class="active" aria-current="page" to="/collections">Collections
              </router-link>
            </h6>
          </li>
          <li class="nav-item">
            <h6>
              <router-link class="nav-link text-purple" active-class="active" aria-current="page" to="/about">About
                Us</router-link>
            </h6>
          </li>
        </ul>
      </div>
    </nav>
  </header>

  <main class="">
    <slot name="title" />
    <slot name="description" />
    <slot name="content" />
  </main>


  <footer class="p-4 footer bg-purple text-white">
    <!-- <div class="row g-0 justify-content-end">
      <div class="col-2 ps-5">
        <h2 class="fs-4 d-flex fw-bold border-bottom">Husky Voices</h2>
        <p>ux@uw.edu</p>
      </div>
      <div class="col-5"></div>
      <div class="col-5 display-block">
        <a href="mailto:ux@uw.edu?subject=Husky Voices" title="Contact the AXDD UX Team"
          class="text-decoration-none ms-4 justify-content-end">Contact</a>
        <a href="https://itconnect.uw.edu/learn/success-analytics/apps/#dawg" title="DawgPath Docs on IT Connect"
          class="text-decoration-none ms-4">Documentation</a>
        <a href="https://www.washington.edu/online/terms/" title="UW Terms of Use"
          class="text-decoration-none ms-4">Terms</a>
        <a href="https://www.washington.edu/online/privacy/" title="UW Privacy Policy"
          class="text-decoration-none router-link ms-4">Privacy</a>
      </div>
    </div> -->
    <div class="col-6">
      
    </div>
    <div class="col-6">
      <p class="ps-5 text-right justify-content-end">Copyright &copy; 2023 University of Washington</p>
    </div>
    

</footer>
</template>

<script>
export default {
  name: "LayoutComp",
  inject: ["mq"],
  components: {},
  props: {
    pageTitle: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      // minimum application setup overrides
      appName: "Interview DB",
      // automatically set year
      currentYear: new Date().getFullYear(),
    };
  },
  created: function () {
    // constructs page title in the following format "Page Title - AppName"
    document.title = this.pageTitle + " - " + this.appName;
  },
};
</script>