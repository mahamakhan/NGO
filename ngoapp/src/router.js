import { createWebHistory, createRouter } from "vue-router"
import DonationsPage from './components'
import BankAccount from './components'
import NgoList from './components'
import HomePage from './components'
import OneNgo from'./components/OneNgo.vue'
import OneDonation from './components'



const routes = [
    { path: '/', component: HomePage, name: 'HomePage' },
    { path: '/donations', component: DonationsPage, name: 'DonationsPage' },
    { path: '/bankaccount', component: BankAccount, name: 'BankAccount' },
    { path: '/ngolist', component: NgoList, name: 'NgoList' },
    { path: '/donations/:donations_id', component: OneDonation, name: 'OneDonation' },
    { path: '/ngolist/:ngolist_id', component: OneNgo, name: 'OneNgo' }


  ]

  const router = createRouter({
    history: createWebHistory(),
    routes
  })
  
  export default router