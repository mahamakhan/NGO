<template>
    <div class="flex flex-wrap w-full mt-0">
     
        
        <nav>
          <ul class="flex mb-0 list-none flex-wrap pt-3 pb-4 flex-row mt-0">
     <li class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-orange-600 bg-orange-200 uppercase last:mr-0 mr-1"><router-link to="/">About</router-link></li>
    <li class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-orange-600 bg-orange-200 uppercase last:mr-0 mr-1"><router-link to="/donations">Donations</router-link></li>
  <li class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-orange-600 bg-orange-200 uppercase last:mr-0 mr-1"><router-link to="/ngolist">List of NGOs</router-link></li>
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