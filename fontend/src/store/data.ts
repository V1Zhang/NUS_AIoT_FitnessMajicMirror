import { defineStore } from 'pinia'; // 前端状态管理
export const useMainStore = defineStore('myStore', {
	state: () => {
        return {
            videoPopUrl: "https://cn-hk-eq-01-10.bilivideo.com/upgcxcode/71/12/1158901271/1158901271-1-192.mp4?e=ig8euxZM2rNcNbRV7WdVhwdlhWdBhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1721127940&gen=playurlv2&os=bcache&oi=729892153&trid=00001f4fded7121e43358d7ef7ce1f315b37T&mid=3546712159291839&platform=html5&og=cos&upsig=61932c241c510493aae8565e4a2732ea&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=68704&bvc=vod&nettype=0&bw=105459&orderid=0,1&buvid=&build=0&mobi_app=&f=T_0_0&logo=80000000",
            username:"",
            text:"",
        }
    },
actions: {
    login(message: { username: string }){
        this.username = message.username
    },
    update(message: { text: string }){
        this.text = message.text
    },
    async fetchText() {
        try {
          const res = await fetch('http://127.0.0.1:5000/vueflask');
          this.text = await res.text(); 
        } catch (error) {
          console.error('Error fetching text:', error);
        }
      },
    }
});

