const app = getApp()
/*
1. 新增患者接口
2.待回复接口
3.现有患者接口
*/
Page({
      data: {
          indicatorDots: true,
          vertical: false,
          autoplay: true,
          interval: 3000,
          duration: 1000,
          loadingHidden: false,  // loading
          List:[],
          patient_new_num: 0,
          patient_reply: 0,
          patient_sum_num: 0,
          name_info:"",  //姓名
          motto_info: "",  //格言
          gender: "",        //性别
          todo_item:"" ,    //  待办
          headshot:""//头像
      },
  
      //事件处理函数
      swiperchange: function(e) {
          //console.log(e.detail.current)
      },
  
      onLoad: function() {
      wx.request({
        url: 'http://127.0.0.1:5000/todolist',
        success:res=>{
          this.setData({todo_item: res.data.todo_item})
        }
      })
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
        wx.request({
          url: 'http://127.0.0.1:5000/show_medical',
         success: (res) =>  {
           var temp = res.data
          this.setData({List:temp});
          console.log(this.data.List); //返回的数据
        }
      }) 
      },
    //获取当前滑块的index
    bindchange:function(e){
      const that  = this;
      that.setData({
        currentData: e.detail.current
      })
    },
    //点击切换，滑块index赋值
    checkCurrent:function(e){
      const that = this;
   
      if (that.data.currentData === e.target.dataset.current){
          return false;
      }else{
   
        that.setData({
          currentData: e.target.dataset.current
        })
      }
    },
    to_prescribe:function(){
      wx.navigateTo({
        url: '../prescribe/prescribe',
      })
    },
    to_medical:function(e){
      var medical_id = e.currentTarget.dataset.id;
      wx.navigateTo({
        url: '../medical_records/medical_records?id=' + medical_id,
      })
    },
  //跳转至MINE
  to_mine: function(){
    wx.navigateTo({
      url: '../mine/mine',
    })
  },
  to_chat: function(){
    wx.navigateTo({
      url: '../chat/chat',
    })
  }
})