<template>
  <div class="bg-auto bg-gradient-to-l from-slate-300 via-slate-600 to-gray-400 ">
<form  class="flex flex-col " @submit="createlist">
            <label class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">Name of Your NGO</label>
            <input class=" text-center appearance-none bg-transparent border-b border-gray-800 py-2 w-3/4 text-white-700 m-20 py-1 px-2 leading-tight focus:outline-none" placeholder="Name" v-model='newlist.name'/>
            <label class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">Country</label>
            <input class=" text-center appearance-none bg-transparent border-b border-gray-800 py-2 w-3/4 text-white-700 m-20 py-1 px-2 leading-tight focus:outline-none" placeholder="Country" v-model='newlist.country'/>
            <label class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white" >Founded</label>
            <input class="text-center appearance-none bg-transparent border-b border-gray-800 py-2 w-3/4 text-white-700 m-20 py-1 px-2 leading-tight focus:outline-none" placeholder="founded" v-model='newlist.founded'/>
            <label class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">Email to contact</label>
            <input class="text-center appearance-none bg-transparent border-b border-gray-800 py-2 w-3/4 text-white-700 m-20 py-1 px-2 leading-tight focus:outline-none" placeholder="email" v-model='newlist.email'/>
            <label class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">Is it International?</label>
            <input class="text-center appearance-none bg-transparent border-b border-gray-800 py-2 w-3/4 text-white-700 m-20 py-1 px-2 leading-tight focus:outline-none" placeholder="international"  v-model='newlist.international'/>
            <label class="text-center text-2xl font-normal leading-normal mt-0 mb-2 text-white">Logo/Video</label>
            <input class="text-center appearance-none bg-transparent border-b border-gray-800 py-2 w-3/4 text-white-700 m-20 py-1 px-2 leading-tight focus:outline-none" placeholder="profit/nonprofit"  v-model='newlist.profit'/>
            <button class="text-white rounded bg-gray-400 px-6 py-4 show-lg hover:bg-gray-600 outline-none active:outline-none focus:outline-none font-bold" @click="goback()">Add</button>
            </form>
          </div>
</template>
<script>
  import axios from 'axios';
  import { BASE_URL } from '@/globals';
export default {
    name: 'FormPage',
    data() {
    return {
      list: [],
      newlist:{
                name:'',
                country:'',
                founded:'',
                email:'',
                international:'',
                profit:''
          },
    }
  },
  methods: {
    async getlist() {
            const res = await axios.get(`${BASE_URL}/ngolist/`);
            this.list = res.data;
            console.log(res.data + "getlist");
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
    goback(){
      this.$router.push("/ngolist/")
    }
  
      
    }
}


</script>