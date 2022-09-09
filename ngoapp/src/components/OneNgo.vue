<template>
  <div class="bg-cover bg-gradient-to-r from-rose-400 via-red-500 to-rose-500">
    <div>
        <!-- <h1>NGO</h1> -->
        <h2 class="text-5xl font-normal leading-normal mt-0 mb-2 text-white pb-14"> Name:{{ngoDetails.name}}</h2>
        <iframe class="ml-20" width="800" height="715" :src="ngoDetails.profit"/>
          <h2 class="text-5xl font-normal leading-normal mt-0 mb-2 text-white pb-14">Country:{{ngoDetails.country}}</h2>
          <h2 class="text-5xl font-normal leading-normal mt-0 mb-2 text-white pb-14">Founded in:{{ngoDetails.founded}}</h2>
          <h2 class="text-5xl font-normal leading-normal mt-0 mb-2 text-white pb-14">Local/International:{{ngoDetails.international}}</h2>
          <h2 class="text-5xl font-normal leading-normal mt-0 mb-2 text-white pb-14">Contact:{{ngoDetails.email}}</h2>
    </div>
    <button @click="deletelist()" class="text-red-900 border border-red-380 hover:bg-red-400 hover:text-white active:bg-red-600 font-bold uppercase text-sm px-6 py-3 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button">Remove</button>
    <div class="flex items-center border-b border-teal-500 py-2">
     
      <form @submit="changelist">
            <label>Name of Your NGO:</label>
            <input class="text-center appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" placeholder="Name" v-model='newlist.name'/>
            <label>Country:</label>
            <input class="text-center appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" placeholder="Country" v-model='newlist.country'/>
            <label>Founded:</label>
            <input class="text-center appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" placeholder="founded" v-model='newlist.founded'/>
            <label>Email/contact:</label>
            <input class="text-center appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" placeholder="email" v-model='newlist.email'/>
            <label>Is it International?</label>
            <input class="text-center appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" placeholder="international"  v-model='newlist.international'/>
            <label>Logo/Video</label>
            <input class="text-center appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" placeholder="profit/nonprofit"  v-model='newlist.profit'/>
            <button  class="text-red-900 border border-red-380 hover:bg-red-400 hover:text-white active:bg-red-600 font-bold uppercase text-sm px-6 py-3 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button">Edit</button>
            </form>

    </div>
  </div>
  </template>
  
  <script>
    import axios from 'axios';
    import { BASE_URL } from '@/globals';
    export default {
      name: 'OneNgo',
      
      data: () => ({
      ngoDetails: {},
      newlist:{
                name:'',
                country:'',
                founded:'',
                email:'',
                international:'',
                profit:''
          }
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
        await axios.put(`${BASE_URL}/ngolist/${ngoId}`,this.newlist).then(
        response => {
        this. newlist= response.data;
          console.log(this.newlist)})
      },
      async deletelist(){
        const ngoId= parseInt(this.$route.params.list_id)
        await axios.delete(`${BASE_URL}/ngolist/${ngoId}`)
        this.$router.push("/ngolist/")
    }
  }
    }
  </script>