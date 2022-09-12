<template>

<div id="app">
  <header>
     <NavBar/>
    </header>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
   <main>
      <router-view v-slot="{ Component }">
        <transition name="slide" mode="out-in">
    <component :is="Component" :key="$route.path"/>
  </transition>
</router-view>
  
</main>
<footer>
  <FooterComp/>
</footer>
</div>
</template>

<script type="text/javascript">

import NavBar from './components/NavBar.vue';
import FooterComp from './components/FooterComp.vue';


export default {
  name: 'App',
 components: {
 
    NavBar,
    FooterComp
}
}
</script>

<style>
#app {
  font-family: 'Combo', cursive;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
  .slide-enter-active,
  .slide-leave-active{
    transition: opacity 1s, transform 1s;
  }
  .slide-enter-from,
  .slide-leave-to{
    opacity: 0;
    transform: translateX(-30%)
  }



</style>
