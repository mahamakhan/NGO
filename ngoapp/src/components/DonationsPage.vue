<template>
    <div>
        <h1>Donations</h1>
    </div>
    <div v-for="donation in donations" :key="donation.id" @click='selectdonation(donation.id)'>
      <h2>{{donation.name}}</h2>
      <h2>{{donation.title}}</h2>
      <h2>{{donation.typeof}}</h2>
      <h2>{{donation.description}}</h2>
    </div>
    
    <div>
          <form>
            <label>Name</label>
            <input placeholder="name" value='name'  @input='handleChange'/>
            <label>Title</label>
            <input placeholder="title" value='title'  @input='handleChange'/>
            <label>Type</label>
            <input placeholder="type" value='type'  @input='handleChange'/>
            <label>Description</label>
            <input placeholder="description" value='description'  @input='handleChange'/>
            <button @submit="addDonation">Add</button>
            </form>
        </div>
  </template>
  
  <script>
    import axios from 'axios'
    import { BASE_URL } from '@/globals';

    export default {
    name: "DonationsPage",
    data: () => ({
        donations: [],
        form:{}
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
      async addDonation(){
        const res=await axios.post(`${BASE_URL}/donations/`)
        console.log(res.data)
      },
      handleChange(event) {
          this.form=event.target.value
           
        },
    }
}
  </script>