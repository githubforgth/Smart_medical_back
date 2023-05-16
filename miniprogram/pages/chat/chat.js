Page({
  onSubmit: function(event) {
    wx.request({
      url: 'http://localhost:5000/send_message',
      method: 'POST',
      data: event.detail.value,
      success: function(res) {
        console.log(res.data)
      }
    })
  }
})
