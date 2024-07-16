<template>
    <div>
      <img :src="videoUrl" alt="Video Stream" />
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        videoUrl: 'http://172.20.10.10:7777/video',
      };
    },
  };
  </script>
  
  <style scoped>
  img {
    width: 100%;
    height: auto;
  }
  </style>
  