<template>
    <div>
      <nav><h1>Nav</h1></nav>
        
        <nav>
          <ul>
     <li><router-link to="/">About</router-link></li>
    <li><router-link to="/donations">Donations</router-link></li>
  <li><router-link to="/ngolist">List of NGOs</router-link></li>
</ul>
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