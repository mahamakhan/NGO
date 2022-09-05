<template>
    <div>
        <h1>NGO</h1>
    </div>
  </template>
  
  <script>
    import axios from 'axios';
    import { BASE_URL } from '@/globals';
    export default {
      name: 'OneNGO',
      data: () => ({
      ngoDetails: null
    }),
    mounted: async function() {
      await this.getngoDetails()
    },
    methods: {
      async getngoDetails() {
        const ngoId= parseInt(this.$route.params.ngolist_id)
         const res = await axios.get(`${BASE_URL}/ngolist/${ngoId}`);
         console.log(res.data)
         console.log(ngoId)
         this.ngoDetails=res.data
      }
    }
      
    }
  </script>