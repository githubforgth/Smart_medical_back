// pages/prescribe/prescribe.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    keyword: '', // 搜索关键词
    searchResult: [], // 搜索结果
  },
  onSearchInput: function (e) {
    var keyword = e.detail.value;
    console.log(keyword)
    this.setData({
      keyword: keyword
    });
    this.search(keyword);
  },
  // 发起搜索请求
  search: function (keyword) {
    wx.request({
      url: 'http://127.0.0.1:5000/search_painter',
      data:{
        keyword:keyword 
      },
      success:(res)=>{
        this.setData({
          searchResult:res.data
        })
        console.log(res.data)
      }
    })
  },
  // 监听滚动到底部事件
  onLoadMore: function () {
    // 加载更多搜索结果
    // 将搜索结果添加到 searchResult 变量中
    this.setData({
      searchResult: searchResult.concat(moreSearchResult)
    });
  },

  /**
   * 生命周期函数--监听页面加载
   */
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