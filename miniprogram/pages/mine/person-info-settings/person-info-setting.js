// pages/person-info-settings/person-info-setting.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    user:{
      headshot:'https://img.wxcha.com/m00/65/4e/89433954b6fdfacab88ffcdb8e84158e.jpg',
      name: '高泰恒',
      gender:'男',
      title:"光头大主管",
      department:"内科"
    }
  },

  /**
   * 生命周期函数--监听页面加载
   */onUsernameInput: function(e) {
    // 更新 username 变量的值
    this.setData({
      username: e.detail.value
    })
  },
  onLoad(options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})