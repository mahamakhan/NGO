<template>

<div id="app">
  <header>
     <NavBar/>
    </header>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
   <main>
      <router-view></router-view>
  <!-- <BankAccount/>
  <DonationsPage/>
  <HomePage/>
  <OneDonation/>
  <OneNgo/>
  <NgoList/> -->
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
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  
}
</style>
