// app.js
App({
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
    wx.cloud.init({
      env:"cloud1-7g5w3ge28dc53a19"
    })
    if(wx.getStorageSync('userInfo')){
      this.globalData.userInfo = wx.getStorageSync('userInfo')
      console.log('get storage')
    }
  },
  

  globalData: {
    userInfo: null
  }
})
