<template>
  <header class="bg-purple">
    <nav class="navbar navbar-expand-md py-2">
      <div class="container-xxl d-flex align-items-center justify-content-between">
        
        <!-- Left: Branding -->
        <div class="d-flex align-items-center gap-3">
          <!-- W Logo -->
          <router-link to="/" aria-label="Home" class="d-inline-flex align-items-center">
            <span class="w-logo"></span>
          </router-link>

          <!-- Wordmark -->
          <router-link to="/" aria-label="Home" class="d-inline-flex align-items-center">
            <span class="wordmark"></span>
          </router-link>

          <!-- Divider -->
          <span class="text-light opacity-50 fs-5 header-divider">|</span>

          <!-- Husky Voices -->
          <router-link to="/" class="nav-link p-0 text-light">
            Husky<strong>Voices</strong>
          </router-link>
        </div>

        <!-- Right: Nav Links -->
        <ul class="nav d-none d-lg-flex align-items-center gap-4 gap-lg-5 mb-0">
          <li class="nav-item">
            <router-link class="nav-link px-0 text-light fw-bold" to="/students">Student Stories</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link px-0 text-light fw-bold" to="/about">About Us</router-link>
          </li>
        </ul>

        <!-- Hamburger (mobile/tablet only) -->
        <router-link v-if="mq.mobile | mq.tablet" active-class="active" aria-current="page" to="/menu">
          <i class="bi bi-list hamburger-menu"></i>
        </router-link>

      </div>
    </nav>
  </header>

  <main>
    <slot name="title" />
    <slot name="description" />
    <slot name="content" />
  </main>

  <footer class="uw-footer text-white text-center">
    <div class="container py-5">
      <!-- word mark -->
      <a href="https://www.washington.edu" class="wordmark d-block mx-auto mb-1">
        <span class="visually-hidden">University of Washington</span>
      </a>
      <!-- be boundless -->
      <a href="https://www.washington.edu/boundless/" class="d-block mx-auto my-0">
        <span class="be-boundless d-block mx-auto">
          <span class="visually-hidden">Be boundless</span>
        </span>
      </a>
      <hr class="uw-footer-rule" />
      <!-- copyright info -->
      <p class="mb-0 small">
        © 2026 University of Washington <span class="opacity-75">|</span> Seattle, WA
      </p>
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