<template>
  <div class="container py-4">
    <header class="pb-3">
      <nav>
        <ul class="nav justify-content-end">
          <li class="nav-item">
            <router-link class="nav-link" active-class="active" aria-current="page" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" active-class="active" aria-current="page" to="/students">Students</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" active-class="active" aria-current="page" to="/collections">Collections</router-link>
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
      &copy; 2022
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