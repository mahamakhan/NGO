<template>
    <div>
        <h1>Bank Account</h1>
    </div>
  </template>
  
  <script>
    import axios from 'axios'
    import { BASE_URL } from '@/globals';
    export default {
      name: 'BankAccount',
      data: () =>({
        bank:[]
      }),
      mounted: async function () {
        await this.getbank();
      },
      methods:{
        async getbank(){
          const res= await axios.get(`${BASE_URL}/bankaccount/`)
          this.bank=res.data
          console.log(res.data+ 'getbank')
        }
      }
    }
  </script>