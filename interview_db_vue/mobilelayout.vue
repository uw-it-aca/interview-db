<template>
    <nav class="bg-white p-2">
        <!--<div class="d-flex flex-md-row text-purple justify-content-between">
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
          </div> -->
        <ul class="nav mt-2 p-2 flex-column justify-content-start">
            <li class="nav-item">
                <h6>
                    <router-link class="nav-link text-purple row" active-class="active" aria-current="page" to="/">
                        Home
                    </router-link>
                </h6>
            </li>
            <li class="nav-item">
              <h6>
                <router-link class="nav-link text-purple row" active-class="active" aria-current="page" to="/students">Student
                  Stories
                </router-link>
              </h6>
            </li>
            <li class="nav-item">
              <h6>
                <router-link class="nav-link text-purple row" active-class="active" aria-current="page"
                  to="/collections">Collections
                </router-link>
              </h6>
            </li>
            <li class="nav-item">
              <h6>
                <router-link class="nav-link text-purple row" active-class="active" aria-current="page" to="/about">About
                  Us</router-link>
              </h6>
            </li>
          </ul>
      </nav>
  </template>
  
<script>
export default {
    name: "LayoutMobile",
  };
</script>