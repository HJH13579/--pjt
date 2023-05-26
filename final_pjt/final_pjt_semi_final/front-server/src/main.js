import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import './assets/global.css'

// import { library } from '@fortawesome/fontawesome-svg-core'
// import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
// import { faHeart } from '@fortawesome/free-solid-svg-icons'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// library.add(faHeart);
// Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.config.productionTip = false
Vue.use(BootstrapVue)
new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
