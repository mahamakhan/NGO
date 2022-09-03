<template>
    <div>
        <h1>Donations</h1>
    </div>
  </template>
  
  <script>
    import axios from 'axios'
    export default {
      name: 'DonationsPage',
      data: () =>({
        donations:[]
      }),
      mounted: async function () {
        await this.getDonations();
      },
      methods:{
        async getDonations(){
          const res= await axios.get('http://127.0.0.1:8000/donations')
          this.donations=res.data
          console.log(res.data+ 'getDonations')
        }
      }
      
    }
  </script>