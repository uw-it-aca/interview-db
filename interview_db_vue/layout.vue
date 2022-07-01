<template>
  <header>
    <h1>Interview DB</h1>
  </header>
    <nav>
    <ul>
    <li><router-link to="/customize">Customize</router-link></li>
    <li><router-link to="/">Home</router-link></li>
    </ul>
    </nav>
    <main>
        <slot name="content" />
    </main>
    <footer>
    Copyright &copy; 2012-2013
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
      appName: "AXDD Django+Vue",
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
