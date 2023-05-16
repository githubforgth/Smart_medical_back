// pages/mine/mine.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    name_info:"",  //姓名
    motto_info: "",  //格言
    gender: "",        //性别
    todo_item:"" ,    //  待办
    headshot:""//头像
  },
to_settings:function(){
  wx.navigateTo({
    url: '/pages/mine/person-info-settings/person-info-setting',
  })
},
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    wx.request({
      url: 'http://127.0.0.1:5000/doctor_info',
      success:(res)=>{
        this.setData({
          name_info: res.data.name,
          motto_info: res.data.motto,
          gender: res.data.gender,
          headshot: res.data.headshot
        });
        console.log(this.data.name_info)
      }
    })

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