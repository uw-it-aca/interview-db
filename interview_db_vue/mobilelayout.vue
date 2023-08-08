<template>
  <nav class="bg-white p-2">
    <div class="row mt-2 px-4">
      <button type="button" class="btn-close justify-content-end" aria-label="Close" @click="$router.go(-1)"></button>
    </div>
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