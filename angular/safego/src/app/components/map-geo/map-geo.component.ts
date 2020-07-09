import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpClientModule, HttpHeaders } from '@angular/common/http'
import { Address } from '../address/address';
import { Question } from '../question/question'
import { ClassStmt } from '@angular/compiler';
import { ReplaySubject } from 'rxjs';

declare const AMapUI: any;
declare const AMap: any;

@Component({
  selector: 'app-map-geo',
  templateUrl: './map-geo.component.html',
  styleUrls: ['./map-geo.component.css']
})
export class MapGeoComponent implements OnInit {

  public show = '';
  public active = true;
  public address = '天安门';
  public detail:any = {
    detail_address: '',
    lnglat: ''
  }
  public risk = '';
  public answer = '';

  map:any;
  mapObj: any;
  infoWindow: any;
  getlnglatPoint:any;

  constructor(public http:HttpClient) {
  }

  //获取经纬度
  arrdes = this.GetQueryString("lnglat");
  //获取站点名称
  siteName = this.GetQueryString("siteNaem");
  //站点负责人
  WorkerName = this.GetQueryString("WorkerName");
  //获取站点具体地址
  FullName = this.GetQueryString("FullName");

  GetQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) {
        var value = unescape(r[2]);
        //去掉最后一个字符，是一个，号
        value = value.substr(0, value.length - 1);

        //定义一个数组来存放传过来的所有参数
        var Arrvalue = [];
        //给arrdes赋值  string2Array方法下面有说明
        Arrvalue = this.string2Array(value);
        return Arrvalue;
    } else {
        return null;
    }
  }

  //将字符转换为数组的方法,去除分割标志
  string2Array(stringObj) {
      stringObj = stringObj.replace(/\[([\w, ]*)\]/, "$1");
      if (stringObj.indexOf("[") == 0) {// if has chinese
          stringObj = stringObj.substring(1, stringObj.length - 1);
      }
      var arr = stringObj.split("p");    //------------     !!!!!!!!!!!!注意：分割标志p
      var newArray = []; //new Array();
      for (var i = 0; i < arr.length; i++) {
          var arrOne = arr[i];
          newArray.push(arrOne);
      }
      // console.log(newArray);
      return newArray;
  };

  ngOnInit() {
    this.getMap();
    this.mapObj = new AMap.Map('iCenter');

    this.map.on('click', e => {
      //(<HTMLInputElement>document.getElementById("lnglat")).value = e.lnglat.getLng() + ',' + e.lnglat.getLat();
      (<HTMLInputElement>document.getElementById("key_11")).value = e.lnglat.getLng();
      (<HTMLInputElement>document.getElementById("key_12")).value = e.lnglat.getLat();
      this.detail.lnglat = e.lnglat.getLng() + ',' + e.lnglat.getLat();
      this.geocoder2();
      this.detail.detail_address = (<HTMLInputElement>document.getElementById("tipinput")).value;
    });

  }

  getMap() {
    this.map =  new AMap.Map('container', {
      resizeEnable: true,              //是否监控地图容器尺寸变化，默认值为false
      zoom: 13,                        //初始化大小，从国到街为3-18
      center: [116.397428, 39.90923]   //初始化中心点，传入经纬度
    });

    this.infoWindow = new AMap.InfoWindow({ offset: new AMap.Pixel(0, -30) });
    if(this.arrdes != null){
      for (var i = 0, marker; i < this.arrdes.length; i++) {
        //定义经度
        var lng = "";
        //定义纬度
        var lat = "";
        //把数组里面的经纬度转换成字符串
        var lnglat = this.arrdes[i] + "";
        //给经度赋值 从0开始到，结束
        lng = lnglat.substr(0, lnglat.indexOf(","));
        //给纬度赋值   从，后一位开始到数组的总长结束
        lat = lnglat.substr(lnglat.indexOf(',') + 1, lnglat.length - 1);
        //添加一个点，
        var marker = new AMap.Marker({
            //点的位置，从上面赋值，直接赋数组的值是无法得到的，所有东西弄了可能有12个小时，这里占了10个小时
            position: [lng, lat],
            map: this.map //地图，就是最开始创建的地图
        });
        //这里的content是信息框里面的内容，可以用js拼接成想要的样式或格式
        marker.content =
        '<div class="info-title">名称：' + this.siteName[i] + '</div><div class="info-content">' +
        '<img src="http://webapi.amap.com/images/amap.jpg">' +
        '负责人：' + this.WorkerName[i] + '<br/>' +
        '地址：' + this.FullName[i] + '</div>';
        ;
        //添加点的单击事件
        marker.on('click', this.markerClick);
        marker.emit('click', { target: marker });
      }
    }

    //定义需要的地图控件，类似于实例化一个对象
    AMap.plugin(['AMap.ToolBar', 'AMap.Scale', 'AMap.OverView', 'AMap.MapType', 'AMap.Geolocation'],
    //添加地图控件 若不需要，可直接删除代码
    () => {
      //集成了缩放、平移、定位等功能按钮在内的组合控件  界面操作集成(鼠标右键双击缩小，鼠标左键双击放大，移动，鼠标滑轮缩放)
      this.map.addControl(new AMap.ToolBar());

      //展示地图在当前层级和纬度下的比例尺 左下
      this.map.addControl(new AMap.Scale());

      //在地图右下角显示地图的缩略图 右下
      this.map.addControl(new AMap.OverView({ isOpen: false }));//默认不打开

      //实现默认图层与卫星图、实施交通图层之间切换的控 右上
      //map.addControl(new AMap.MapType());

      //用来获取和展示用户主机所在的经纬度位置 左下
      this.map.addControl(new AMap.Geolocation());
    });
  }

  markerClick(e) {
    // alert(e.target.getPosition()); 获取点的经纬度
    this.infoWindow.setContent(e.target.content);
    this.infoWindow.open(this.map, e.target.getPosition());
    this.clearMarker(e);
  }

  //获取单击的点的经纬度
  clearMarker(e) {

    //获取到单击的点坐标
    var lat = e.target.getPosition();
    //把坐标存入全局变量
    this.getlnglatPoint = lat;
  }

  geocoder2() {  //POI搜索，关键字查询
    let key_11 = (<HTMLInputElement>document.getElementById("key_11")).value;
    let key_12 = (<HTMLInputElement>document.getElementById("key_12")).value;

    if (key_11 == "" || typeof (key_11) == null || typeof (key_11) == 'undefined') {

        alert("地图还未加载完成，无法获取相应点，请稍后...")
    }

    var lnglatXY = new AMap.LngLat(key_11, key_12);
    //document.getElementById('result').innerHTML = "您输入的是：" + key_1;
    //加载地理编码插件
    this.mapObj.plugin(["AMap.Geocoder"], () => {
        let MGeocoder = new AMap.Geocoder({
            radius: 1000,
            extensions: "all"
        });
        //返回地理编码结果
        AMap.event.addListener(MGeocoder, "complete", this.geocoder_CallBack2);
        //逆地理编码
        MGeocoder.getAddress(lnglatXY);
    });

    this.mapObj.setFitView();
  }

  geocoder_CallBack2(data) { //回调函数
    var resultStr = "";
    var address;
    //返回地址描述
    address = data.regeocode.formattedAddress;
    //返回周边道路信息

    //返回结果拼接输出
    resultStr = "<div style=\"font-size: 12px;padding:0px 0 4px 2px; border-bottom:1px solid #C1FFC1;\">" + "<b>地址</b>：" + address + "</div>";
    document.getElementById("result").innerHTML = resultStr;
    (<HTMLInputElement>document.getElementById("tipinput")).value = address;
  }

  addMarker() {
    //获取经纬度
    //document.getElementById("myPageTop").style.display = "none"; //隐藏
    document.getElementById("myPageTop").style.display = ""; //显示
  }

  AddMarkerBtn() {
    //获取经纬度
    var lnglat = (<HTMLInputElement>document.getElementById("lnglat")).value;
    //获取站点名
    var siteName = (<HTMLInputElement>document.getElementById("siteName")).value;
    //获取站点负责人
    var WorkerName = (<HTMLInputElement>document.getElementById("WorkerName")).value;
    //获取详细地址
    var DeiliteAddress = (<HTMLInputElement>document.getElementById("tipinput")).value;
    //定义经度
    var lng = "";
    //定义纬度
    var lat = "";
    //给经度赋值 从0开始到，结束
    lng = lnglat.substr(0, lnglat.indexOf(","));
    //给纬度赋值   从，后一位开始到数组的总长结束
    lat = lnglat.substr(lnglat.indexOf(",") + 1, lnglat.length - 1);

    if (lnglat == "" || lnglat == null) {
        alert("请单击地图获取坐标或输入相应地址或取坐标后重试！");
    } else {
        if (WorkerName != "" && siteName != "") {
            let external:any = window.external;
            external.addMarker(siteName, WorkerName, lng, lat, DeiliteAddress); //getDebugPath()为c#方法
            document.getElementById("myPageTop").style.display = "none"; //隐藏

        } else {
            alert("请填写相关数据！");
        }
    }
  }

  ColseaddMarkerWindow(){
    document.getElementById("myPageTop").style.display = "none"; //隐藏
  }

  onSearchSimple(addressForm){
    const httpOptions = {
      headers:new HttpHeaders({'Content-Type':'application/json'})
    };
    let url = 'http://localhost:8000/safego/search_simple/';
    this.http.post(url, {'address': addressForm.value.address}, httpOptions).subscribe(response=>{
      this.risk = response['risk'];
      this.answer = response['answer'];
    });
  }

  onSearchDetail(detailForm){
    const httpOptions = {
      headers:new HttpHeaders({'Content-Type':'application/json'})
    };
    let url = 'http://localhost:8000/safego/search_detail/';
    let data = (<HTMLInputElement>document.getElementById("tipinput")).value;
    this.http.post(url, {'lnglat': detailForm.value.lnglat,'detail_address': data}, httpOptions).subscribe(response=>{
      console.log(response);
      this.risk = response['risk'];
      this.answer = response['answer'];
    });
  }
}

