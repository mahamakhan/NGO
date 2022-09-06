<template>
    <div>
        <h1>NGO LIST</h1>
        <div v-for="list in list" :key="list.id">
          <h2>{{list.name}}</h2>
          <h2>{{list.country}}</h2>
          <h2>{{list.city}}</h2>
          <h2>{{list.profit}}</h2>
          <h2>{{list.international}}</h2>
          <h2>{{list.email}}</h2>
        </div>
        <div>
          <form>
            <label>Name of Your NGO</label>
            <input placeholder="Name"/>
            <label>Country</label>
            <input placeholder="Country"/>
            <label>City</label>
            <input placeholder="city"/>
            <label>Email to contact</label>
            <input placeholder="email"/>
            <label>Is it International?</label>
            <input placeholder="international" type='radio'/>
            <label>Is it a non-profit NGO?</label>
            <input placeholder="profit/nonprofit" type='radio'/>
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