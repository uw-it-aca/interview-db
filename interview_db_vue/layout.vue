<template>
  <div class="container py-4">
    <header class="pb-3">
      <nav>
        <ul class="nav justify-content-end">
          <li class="nav-item">
            <router-link class="nav-link" active-class="active" aria-current="page" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" active-class="active" aria-current="page" to="/students">Students
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" active-class="active" aria-current="page" to="/collections">Collections
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" active-class="active" aria-current="page" to="/about">About Us</router-link>
          </li>
        </ul>
      </nav>
    </header>
    <main>
      <slot name="title" />
      <slot name="description" />
      <slot name="content" />
    </main>
    <footer class="p-5 my-5 text-muted bg-light justify-content-end">
      <ul class="list-inline mb-2">
        <li class="list-inline-item item-dot">
          <a href="mailto:help@uw.edu?subject=Student Experience Interviews Project" title="Contact the DawgPath team"
            class="text-muted text-decoration-none me-2">Contact</a>
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