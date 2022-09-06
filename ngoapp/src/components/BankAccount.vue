<template>
    <div>
        <h1>Bank Account</h1>
    </div>
    <div v-for="bank in banks" :key="bank.id">
    <h2>{{bank.name}}</h2>
    <h2>{{bank.iban}}</h2>
    <h2>{{bank.number}}</h2>
    </div>
  </template>
  
  <script>
    import axios from 'axios'
    import { BASE_URL } from '@/globals';
    export default {
      name: 'BankAccount',
      data: () =>({
        banks:[]
      }),
      mounted: async function () {
        await this.getbank();
      },
      methods:{
        async getbank(){
          const res= await axios.get(`${BASE_URL}/bankaccount/`)
          this.banks=res.data
          console.log(res.data+ 'getbank')
        }
      }
    }
  </script>