<template>
  <div id="page_container" style="text-align: center; padding: 5px;">
    <div class="action-list">
      <div
        v-for="action in actions"
        :key="action.id"
        class="action-item"
        :class="{ 'active': selectedAction === action }"
        @mouseenter="selectAction(action)"
        @mouseleave="deselectAction(action)"
        @click="handleActionClick(action)"
        :data-id="action.id"
        :style="{ backgroundColor: action === selectedAction ? ' #191970' : '#FFFFFF', color: action === selectedAction ? 'white' : '#000000'}"
      >
        <button class="action-image">
          <img :src="action.imageUrl" :alt="action.name">
        </button>
        <div class="action-text">{{ action.name }}</div>
      </div>
    </div>
  </div>
</template>

  <script>
  import axios from 'axios'
  import img1 from '../assets/img/foream_plank.png'
  import img2 from '../assets/img/push_up.png'
  import img3 from '../assets/img/sumo_glute_bridge.png'
  import img4 from '../assets/img/lying_leg_raise.png'
  import {useMainStore} from '../store/data.ts';
  const mainStore = useMainStore()

  export default {
    data() {
      return {
        selectedAction: null,
        actions: [
          {
            id: 1,
            name: 'Foream Plank',
            imageUrl: img1
          },
          {
            id: 2,
            name: 'Push-up',
            imageUrl: img2
          },
          {
            id: 3,
            name: 'Sumo Glute Bridge',
            imageUrl: img3
          },
          {
            id: 4,
            name: 'Lying Leg Raise',
            imageUrl: img4
          }
        ]
      }
    },
    methods: {
        selectAction(action) {
      this.selectedAction = action;
    },
    deselectAction(action) {
      if (this.selectedAction === action) {
        this.selectedAction = null;
      }
    },
    handleActionClick(action) {
      console.log(`Selected action: ${action.name}`);
      axios.post('/vueflask', { actionId: action.id })
      .then(response => {
        console.log(response.data)

        mainStore.update({ text: response.data.text });
        
        // this.textContent = response.data.text; // 保存文本内容
        // this.imageData = 'data:image/png;base64,' + response.data.image; // 保存图像数据
        this.$router.push('/interaction');
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }
  }
}
  </script>
  
  <style scoped>

  #page_container {
    background: url("../assets/img/bg.png") center; /* 增加背景图 */
    background-size: 100% auto; /* 设置背景的大小 */
    background-repeat: no-repeat; /* 将背景设置为不重复显示 */
    background-position: center; /* 将背景图片居中显示 */
    background-repeat: no-repeat; /* 背景图片不重复 */
    height: 100vh; /* 设置容器高度为视口高度 */
    display: flex;
    justify-content: center;
    align-items: center;
  }


  .action-list {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .action-item {
    width: 250px; 
    border: 3px solid #FFFFFF; /* 设置按钮的边界粗细和颜色 */
    margin-top: 18px; /* 设置合适的上部外框的宽度 */
    text-align: center;
    font-size: 15px; /* 修改按钮文字的大小 */
    color: #FFFFFF;
    line-height: 30px;
    border-radius: 30px; /* 将按钮的左右边框设置为圆弧 */
    cursor: pointer;
    display: flex;
    align-items: center;/* 垂直居中 */
    padding: 10px;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
  }
  
  .action-image {
    width: 50px;
    height: 50px;
    margin-right: 20px;
  }
  
  .action-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .action-text {
    font-size: 18px;
    font-weight: bold;
  }
  </style>