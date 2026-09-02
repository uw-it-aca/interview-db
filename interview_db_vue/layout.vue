<template>
  <header>
    <nav class="bg-white p-2">
      <div class="d-flex flex-md-row text-purple justify-content-between">
        <div class="d-flex flex-row title-logo">
          <router-link class="nav-link text-purple" active-class="active" aria-current="page" to="/">
            <img src="./images/purplew.png" class="img-fluid justify-content-start"
              style="object-fit:contain; width:100%; height:50px" alt="Husky W Logo">
          </router-link>
          <h2
            :class="[mq.mobile ? 'fs-3 d-flex text-center justify-content-center fw-bold' : 'fs-3 d-flex justify-content-start fw-bold',]">
            <router-link class="flex nav-link text-purple" active-class="active" aria-current="page" to="/">
              Husky Voices
            </router-link>
          </h2>
          <router-link v-if="mq.mobile || mq.tablet" active-class="active" aria-current="page" to="/menu">
            <i class="bi bi-list hamburger-menu"></i>
          </router-link>
        </div>
        <ul class="nav mt-2 p-2 col-6 justify-content-end nav-list">
          <li class="nav-item">
            <h6>
              <router-link class="nav-link text-purple" active-class="active" aria-current="page" to="/students/">Students
              </router-link>
            </h6>
          </li>
          <li class="nav-item">
            <h6>
              <router-link class="nav-link text-purple" active-class="active" aria-current="page"
                to="/collections">Collections
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

  <main>
    <slot name="title" />
    <slot name="description" />
    <slot name="content" />
  </main>

  <footer class="uw-footer text-white text-center">
    <div class="container py-5">
      <!-- word mark -->
      <a href="https://www.washington.edu" class="footer-wordmark d-block mx-auto mb-1">
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