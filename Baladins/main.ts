import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue' // pourquoi une erreur ? ¯\_(ツ)_/¯
import router from '@/router'

createApp(App).use(router).mount('#app')
