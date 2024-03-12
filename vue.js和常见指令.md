# 1.Vue初体验

## 1.1 Vue是什么

Vue 是一个现代 JavaScript 框架，是jQuery的替代

* vue2 经典版本
* vue3 主流版本

## 1.2 Vue安装

下载地址：[安装 - vue.js (vuejs.org)](https://v1-cn.vuejs.org/guide/installation.html)

在项目中导入通过`<script src="">`来导入vue.js

编写前端代码使用的IDE：WebStorm

## 1.3 Vue初体验

一般在显示文本内容的标签中使用

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!-- 1.引入vue.js文件-->
    <script src="C:\Users\X\Desktop\Study\libraryMIS\study_vue3\vue_demo\app01\static\js\vue.js"></script>  
</head>
<body>

    <!-- 2.指定区域，该区域的内容希望由vue.js来接管-->
    <div id="app">
        <h1>欢迎学习Vue.js</h1>
        <div>我叫{{ name }}，微信{{ wechat }}</div>
        <input type="button" value="点我" v-on:click="clickMe">
    </div>  

    <script>
        // 3.创建Vue对象，并关联指定的HTML区域
        var app = new Vue({
            el: '#app',
            data: {
                name:'Gin49SZ',
                wechat:'gin49sz'
            },
            methods: {
                clickMe: function () {
                    // 获取值this.name
                    // 修改值this.name = 'xx'
                    this.name = "Alex";
                    this.wechat = "wupeiqi666";
                }
            }
        });
    </script> 
</body>
</html>
```

# 2.Vue常见指令

## 2.1 插值表达式

一般在显示文本内容的标签中使用

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="..\..\static\js\vue.js"></script>  
</head>
<body>
    <div id="app">
        <div>我叫{{ name }}，我喜欢{{ hobby }}，邮箱{{ dataInfo.email }}</div>
        <ul>
            <li>{{ 'Li Hua' }}</li>
            <li>{{ 'Li Hua' + 'has a football' }}</li>
            <li>{{ base + 1 + 1 }}</li>
            <li>{{ 1===1 ?'Li Hua':'Li Min' }}</li>
        </ul>
        <ul>
            <li>{{ condition?'Li Hua':'Li Min' }}</li>
        </ul>
        <input type="button" value="点我" v-on:click="clickMe">
    </div>  

    <script>
        var app = new Vue({
            el: '#app',
            data: {
                name: 'Cai Xukun',
                hobby: 'Basketball',
                dataInfo: {
                    id: 1,
                    email: "xxx.com"
                },
                condition:false,
                base:1,
            },
            methods: {
                clickMe: function () {
                    this.name = "Alex";
                }
            }
        });
    </script> 
</body>
</html>
```

## 2.2 v-bind指令

一般用于对标签中的属性进行操作

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>v-bind指令</title>
    <script src="..\..\static\js\vue.js"></script>  
    <style>
        .ig{
            border: 2px solid red;
        }
        .danger{
            color:red;
        }
        .info{
            background-color:#a7bb6e54;
        }
    </style>
</head>
<body>
    <div id="app">
        <img alt="" v-bind:src="imageUrl" v-bind:class="cls">
        <h1 v-bind:class="{info:v1, danger:v2}">你好呀</h1>
        <h1 v-bind:class="clsDict">Hello</h1>

        <h2 v-bind:class="[a1, a2]">Welcome to you</h1>
        <h2 v-bind:class="[ 1 === 1 ? a1 : a2 ]">this is a condition</h1><!--条件判断，若为true返回a1否则返回a2-->
        <h2 v-bind:class=" 1 === 1 ? 'info' : 'danger' ">this is another condition</h1><!--与上一个效果相同-->

        <h3 v-bind:style="{ color:clr, fontSize:'19px' }">use v-bind:style</h3>

        <input type="button" value="点我" v-on:click="clickMe"></input>
    </div>  

    <script>
        var app = new Vue({
            el: '#app',
            data: {
                imageUrl:"图片链接",
                cls:"ig",   //对应的class="ig"

                v1:true,
                v2:false,   //对应的class="info"

                clsDict:{
                    info:false,
                    danger:true,
                },          //对应的class="danger"

                a1:"info",
                a2:"danger",    //对应的class="info danger"

                clr:"red",
            },
            methods: {
                clickMe: function () {
                    this.v1 = false;    //修改v1为false, "你好呀"的class中去掉了info
                }
            },
        });
    </script> 
</body>
</html>
```

**v-bind注意事项：**

- 简写的格式：`:属性名=属性值`，例如

  ```vue
  <h1 v-bind:class="v1">xxx</h1>
  <h1 :class="v1">xxx</h1>
  
  <img :src="yy">
  ```

- v-bind属于单向绑定(JS修改 -> HTML修改)

  ```vue
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>插值表达式</title>
      <script src="..\..\static\js\vue.js"></script>  
  </head>
  <body>
      <div id="app">
          <h1>{{txt}}</h1>
          <input type="text" :value="txt">
          <input type="button" value="点击" v-on:click="clickMe">
      </div>  
  
      <script>
          var app = new Vue({
              el: '#app',
              data: {
                  txt: "武沛齐", //单项绑定，在页面修改值，并不会修改相关联的js
              },
              methods: {
                  clickMe: function () {
                      this.txt = "Alex";
                  },
              },
          });
      </script> 
  </body>
  </html>
  ```

## 2.3 v-model指令

一般用于在交互的表中使用，例如input、select、textarea等 [双向绑定]

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>单向绑定</title>
    <script src="..\..\static\js\vue.js"></script>  
</head>
<body>
    <div id="app">
        <div>
            用户名：<input type="text" v-model="user">
        </div>
        <div>
            密码：<input type="password" v-model="pwd">
        </div>
        <input type="button" value="登录" v-on:click="clickMe">
        <input type="button" value="重置" v-on:click="resetForm">
    </div>  

    <script>
        var app = new Vue({
            el: '#app',
            data: {
                user: "",
                pwd: "",
            },
            methods: {
                clickMe: function () {
                    console.log(this.user, this.pwd);
                },
                resetForm: function () {
                    this.user = "";
                    this.pwd = "";
                },
            },
        });
    </script> 
</body>
</html>
```

更多细节

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>v-model</title>
    <script src="../../static/js/vue.js"></script>
</head>
<body>
<div id="app">
    <div>
        用户名：<input type="text" v-model="info.user">
    </div>
    <div>
        用户名：<input type="password" v-model="info.pwd">
    </div>
    <div>
        性别：
        <input type="radio" v-model="info.gender" value="1">男
        <input type="radio" v-model="gender" value="2">女
    </div>
    <div>
        爱好：
        <input type="checkbox" v-model="hobby" value="1">篮球
        <input type="checkbox" v-model="hobby" value="2">足球
        <input type="checkbox" v-model="hobby" value="3">板球
    </div>
    <div>
        城市：
        <select v-model="city">
            <option value="sh">上海</option>
            <option value="bj">北京</option>
            <option value="sd">山东</option>
        </select>
    </div>
    <div>
        擅长领域：
        <select v-model="company" multiple>
            <option value="js">技术</option>
            <option value="xs">销售</option>
            <option value="yy">运营</option>
        </select>
    </div>
    <div>
        其他：<textarea v-model="more"></textarea>
    </div>
    <input type="button" value="注册" v-on:click="Clickme">
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            info:{
                user: "",
                pwd: "",
                gender: "1",
            },
            hobby: ["1"],
            city: "",
            company:["js"],
            more: "...",
        },
        methods: {
            Clickme: function () {
                console.log(this.info, this.hobby, this.city, this.company, this.more)
            }
        }
    });
