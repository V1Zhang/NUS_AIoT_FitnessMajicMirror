<template>
    <div id="page_container">
      <h2 v-if="textContent">{{ textContent }}</h2>
      <div id="image-container">
        <img :src="imageData" alt="Backend Image" v-if="imageData" />
        <audio :src="audioData" controls v-if="audioData"></audio>
        <p v-else>Loading...</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        imageData: null,
        textContent: '',
        audioData: null
      }
    },
    mounted() {
      this.fetchImageData()
    },
    methods: {
      fetchImageData() {
        axios.get('/api/image')
          .then(response => {
            this.imageData = response.data.imageData;
            this.textContent = response.data.textContent;
            this.audioData = response.data.audioData;
          })
          .catch(error => {
            console.error('Error fetching image:', error)
          })
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
  justify-content: center;
  align-items: center;
}

#h2 {
  margin-top: 0;
  margin-bottom: 20px;
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  color: #333;
}

#audio {
  width: 100%;
  margin-top: 20px;
}

#image-container {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  width: 500px; /* 设置小窗口的宽度 */
  height: 400px; /* 设置小窗口的高度 */
}

#image-container img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}
  </style>