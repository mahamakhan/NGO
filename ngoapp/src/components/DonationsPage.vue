<template>
  <div  class="bg-cover bg-gradient-to-r from-lime-500 via-lime-800 to-lime-700">
    <div>
        <h1 class="text-6xl font-normal leading-normal mt-0 mb-2 text-white">Donations</h1>
    </div>
    <div v-for="donation in donations" :key="donation.id" class="py-12">
      <h2  class="text-left text-4xl font-normal leading-normal mt-0 mb-2 text-white">{{donation.name}}</h2>
      <h2 class="text-left text-3xl font-normal leading-normal mt-0 mb-2 text-white">{{donation.typeof}}</h2>
      <img :src='donation.title'  class="float-right max-w-sm h-auto transition-shadow ease-in-out duration-600 shadow-none hover:shadow-xl" @click='selectdonation(donation.id)'/>
      <h2 class="text-left text-2xl font-normal leading-normal mt-0 mb-2 text-white">{{donation.description}}</h2>
      <button @click="gotobank()">Donate</button>
    </div>
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