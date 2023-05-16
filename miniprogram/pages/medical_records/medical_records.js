// 病历信息页面的控制代码
const app = getApp()
Page({
  /**
   * 页面的初始数据
   */
  data: {
    record: {}, // 病历数据对象
    medical_info:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var medical_id = options.id;
    // 根据id查询病历详细信息
    wx.request({
      url: 'http://127.0.0.1:5000/medical_info',
      data:{
        id: options.id
      },
      success:(res)=>{
        this.setData({
          medical_info: res.data
        })
      },
    })
  }
})
