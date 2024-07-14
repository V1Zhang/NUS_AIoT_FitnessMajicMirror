<template>
  <div id="page_container">
    <p class="custom-text">{{ text }}</p>
    <div id="image-container">
      <img src="../assets/img/example.jpg" alt="Backend Image" />
    </div>
  </div>
</template>
  
  <script>
  import {useMainStore} from '../store/data';
  export default {
  data() {
    return {
      store: useMainStore()
    }
  },
  computed: {
    text() {
      return this.store.text
    }
  },
  watch: {
    text() {
      this.playVoice();
    }
  },
    methods: {
      mounted() {
        this.store.fetchText()
        this.playVoice();
      },
      playVoice() {
        this.handleSpeak(this.text)
      },
      handleSpeak(text){
        const synth = window.speechSynthesis;
        const msg = new SpeechSynthesisUtterance();
        msg.text = text;
        msg.lang = "zh-CN"; //使用的语言
        msg.volumn = 1; //声音音量
        msg.rate = 1; //语速
        msg.pitch = 1; //音高
        synth.speak(msg); //播放
      }
    }
  }
  </script>
  
  <style scoped>
  #page_container {
  background: url("../assets/img/bg.png") center;
  background-size: cover;
  background-repeat: no-repeat;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.custom-text {
  font-family: 'Arial', sans-serif;
  font-size: 18px;
  font-weight: bold;
  color: white;
  text-align: right;
  margin-top: 20px;
  padding: 10px;
  border-radius: 5px;
}

  #image-container {
    background-color: white;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    width: 500px; /* 设置小窗口的宽度 */
    height: 400px; /* 设置小窗口的高度 */
    display: flex;
    justify-content: center;
    align-items: center;
  }

#image-container img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}
  </style>