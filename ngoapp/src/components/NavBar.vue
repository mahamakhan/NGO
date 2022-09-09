<template>
  <nav class="relative flex flex-wrap items-center justify-between px-2 py-3 bg-slate-300 -mt-16">
      <div class="container px-4 mx-auto flex flex-wrap items-center justify-between">
        <div class="w-full relative flex justify-between lg:w-auto  px-4 lg:static lg:block lg:justify-start">
          <h1 class="text-md font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase text-grey">
              این جی او
          </h1>
          <button class="text-white cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none" type="button" v-on:click="toggleNavbar()">
            <i class="fas fa-bars"></i>
          </button>
        </div>
        <div v-bind:class="{'hidden': !showMenu, 'flex': showMenu}" class="lg:flex lg:flex-grow items-center">
          <ul class="flex flex-col lg:flex-row list-none ml-auto">
            <li class="nav-item">
              <div class="px-3 py-2 flex items-center text-sm uppercase font-bold leading-snug text-grey hover:opacity-75">
                <i class="fab fa-facebook-square text-lg leading-lg text-white opacity-75" /><span class="ml-2"><router-link to="/">About</router-link></span>
              </div>
            </li>
            <li class="nav-item">
              <div class="px-3 py-2 flex items-center text-sm uppercase font-bold leading-snug text-grey hover:opacity-75" >
                <i class="fab fa-twitter text-lg leading-lg text-white opacity-75" /><span class="ml-2"><router-link to="/donations">Donations</router-link></span>
              </div>
            </li>
            <li class="nav-item">
              <div class="px-3 py-2 flex items-center text-sm uppercase font-bold leading-snug text-grey hover:opacity-75" >
                <i class="fab fa-pinterest text-lg leading-lg text-white opacity-75" /><span class="ml-2"><router-link to="/ngolist">List of NGOs</router-link></span>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
      export default {
      name: "NavBar",
      data() {
      return {
        showMenu: false
      }
    },
    methods: {
      toggleNavbar: function(){
        this.showMenu = !this.showMenu;
      }
    }
      }
  </script>