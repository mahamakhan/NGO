import { createWebHistory, createRouter } from "vue-router"
import DonationsPage from './components/DonationsPage.vue'
import BankAccount from './components/BankAccount.vue'
import NgoList from './components/NgoList.vue'
import HomePage from './components/HomePage.vue'
import OneNgo from'./components/OneNgo.vue'
import OneDonation from './components/OneDonation.vue'



const routes = [
    { path: '/', component: HomePage, name: 'HomePage' },
    { path: '/donations', component: DonationsPage, name: 'DonationsPage' },
    { path: '/bankaccount', component: BankAccount, name: 'BankAccount' },
    { path: '/ngolist', component: NgoList, name: 'NgoList' },
    { path: '/donations/:donations_id', component: OneDonation, name: 'OneDonation' },
    { path: '/ngolist/:list_id', component: OneNgo, name: 'OneNgo' }


  ]

  const router = createRouter({
    history: createWebHistory(),
    routes
  })
  
  export default router