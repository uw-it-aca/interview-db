<template>
  <header>
    <nav class="bg-white p-2">
      <div class="d-flex flex-md-row text-purple justify-content-between">
        <div class="d-flex flex-row title-logo">
            <router-link class="nav-link text-purple" active-class="active" aria-current="page" to="/">
              <img src="./images/purplew.png" class="img-fluid justify-content-start"
                style="object-fit:contain; width:100%; height:50px" alt="Husky W Logo">
            </router-link>
            <h2 class="fs-3 d-flex justify-content-start fw-bold">
              <router-link class="nav-link text-purple" active-class="active" aria-current="page" to="/">
                Husky Voices
              </router-link>
            </h2>
          <router-link active-class="active" aria-current="page" to="/menu">
            <i class="bi bi-list hamburger-menu"></i>
          </router-link>
        </div>
<!-- 
        <router-link class="nav-link text-purple" active-class="active" aria-current="page" to="/">
          <div><img src="./images/purplew.png" class="justify-content-start"
              style="object-fit:contain; width:100%; height:50px; position:absolute" alt="Husky W Logo"></div>
          <div>
            <h2 class="fs-3 fw-bold">
              Husky Voices
            </h2>
          </div>
        </router-link> -->

        <!-- <button @click="$router.push({ name: 'Home' })" class="border-0 bg-white">
            <img src="./images/purplew.png" style="object-fit:contain; width:100%; height:50px"
              alt="Husky W Logo">
            <h2 class="fs-3 fw-bold text-purple">Husky Voices
            </h2>
          </button> -->
        <!-- </div> -->
        <ul class="nav mt-2 p-2 col-6 justify-content-end nav-list">
          <li class="nav-item">
            <h6>
              <router-link class="nav-link text-purple" active-class="active" aria-current="page" to="/students">Student
                Stories
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

  <main class="p-2">
    <slot name="title" />
    <slot name="description" />
    <slot name="content" />
  </main>


  <footer class="py-4 px-5 footer bg-purple text-white">
    <div class="row">
       <div class="col-6">
        <!--<img src="../images/washingtonlogo.svg" /> -->
      </div>
      <div class="col-6">
        <p class="text-end justify-content-end">Copyright &copy; 2023 University of Washington</p>
      </div>
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