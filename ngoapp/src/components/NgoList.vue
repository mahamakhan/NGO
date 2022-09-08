<template>
  <div class="bg-cover bg-gradient-to-r from-rose-400 via-red-500 to-rose-500">
    <div>
        <h1 class="text-5xl font-normal leading-normal mt-0 mb-2 text-white">NGO LIST</h1>
        <div v-for="list in list" :key="list.id" @click='selectngo(list.id)' class="py-12">
         <h2 class="text-5xl font-normal leading-normal mt-0 mb-2 text-white py-10">{{list.name}}</h2>
         <!-- <video :src='list.profit'/> -->
         <div class="flex flex-row">
         <div>
         <iframe width="560" height="315" :src='list.profit' title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div> 
        <div class="grow">
         <h2  class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white ">{{list.country}}</h2>
          <h2  class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">{{list.founded}}</h2>
          <h2  class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">{{list.international}}</h2>
          <h2 class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">{{list.email}}</h2>
        </div>
        </div>
          <!-- <OneNgo :list='list' /> -->
        </div>
        <div>
          <h1>Add your NGO</h1>
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
    </div>
  </template>
  
  <script>
    import axios from 'axios'
    import { BASE_URL } from '@/globals';
    // import Embed from 'v-video-embed'
    // import  Vue from 'vue';
    
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