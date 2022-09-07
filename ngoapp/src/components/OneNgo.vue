<template>
    <div>
        <!-- <h1>NGO</h1> -->
        <h2>{{ngoDetails.name}}</h2>
        <form @submit="changelist">
            <label>Name of Your NGO</label>
            <input placeholder="Name" v-model='newlist.name'/>
            <label>Country</label>
            <input placeholder="Country" v-model='newlist.country'/>
            <label>City</label>
            <input placeholder="city" v-model='newlist.city'/>
            <label>Email to contact</label>
            <input placeholder="email" v-model='newlist.email'/>
            <label>Is it International?</label>
            <input placeholder="international"  v-model='newlist.international'/>
            <label>Is it a non-profit NGO?</label>
            <input placeholder="profit/nonprofit"  v-model='newlist.profit'/>
            <button>Edit</button>
            </form>
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
      },
      async changelist(){
        const ngoId= parseInt(this.$route.params.list_id)
        await axios.put(`${BASE_URL}/ngolist/${ngoId}`)
      }
    }
      
    }
  </script>