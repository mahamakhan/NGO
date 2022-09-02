<template>
    <div>
      <nav><h1>Nav</h1></nav>
        
        <nav>
     <router-link to="/">About</router-link>
    <router-link to="/donations">Donations</router-link>
    <router-link to="/ngolist">List of NGOs</router-link>
  </nav> 
    </div>
  </template>
  
  <script>
    export default {
      name: 'NavBar'
      
    }
  </script>

  <style>
    #navbar{
  background-image: url('../bg.png');
  background-position: center; /* Center the image */
  background-repeat: no-repeat; /* Do not repeat the image */
    }
  </style>