<template>
    <div>
        <h1>NGO LIST</h1>
        <div>
          <form>
            <input placeholder="Name"/>
            <input placeholder="Country"/>
            <button>Add</button>
            </form>
        </div>
    </div>
  </template>
  
  <script>
    import axios from 'axios'
    import { BASE_URL } from '@/globals';
    export default {
      name: 'NgoList',
      data: () =>({
        list:[]
      }),
      mounted: async function () {
        await this.getlist();
      },
      methods:{
        async getlist(){
          const res= await axios.get(`${BASE_URL}/ngolist/`)
          this.list=res.data
          console.log(res.data+ 'getlist')
        }
      }
      
    }
  </script>