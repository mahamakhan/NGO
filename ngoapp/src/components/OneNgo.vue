<template>
    <div>
        <!-- <h1>NGO</h1> -->
        <h2>{{ngoDetails.name}}</h2>
    </div>
  </template>
  
  <script>
    import axios from 'axios';
    import { BASE_URL } from '@/globals';
    export default {
      name: 'OneNgo',
      props:{
        list:{}
      },
      data: () => ({
      ngoDetails: {}
    }),
    mounted: async function() {
      await this.getngoDetails()
    },
    methods: {
      async getngoDetails() {
        const ngoId= parseInt(this.$route.params.list_id)
         const res = await axios.get(`${BASE_URL}/ngolist/${ngoId}`);
         console.log(res.data)
         console.log(ngoId)
         this.ngoDetails=res.data
      }
    }
      
    }
  </script>