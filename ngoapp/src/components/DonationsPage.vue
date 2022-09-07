<template>
    <div>
        <h1>Donations</h1>
    </div>
    <div v-for="donation in donations" :key="donation.id" >
      <h2 @click='selectdonation(donation.id)'>{{donation.name}}</h2>
      <h2>{{donation.title}}</h2>
      <h2>{{donation.typeof}}</h2>
      <h2>{{donation.description}}</h2>
      <button @click="gotobank()">Donate</button>
    </div>
    
    
  </template>
  
  <script>
    import axios from 'axios'
    import { BASE_URL } from '@/globals';


    export default {
    name: "DonationsPage",
    data: () => ({
        donations: [],
         
       
          name:'',
          title:'',
          type:'',
          description:'',
        
        
    }),
    mounted: async function () {
        await this.getDonations();
    },
    methods: {
        async getDonations() {
            const res = await axios.get(`${BASE_URL}/donations/`);
            this.donations = res.data;
            console.log(res.data + "getDonations");
        },
        selectdonation(donationid) {
        this.$router.push(`/donations/${donationid}`);
    },
    gotobank(){
      this.$router.push(`/bankaccount/`);
        }
      
}}
  </script>