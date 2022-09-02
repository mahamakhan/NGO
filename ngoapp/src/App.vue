<template>

<div>
  <img alt="Vue logo" src="./assets/logo.png">
  <BankAccount/>
  <DonationsPage/>
  <HomePage/>
  <OneDonation/>
  <OneNgo/>
  <NavBar/>
  <NgoList/>
</div>
</template>

<script>
import BankAccount from './components/BankAccount.vue';
import DonationsPage from './components/DonationsPage.vue';
import HomePage from './components/HomePage.vue';
import OneDonation from './components/OneDonation.vue';
import OneNgo from './components/OneNgo.vue';
import NavBar from './components/NavBar.vue';
import NgoList from './components/NgoList.vue';

export default {
  name: 'App',
  components: {
    BankAccount,
    DonationsPage,
    HomePage,
    OneDonation,
    OneNgo,
    NavBar,
    NgoList
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
