import { defineStore } from 'pinia'; // 前端状态管理
export const useMainStore = defineStore('myStore', {
	state: () => {
        return {
            text:"",
        }
    },
actions: {
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

