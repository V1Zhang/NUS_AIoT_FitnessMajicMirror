<template>
	<div class="header">
	  <div class="logo"></div>
	  <div class="header-right">
		<div class="header-user-con">
		  <div class="welcome-msg">
			<span class="location">{{ currentLocation }}</span>
			<span class="weather">{{ currentWeather }}</span>
			<span class="date-time">{{ currentDate }} {{ currentDay }} {{ currentTime }}</span>
			Hello, {{ username }}!
		  </div>
		  <!-- 用户名下拉菜单 -->
		  <el-dropdown class="user-name" trigger="click" @command="handleCommand">
			<!-- ... -->
		  </el-dropdown>
		</div>
	  </div>
	</div>
  </template>



<script>
import axios from 'axios'

export default {
  data() {
    return {
	  days: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
      username: 'Zhang V1',
	  currentLocation: 'Beijing',
      currentDate: '',
	  currentDay: '',
      currentTime: '',
      currentWeather: 'Sunny'
    }
  },
  created() {
	this.getCurrentLocation()
    this.getCurrentDateTime()
    this.getCurrentWeather()
    this.updateCurrentTime()
  },
  beforeUnmount() {
    clearInterval(this.intervalId)
  },
  methods: {
    handleCommand(command) {
      if (command === 'loginout') {
        // 退出登录的逻辑
      } else if (command === 'user') {
        // 个人中心的逻辑
      }
    },
    getCurrentDateTime() {
      const currentDate = new Date()
      this.currentDate = currentDate.toLocaleDateString()
	  this.currentDay = this.days[currentDate.getDay()]
      this.currentTime = currentDate.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    },
    updateCurrentTime() {
      this.intervalId = setInterval(() => {
        this.getCurrentDateTime()
      }, 60000)
    },
    getCurrentWeather() {
      // 使用第三方API获取当前天气信息
      axios.get('/api/weather')
        .then(response => {
          this.currentWeather = response.data.weather
        })
        .catch(error => {
          console.error('Error fetching weather:', error)
        })
    },
	getCurrentLocation() {
  // 使用浏览器地理位置API获取当前位置
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      position => {
        // 根据经纬度获取城市信息
        this.fetchLocationData(position.coords.latitude, position.coords.longitude);
      },
      error => {
        console.error('Error getting location:', error);
        this.currentLocation = 'Beijing';
      }
    );
  } else {
    console.error('Geolocation is not supported by this browser.');
    this.currentLocation = 'Beijing';
  }
},

fetchLocationData(latitude, longitude) {
  axios.get(`/api/location?lat=${latitude}&lon=${longitude}`)
    .then(response => {
      this.currentLocation = response.data.city;
    })
    .catch(error => {
      console.error('Error fetching location:', error);
      this.currentLocation = '无法获取城市信息';
    });
}
  }
}
</script>




<style scoped>
.header {
	position: relative;
	box-sizing: border-box;
	width: 100%;
	height: 70px;
	font-size: 22px;
	color: #fff;
}
.collapse-btn {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 100%;
	float: left;
	padding: 0 21px;
	cursor: pointer;
}
.header .logo {
	float: left;
	width: 250px;
	line-height: 70px;
}
.header-right {
	float: right;
	padding-right: 50px;
}
.header-user-con {
	display: flex;
	height: 70px;
	align-items: center;
}
.btn-fullscreen {
	transform: rotate(45deg);
	margin-right: 5px;
	font-size: 24px;
}
.btn-bell,
.btn-fullscreen {
	position: relative;
	width: 30px;
	height: 30px;
	text-align: center;
	border-radius: 15px;
	cursor: pointer;
	display: flex;
	align-items: center;
}
.btn-bell-badge {
	position: absolute;
	right: 4px;
	top: 0px;
	width: 8px;
	height: 8px;
	border-radius: 4px;
	background: #f56c6c;
	color: #fff;
}
.btn-bell .el-icon-lx-notice {
	color: #fff;
}
.user-name {
	margin-left: 10px;
}
.user-avator {
	margin-left: 20px;
}
.el-dropdown-link {
	color: #fff;
	cursor: pointer;
	display: flex;
	align-items: center;
}
.el-dropdown-menu__item {
	text-align: center;
}
.welcome-msg {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}
.welcome-msg > span {
  margin: 0 10px;
}
</style>













