<template>
    <div>
      
     <h1>{{donation.name}}</h1>
     <h2>{{donation.title}}</h2>
      <h2>{{donation.typeof}}</h2>
      <h2>{{donation.description}}</h2>
    </div>
  </template>
  
  <script>
    
import { BASE_URL } from '@/globals';
import axios from 'axios';


    export default {
      name: 'OneDonation',
      data:()=>({
        donation:{}
      }),
      methods:{
        async getDonationDets(){
          const donId=parseInt(this.$route.params.donations_id)
          const res= await axios.get(`${BASE_URL}/donations/${donId}`)
          console.log(res.data)
          this.donation=res.data
        }
      },
      mounted : async function(){
        await this.getDonationDets()
      }
    }
  </script>