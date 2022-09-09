<template>
    <div class="bg-auto bg-gradient-to-l from-cyan-300 via-blue-700 to-sky-400">
      <div>
        <h1 class="text-6xl font-normal leading-normal mt-0 mb-2 text-white">Bank Accounts</h1>
    </div>
    <div  class=" py-20" v-for="bank in banks" :key="bank.id">
    <h2 class="text-center text-left text-3xl font-normal leading-normal mt-0 mb-2 text-white">Bank Name:{{bank.name}}</h2>
    <h2 class="text-center text-left text-2xl font-normal leading-normal mt-0 mb-2 text-white">IBAN:{{bank.iban}}</h2>
    <h2 class="text-center text-left text-2xl font-normal leading-normal mt-0 mb-2 text-white">Account Number:{{bank.number}}</h2>
    </div>
   
  </div>
  </template>
  
  <script>
    import axios from 'axios'
    import { BASE_URL } from '@/globals';

    export default {
    name: "BankAccount",
    data: () => ({
        banks: []
    }),
    mounted: async function () {
        await this.getbank();
    },
    methods: {
        async getbank() {
            const res = await axios.get(`${BASE_URL}/bankaccount/`);
            this.banks = res.data;
            console.log(res.data + "getbank");
        }
    }
}
  </script>