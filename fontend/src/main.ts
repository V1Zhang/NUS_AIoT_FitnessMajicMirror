import { createApp } from 'vue';
import { createPinia } from 'pinia';
import * as ElementPlusIconsVue from '@element-plus/icons-vue';
import App from './App.vue';
import router from './router';
import { usePermissStore } from './store/permiss';
import 'element-plus/dist/index.css';
import './assets/css/icon.css';

import axios from "axios";

// import VueCoreVideoPlayer from 'vue-core-video-player'

axios.defaults.baseURL = "http://localhost:5000"
axios.defaults.headers["Content-Type"] =  "application/json;charset=UTF-8"


const app = createApp(App);
app.use(createPinia());
app.use(router);
// app.use(VueCoreVideoPlayer)

// 注册elementplus图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component);
}
// 自定义权限指令
const permiss = usePermissStore();
app.directive('permiss', {
    mounted(el, binding) {
        if (!permiss.key.includes(String(binding.value))) {
            el['hidden'] = true;
        }
    },
});



app.mount('#app');