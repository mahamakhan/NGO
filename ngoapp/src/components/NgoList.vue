<template>
    <div>
        <h1>NGO LIST</h1>
        <div v-for="list in list" :key="list.id" @click='selectngo(list.id)'>
         <h2>{{list.name}}</h2>
          <h2>{{list.country}}</h2>
          <h2>{{list.city}}</h2>
          <h2>{{list.profit}}</h2>
          <h2>{{list.international}}</h2>
          <h2>{{list.email}}</h2>
          <!-- <OneNgo :list='list' /> -->
        </div>
        <div>
          <form>
            <label>Name of Your NGO</label>
            <input placeholder="Name" vale='name'/>
            <label>Country</label>
            <input placeholder="Country" value='country'/>
            <label>City</label>
            <input placeholder="city" value='city'/>
            <label>Email to contact</label>
            <input placeholder="email" value='email'/>
            <label>Is it International?</label>
            <input placeholder="international" type='radio' value='international'/>
            <label>Is it a non-profit NGO?</label>
            <input placeholder="profit/nonprofit" type='radio' value='profit'/>
            <button>Add</button>
            </form>
        </div>
    </div>
  </template>
  
  <script>
    import axios from 'axios'
    import { BASE_URL } from '@/globals';
// import OneNgo from './OneNgo.vue';
    export default {
    name: "NgoList",
    data: () => ({
        list: []
    }),
    mounted: async function () {
        await this.getlist();
    },
    methods: {
        async getlist() {
            const res = await axios.get(`${BASE_URL}/ngolist/`);
            this.list = res.data;
            console.log(res.data + "getlist");
        },
        selectngo(listid){
        this.$router.push(`/ngolist/${listid}`)
    }
    },
    // components: { OneNgo },
    
}
  </script>