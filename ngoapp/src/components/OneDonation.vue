<template>
    <div>
      
     <h1>{{donation.name}}</h1>
     <h2>{{donation.title}}</h2>
      <h2>{{donation.typeof}}</h2>
      <h2>{{donation.description}}</h2>
      
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
      <button @click="deleteDonation">Delete</button>
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