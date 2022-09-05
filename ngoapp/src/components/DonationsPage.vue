<template>
    <div>
        <h1>Donations</h1>
    </div>
  </template>
  
  <script>
    import axios from 'axios'
    import { BASE_URL } from '@/globals';
    export default {
      name: 'DonationsPage',
      data: () =>({
        donations:[]
      }),
      mounted: async function () {
        await this.getDonations();
      },
      methods:{
        async getDonations(){
          const res= await axios.get(`${BASE_URL}/donations/`)
          this.donations=res.data
          console.log(res.data+ 'getDonations')
        }
      }
      
    }
  </script>