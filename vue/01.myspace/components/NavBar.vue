<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
          <router-link class="navbar-brand" :to="{name: 'Home'}">MySpace</router-link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarText">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <router-link class="nav-link" aria-current="page" :to="{name: 'Home'}">首页</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" :to="{name: 'UserList'}">用户列表</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" :to="{name: 'UserProfile'}">用户空间</router-link>
              </li>
            </ul>
            <ul class="navbar-nav">
                <li class="nav-item">
                  <router-link class="nav-link" :to="{name: 'Login'}">登录</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link" :to="{name: 'Register'}">注册</router-link>
                </li>
              </ul>
          </div>
        </div>
      </nav>
</template>

<script>

export default {
    name: "NavBar",
    components: {

    }
}

</script>

<style scoped>

</style>