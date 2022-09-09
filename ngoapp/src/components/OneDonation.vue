<template>
    <div class="bg-auto h-screen bg-gradient-to-r from-lime-500 via-lime-800 to-lime-700">
      
     <h1 class="text-center text-5xl font-normal leading-normal mt-0 mb-2 text-white py-10">{{donation.name}}</h1>
     <img :src='donation.title'  class="float-left w-600 h-715 transition-shadow ease-in-out duration-600 shadow-none hover:shadow-xl"/>
      <h2 class="text-left text-4xl font-normal leading-normal mt-0 mb-2 text-white">Reason:{{donation.typeof}}</h2>
      <h2 class="text-left text-2xl font-normal leading-normal mt-0 mb-2 text-white">{{donation.description}}</h2>
      
      <!-- <form @submit="changeDonation">
            <label>Name</label>
            <input placeholder="name" v-model='name'  @input='handleChange'/>
            <label>Title</label>
            <input placeholder="title" v-model='title'  @input='handleChange'/>
            <label>Type</label>
            <input placeholder="type" v-model='type'  @input='handleChange'/>
            <label>Description</label>
            <input placeholder="description" v-model='description' @input='handleChange' />
            <button>Change</button>
        </form> -->
      <button class="text-lime-500 border border-lime-500 hover:bg-lime-500 hover:text-white active:bg-lime-600 font-bold uppercase text-sm px-6 py-3 rounded outline-none focus:outline-none my-20 mr-1 mb-1 ease-linear transition-all duration-150" @click="deleteDonation">Delete</button>
    </div>
  </template>
  
  <script>
    
import { BASE_URL } from '@/globals';
import axios from 'axios';



    export default {
    name: "OneDonation",
    data: () => ({
        donation: {}
    }),
    methods: {
        async getDonationDets() {
            const donId = parseInt(this.$route.params.donations_id);
            const res = await axios.get(`${BASE_URL}/donations/${donId}`);
            console.log(res.data);
            this.donation = res.data;
        },
        async deleteDonation() {
            const donId = parseInt(this.$route.params.donations_id);
            const res = await axios.delete(`${BASE_URL}/donations/${donId}`);
            console.log(res.data);
            this.$router.push("/donations/");
        },
        // async changeDonation() {
        //     const donId = parseInt(this.$route.params.donations_id);
        //     const res = await axios.put(`${BASE_URL}/donations/${donId}`);
        //     console.log(res);
        //     //this.form=res.data
        // }
        
    },
    mounted: async function () {
        await this.getDonationDets();
    }
}
  </script>