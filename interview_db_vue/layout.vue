<template>
  <div class="container py-4 bg-white">
    <header class="pb-3">
      <nav class="fixed-top pt-4 bg-white">
        <div class="d-flex flex-column flex-md-row pb-3 border-bottom border-primary">
          <h2 class="fs-4 d-flex justify-content-center text-decoration-none col-5 fw-bold">
            <router-link class="nav-link" active-class="active" aria-current="page" to="/">Husky Voices</router-link>
          </h2>

          <ul class="nav d-inline-flex mt-2 mt-0 ms-5 col-7">
            <li class="nav-item">
              <h6>
                <router-link class="nav-link" active-class="active" aria-current="page" to="/students">Student Stories
                </router-link>
              </h6>
            </li>
            <li class="nav-item">
              <h6>
                <router-link class="nav-link" active-class="active" aria-current="page" to="/collections">Collections
                </router-link>
              </h6>
            </li>
            <li class="nav-item">
              <h6>
                <router-link class="nav-link" active-class="active" aria-current="page" to="/about">About
                  Us</router-link>
              </h6>
            </li>
          </ul>
        </div>
      </nav>
    </header>
    <main>
      <slot name="title" />
      <slot name="description" />
      <slot name="content" />
    </main>
    <footer class="p-5 my-5 text-muted justify-content-end border-top border-primary">
      <ul class="list-inline mb-2">
        <li class="list-inline-item item-dot">
          <a href="mailto:help@uw.edu?subject=Student Experience Interviews Project" title="Contact the DawgPath team"
            class="text-muted text-decoration-none me-2">Contact</a>
        </li>
        <li class="list-inline-item item-dot">
          <a href="https://itconnect.uw.edu/learn/success-analytics/apps/#dawg" title="DawgPath Docs on IT Connect"
            class="text-muted text-decoration-none me-2">Documentation</a>
        </li>
        <li class="list-inline-item item-dot">
          <a href="https://www.washington.edu/online/terms/" title="UW Terms of Use"
            class="text-muted text-decoration-none me-2">Terms</a>
        </li>
        <li class="list-inline-item">
          <a href="https://www.washington.edu/online/privacy/" title="UW Privacy Policy"
            class="router-link text-muted text-decoration-none me-2">Privacy</a>
        </li>
      </ul>
      &copy; 2022 University of Washington
    </footer>
  </div>
</template>

<script>
export default {
  name: "LayoutComp",
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