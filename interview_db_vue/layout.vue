<template>
  <header>
    <h1>Interview DB</h1>
  </header>
  <nav>
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/collections">Collections</router-link></li>
      <li><router-link to="/students">Students</router-link></li>
      <li><router-link to="/about">About Us</router-link></li>
    </ul>
  </nav>
  <main>
    <slot name="content" />
  </main>
  <footer>
  </footer>
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
