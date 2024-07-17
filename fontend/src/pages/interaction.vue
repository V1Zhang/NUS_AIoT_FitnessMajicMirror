<template>
  <div>
  <v-header />
  <div id="page_container">
    <p class="custom-text">{{ text }}</p>
    <div id="image-container">
      <v-video />
    </div>
  </div>

  <div class="popVideo" id="popVideoBox" @mousemove.stop="mousemove" @mouseleave.stop="mouseleave">
      <div class="open" v-open></div>
      <div class="drag" v-drag>
        <div class="videoPop">
          <div v-show="replaceIcon" class="videoReplay" @click="changeVideoId">替换</div>
          <div class="closeVideo" @click="close"></div>
        </div>
        <vue-aliplayer-v2 class="aliplayerCon" :source="modelVideoUrl" 
                  ref="popVideo"
                  :options="options"
                  @snapshoted="snapshoted"/>

      </div>
    </div>
</div>
</template>
  
  <script>
  import {useMainStore} from '../store/data';
  import vHeader from '../components/header.vue';
  import vVideo from '../components/video.vue';
  const mainStore = useMainStore()
  export default {
    directives: {
    // 拖拽
    drag(el) {
      var odiv = document.getElementById("popVideoBox")
      el.onmousedown = function (eve) {
        eve = eve || window.event;
        var clientX = eve.clientX;
        var clientY = eve.clientY;
        var odivX = odiv.offsetLeft;
        var odivY = odiv.offsetTop;
        var odivLeft = clientX - odivX;
        var odivTop = clientY - odivY;
        var clientWidth = document.documentElement.clientWidth;
        var oWidth = odiv.clientWidth;
        var odivRight = clientWidth - oWidth;
        var clientHeight = document.documentElement.clientHeight;
        var oHeight = odiv.clientHeight;
        var odivBottom = clientHeight - oHeight;
        document.onmousemove = function (e) {
          //e.preventDefault();
          var left = e.clientX - odivLeft;
          if (left < 0) {
            left = 0
          }
          if (left > odivRight) {
            left = odivRight
          }
          var Top = e.clientY - odivTop;
          if (Top < 0) {
            Top = 0
          }
          if (Top > odivBottom) {
            Top = odivBottom
          }
          odiv.style.left = left + "px";
          odiv.style.top = Top + "px";
        }
        document.onmouseup = function () {
          document.onmouseup = "";
          document.onmousemove = "";
        }
      }
    },
    // 放大缩小
    open: function (el) {
      //当被绑定的元素插入到 DOM 中时 放大缩小
      el.onmousedown = function (e) {
        //鼠标按下，计算当前元素距离可视区的距离
        var x = e.clientX - el.offsetLeft;
        var y = e.clientY - el.offsetTop;
        document.onmousemove = function (eve) {
          console.log(y)
          console.log(x)
          //设置宽高
          document.getElementById("popVideoBox").style.height = -y + eve.clientY + "px"
          if (document.getElementById("popVideoBox").offsetHeight > document.body.offsetHeight) {
            document.getElementById("popVideoBox").style.height = document.body.offsetHeight + "px"
          } else if (document.getElementById("popVideoBox").offsetHeight < 150) {
            document.getElementById("popVideoBox").style.height = 150 + "px"
          }
          document.getElementById("popVideoBox").style.width = -x + eve.clientX + "px"
          if (document.getElementById("popVideoBox").offsetWidth > document.body.offsetWidth) {
            document.getElementById("popVideoBox").style.width = document.body.offsetWidth + "px"
          } else if (document.getElementById("popVideoBox").offsetWidth < 150) {
            document.getElementById("popVideoBox").style.width = 150 + "px"
          }
        }
        document.onmouseup = function () {
          document.onmousemove = null;
          document.onmouseup = null;
        }
      }
    }
  },

  components: {
    vHeader,
    vVideo
  },
  data() {
    return {
      modelVideoUrl: "https://cn-hk-eq-01-10.bilivideo.com/upgcxcode/71/12/1158901271/1158901271-1-192.mp4?e=ig8euxZM2rNcNbRV7WdVhwdlhWdBhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1721127940&gen=playurlv2&os=bcache&oi=729892153&trid=00001f4fded7121e43358d7ef7ce1f315b37T&mid=3546712159291839&platform=html5&og=cos&upsig=61932c241c510493aae8565e4a2732ea&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=68704&bvc=vod&nettype=0&bw=105459&orderid=0,1&buvid=&build=0&mobi_app=&f=T_0_0&logo=80000000",
      videoPopUrl: '', // 初始化视频地址为空
      options: {},    // 初始化视频播放选项
      replaceIcon: false, // 根据需要初始化替换图标的显示状态
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
  mounted() {
        this.store.fetchText()
        this.playVoice();
      },
  methods: {
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
  height: 92vh;
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
  margin-top: 0px;
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

/* 视频弹窗样式 */
.popVideo {

  position: absolute;
  float: left;
  width: 2.22rem;
  height: 1.72rem;
  left: 60%;
  top: 1rem;
  z-index: 9999;
  background-color: #fff; /*设置背景色为白色 */
}
 
.open {
  position: absolute;
  cursor: se-resize;
  height: 0.1rem;
  width: 0.1rem;
  bottom: 0;
  right: 0;
  z-index: 132;
 
}
 
.drag {
  position: absolute;
  position: center;
  width: 100%;
  height: 100%;
  padding: 0px;
  z-index: 125;
}
  </style>