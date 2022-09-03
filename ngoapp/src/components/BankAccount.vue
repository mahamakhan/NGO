<template>
    <div>
        <h1>Bank Account</h1>
    </div>
  </template>
  
  <script>
    import axios from 'axios'
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
          const res= await axios.get('http://127.0.0.1:8000/bankaccount/')
          this.bank=res.data
          console.log(res.data+ 'getbank')
        }
      }
    }
  </script>