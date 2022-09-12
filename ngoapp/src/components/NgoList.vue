<template>
  <div class="bg-cover bg-gradient-to-r from-rose-400 via-red-500 to-rose-500 ">
    <div>
        <h1 class="text-5xl font-normal leading-normal mt-0 mb-2 text-white py-10 font-bold font-bold">NGO LIST</h1>
        <div v-for="list in list" :key="list.id" @click='selectngo(list.id)' class="py-12 ">
         <h2 class="text-5xl font-normal leading-normal mt-0 mb-2 text-white pb-14">{{list.name}}</h2>
         <!-- <video :src='list.profit'/> -->
         <div class="flex flex-row">
         <div>
         <iframe class="justify-center ml-8" width="560" height="315" :src='list.profit' title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div> 
        <div class="grow">
         <h2  class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white ">Headquarters:  {{list.country}}</h2>
          <h2  class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">Founded in:  {{list.founded}}</h2>
          <h2  class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">International/Local:  {{list.international}}</h2>
          <h2 class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">Contact:  {{list.email}}</h2>
        </div>
        </div>
          <!-- <OneNgo :list='list' /> -->
        </div>

        <div>
          <button @click="toggleModal" class="text-white rounded bg-red-300 px-6 py-4 show-lg hover:bg-red-900 outline-none active:outline-none focus:outline-none " >Add your NGO</button>
          
          
          
        
          
        
          
        
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
         
    
    toggleModal: function(){
      this.$router.push('/ngolist/form');
    }
  }
  }
            // console.log(res.data + "create")
            // console.log(this.newlist.name)
    
    // components: { OneNgo },
      
  </script>