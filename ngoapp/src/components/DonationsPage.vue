<template>
    <div>
        <h1>Donations</h1>
    </div>
    <div v-for="donation in donations" :key="donation.id" @click='selectdonation(donation.id)'>
      <OneDonation :donation='donation'/>
    </div>
    
    <div>
          <form>
            <label>Name</label>
            <input placeholder="name" value='name'/>
            <label>Title</label>
            <input placeholder="title" value='title'/>
            <label>Type</label>
            <input placeholder="type" value='type'/>
            <label>Description</label>
            <input placeholder="description" value='description'/>
            <button>Add</button>
            </form>
        </div>
  </template>
  
  <script>
    import axios from 'axios'
    import { BASE_URL } from '@/globals';
import OneDonation from './OneDonation.vue';
    export default {
    name: "DonationsPage",
    data: () => ({
        donations: []
    }),
    mounted: async function () {
        await this.getDonations();
    },
    methods: {
        async getDonations() {
            const res = await axios.get(`${BASE_URL}/donations/`);
            this.donations = res.data;
            console.log(res.data + "getDonations");
        }
    },
    selectdonation(donationid) {
        this.$router.push(`/donations/${donationid}`);
    },
    components: { OneDonation }
}
  </script>