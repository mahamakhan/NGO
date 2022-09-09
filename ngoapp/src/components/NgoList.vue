<template>
  <div class="bg-cover bg-gradient-to-r from-rose-400 via-red-500 to-rose-500">
    <div>
        <h1 class="text-5xl font-normal leading-normal mt-0 mb-2 text-white py-10">NGO LIST</h1>
        <div v-for="list in list" :key="list.id" @click='selectngo(list.id)' class="py-12">
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
          <button class="text-white rounded bg-pink-700 px-6 py-4 show-lg hover:bg-pink-400 outline-none active:outline-none focus:outline-none " >Add your NGO</button>
          <div @click="toggleModal()" class=" flex-col justify-center mx-20">
          
        
          
        
          <form  class=" " @submit="createlist">
            <label class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">Name of Your NGO</label>
            <input class=" text-center appearance-none bg-transparent border-b border-teal-500 py-2 w-80 text-gray-700 m-20 py-1 px-2 leading-tight focus:outline-none" placeholder="Name" v-model='newlist.name'/>
            <label class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">Country</label>
            <input class=" text-center appearance-none bg-transparent border-b border-teal-500 py-2 w-80 text-gray-700 m-20 py-1 px-2 leading-tight focus:outline-none" placeholder="Country" v-model='newlist.country'/>
            <label class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white" >Founded</label>
            <input class="text-center appearance-none bg-transparent border-b border-teal-500 py-2 w-80 text-gray-700 m-20 py-1 px-2 leading-tight focus:outline-none" placeholder="founded" v-model='newlist.founded'/>
            <label class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">Email to contact</label>
            <input class="text-center appearance-none bg-transparent border-b border-teal-500 py-2 w-80 text-gray-700 m-20 py-1 px-2 leading-tight focus:outline-none" placeholder="email" v-model='newlist.email'/>
            <label class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">Is it International?</label>
            <input class="text-center appearance-none bg-transparent border-b border-teal-500 py-2 w-80 text-gray-700 m-20 py-1 px-2 leading-tight focus:outline-none" placeholder="international"  v-model='newlist.international'/>
            <label class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">Logo/Video</label>
            <input class="text-center appearance-none bg-transparent border-b border-teal-500 py-2 w-80 text-gray-700 m-20 py-1 px-2 leading-tight focus:outline-none" placeholder="profit/nonprofit"  v-model='newlist.profit'/>
            <button>Add</button>
            </form>
        </div>
      </div>
      </div>
        <h1>You can add your NGO to get donations</h1>
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
          },
          showmodal:false
        
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
    },
    
    toggleModal: function(){
      this.showModal = !this.showModal;
    }
  }
  }
            // console.log(res.data + "create")
            // console.log(this.newlist.name)
    
    // components: { OneNgo },
      
  </script>