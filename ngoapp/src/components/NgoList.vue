<template>
    <div>
        <h1>NGO LIST</h1>
        <div v-for="list in list" :key="list.id" @click='selectngo(list.id)'>
         <h2>{{list.name}}</h2>
          <h2>{{list.country}}</h2>
          <h2>{{list.founded}}</h2>
          <h2>{{list.profit}}</h2>
          <h2>{{list.international}}</h2>
          <h2>{{list.email}}</h2>
          <!-- <OneNgo :list='list' /> -->
        </div>
        <div>
          <form @submit="createlist">
            <label>Name of Your NGO</label>
            <input placeholder="Name" v-model='newlist.name'/>
            <label>Country</label>
            <input placeholder="Country" v-model='newlist.country'/>
            <label>Founded</label>
            <input placeholder="founded" v-model='newlist.founded'/>
            <label>Email to contact</label>
            <input placeholder="email" v-model='newlist.email'/>
            <label>Is it International?</label>
            <input placeholder="international"  v-model='newlist.international'/>
            <label>Is it a non-profit NGO?</label>
            <input placeholder="profit/nonprofit"  v-model='newlist.profit'/>
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
        list: [],
          newlist:{
                name:'',
                country:'',
                founded:'',
                email:'',
                international:'',
                profit:''
          }
        
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
    },
         async createlist() {
         await axios.post(`${BASE_URL}/ngolist/`,
            this.newlist).then(
        response => {
          this. newlist= response.data;
          this.list.push(response.data);
        }
      );
    }
            // console.log(res.data + "create")
            // console.log(this.newlist.name)
    }
    // components: { OneNgo },
    }    
  </script>