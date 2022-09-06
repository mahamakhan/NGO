<template>
    <div>
      
      <h2>{{donation.name}}</h2>
      <h2>{{donation.title}}</h2>
      <h2>{{donation.typeof}}</h2>
      <h2>{{donation.description}}</h2>
    </div>
  </template>
  
  <script>
    export default {
      name: 'OneDonation',
      props:{
        donation:{}
      }
      
    }
  </script>