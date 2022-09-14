<template>
    <div  class="bg-auto bg-gradient-to-r from-amber-500 via-yellow-700 to-yellow-900 font-bold">
      <h1 class="text-6xl font-normal leading-normal mt-0 mb-2 text-white">About</h1>
      <div class="flex flex-wrap justify-center">
      
        <img src="../bg.png"/>
        <h4 class="text-center text-left text-3xl font-normal leading-normal mt-0 mb-2 text-white">
         
The World Association of Non-Governmental Organizations is a global organization whose mission is to serve its member organizations, strengthen and encourage the non-governmental sector as a whole, increase public understanding of the non-governmental community, and provide the mechanism and support needed for NGOs to connect, partner, and multiply their contributions to solve humanity's basic problems.

        </h4>
      </div>
      
      <h1 class="text-4xl font-normal leading-normal mt-0 mb-2 text-white-300 font-bold" >Here is a list of locations to donate food:</h1>
      <button @click="showlocations()">Show</button>
      <div v-if="locations">
      <div v-for="list in list" :key="list.id" class=" inline-block mx-10 py-12" >
        <h1>{{list.name}}</h1>
      </div>
      </div>
    </div>
    
  </template>
  
  <script>
    import axios from 'axios';
    export default {
      name: 'HomePage',
      data: () => ({
        list: [],
        locations: false
         
        
    }),
    mounted: async function () {
        await this.getlist();
    },
    methods: {
        async getlist() {
            const res = await axios.get('https://www.givefood.org.uk/api/2/locations/');
            this.list = res.data;
            console.log(res.data + "getlist");
        },
        showlocations(){
          this.locations=!this.locations
          console.log(this.locations)
        }
    }}
  </script>