</script>
</body>
</html>
```

## 2.4 v-for指令

用户数据进行循环并展示

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>v-model</title>
    <script src="../../static/js/vue.js"></script>
</head>
<body>
<div id="app">
    <!--示例1-->
    <ul>
        <li v-for="item in dataList">{{item}}</li>
    </ul>
    <!--示例2-->
    <ul>
        <li v-for="(idx, item) in dataList">{{idx}}-{{item}}</li>
    </ul>
    <!--示例3-->
    <ul>
        <li v-for="(key, value) in dataDict">{{key}}-{{value}}</li>
    </ul>
    <!--示例4-->
    <ul>
        <li v-for="(idx, item) in cityList">{{item.id}}-{{item.city}}</li>
    </ul>
    <!--示例5-->
    <ul>
        <li v-for="(idx, item) in cityList">
            <span style="color: aqua" v-for="(k, v) in item">{{k}} {{v}}</span>
        </li>
    </ul>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            dataList: ['a', 'b', 'c'],
            dataDict: {
                id: 1,
                age: 18,
                name: "xx",
            },
            cityList: [
                {id:11, city:"上海"},
                {id:12, city:"北京"},
                {id:13, city:"深圳"},
            ],
        }
    });
</script>
</body>
</html>
```

## 2.5 v-on指令

事件相关的指令，例如：

```
v-on:click
v-on:dblclick
v-on:mouseover
v-on:mouseout
v-on:change
v-on:focus
```

简写格式：`@:事件="函数"`

```vue
<li v-on:dblclick="doSomething('双击')">双击</li>

<li @:dblclick="doSomething('双击')">双击</li>
```

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>v-on指令</title>
    <script src="../../static/js/vue.js"></script>
</head>
<body>
<div id="app">
    <ul>
        <li @:dblclick="doSomething('双击')">双击</li>
        <li v-on:mouseover="doSomething('进入')" v-on:mouseout="doSomething('退出')">进入&退出</li>
    </ul>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
        },
        methods:{
            doSomething: function (msg) {
                console.log(msg);
            }
        }
    });
</script>
</body>
</html>
```





