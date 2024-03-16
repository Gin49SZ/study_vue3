# 1.Vue初体验

## 1.1 Vue是什么

Vue 是一个现代 JavaScript 框架，是jQuery的替代

* vue2 经典版本
* vue3 主流版本

## 1.2 Vue安装

下载地址：https://unpkg.com/vue@2/dist/vue.js

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
    <script src="..\..\static\js\vue.js"></script>  
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

## 案例：数据管理

- 数据列表

  ```vue
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>插值表达式</title>
      <script src="../../static/js/vue.js"></script>
  </head>
  <body>
      <div id="app">
          <h3>数据列表</h3>
          <table>
              <thead>
                  <tr>
                      <td>姓名</td>
                      <td>年龄</td>
                  </tr>
              </thead>
              <tbody>
                  <tr v-for="item in dataList">
                      <td>{{ item.name }}</td>
                      <td>{{ item.age }}</td>
                  </tr>
                
              </tbody>
          </table>
      </div>  
  
      <script>
          var app = new Vue({
              el: '#app',
              data: {
                  dataList: [
                      {name: 'Li Ming', age: 19},
                      {name:'Zhang Hua', age:22}
                  ],
              },
          });
      </script> 
  </body>
  </html>
  ```

- 数据添加

  ```vue
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>插值表达式</title>
      <script src="../../static/js/vue.js"></script>
  </head>
  <body>
      <div id="app">
          <h3>表单区域</h3>
          <div>
              <label>姓名</label>
              <input type="text" v-model="name">
          </div>
          <div>
              <label>年龄</label>
              <input type="text" v-model="age">
          	<input type="submit" value="提交" @click="addUser">
          </div>
  
          <h3>数据列表</h3>
          <table>
              <thead>
                  <tr>
                      <td>姓名</td>
                      <td>年龄</td>
                  </tr>
              </thead>
              <tbody>
                  <tr v-for="item in dataList">
                      <td>{{ item.name }}</td>
                      <td>{{ item.age }}</td>
                  </tr>
                
              </tbody>
          </table>
      </div>  
  
      <script>
          var app = new Vue({
              el: '#app',
              data: {
                  name: "",
                  age: "",
                  dataList: [
                      {name: 'Li Ming', age: 19},
                      {name:'Zhang Hua', age:22}
                  ],
              },
              methods: {
                  addUser: function () {
                      // 创建行数据
                      let row = {
                          name: this.name,
                          age: this.age
                      };
                      // 添加到数据表格 -> 添加到dataList
                      this.dataList.push(row);
  
                      // 数据置空
                      this.name = "";
                      this.age = "";
                  }
              }
          });
      </script> 
  </body>
  </html>
  ```

- 删除功能

  > splice(indx, delete_num, add_element)
  >
  > 第一个参数：执行的索引
  >
  > 第二个参数：从该索引开始要删除的元素个数，即返回的元素列表包含的元素个数
  >
  > 第三个参数：要添加的元素
  >
  > ```javascript
  > dataList = ['a', 'b', 'c'];
  > del_el = splice(2, 1);
  > console.log(del_el)
  > 
  > >>>['c']
  > ```

  ```vue
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>插值表达式</title>
      <script src="../../static/js/vue.js"></script>
  </head>
  <body>
      <div id="app">
          <h3>表单区域</h3>
          <div>
              <label>姓名</label>
              <input type="text" v-model="name">
          </div>
          <div>
              <label>年龄</label>
              <input type="text" v-model="age">
          	<input type="submit" value="提交" @click="addUser">
          </div>
  
          <h3>数据列表</h3>
          <table>
              <thead>
                  <tr>
                      <td>姓名</td>
                      <td>年龄</td>
                  </tr>
              </thead>
              <tbody>
                  <tr v-for="(idx, item) in dataList">
                      <td>{{ item.name }}</td>
                      <td>{{ item.age }}</td>
                      <td><input type="button" value="删除" @click="deleteRow(idx)"></td>
                  </tr>
                
              </tbody>
          </table>
      </div>  
  
      <script>
          var app = new Vue({
              el: '#app',
              data: {
                  name: "",
                  age: "",
                  dataList: [
                      {name: 'Li Ming', age: 19},
                      {name:'Zhang Hua', age:22}
                  ],
              },
              methods: {
                  addUser: function () {
                      // 创建行数据
                      let row = {
                          name: this.name,
                          age: this.age
                      };
                      // 添加到数据表格 -> 添加到dataList
                      this.dataList.push(row);
  
                      // 数据置空
                      this.name = "";
                      this.age = "";
                  },
                  deleteRow: function (idx) {
                      //根据索引删除dataList的值
                      this.dataList.splice(idx, 1);
                  }
              }
          });
      </script> 
  </body>
  </html>
  ```

  当执行某一个事件，例如`@click="func(v1, v2, ...)"`，可以将所需要的参数都通过函数传递过去；

  另外，还有一种传递参数的方法，即通过默认的`event`参数，在标签中定义`data-参数名`后，即可在event参数中找到对应的值

  ```vue
  ...
  <td><input type="button" value="删除" @click="deleteRow()" :data-idx="idx"></td>
  
  ...
  <script>
      ...
      deleteRow: function () {
          //通过默认的event参数来删除
          let idx = event.target.dataset.idx;
          this.dataList.splice(idx, 1)
      }
  </script>
  ```

- 编辑功能

  > 解包
  >
  > 在es6（JavaScript版本）中，支持解包功能，和python一样
  >
  > ```javascript
  > let {id, name} = {id: 1, name: 'Li Ming'}
  > console.log(id, name)
  > 
  > >>> 1 Li Ming
  > ```

  ```vue
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>插值表达式</title>
      <script src="../../static/js/vue.js"></script>
  </head>
  <body>
      <div id="app">
          <h3>表单区域</h3>
          <div>
              <label>姓名</label>
              <input type="text" v-model="name">
          </div>
          <div>
              <label>年龄</label>
              <input type="text" v-model="age">
              <input type="submit" :value="title" @click="modifyUser">
          </div>
  
          <h3>数据列表</h3>
          <table>
              <thead>
                  <tr>
                      <td>姓名</td>
                      <td>年龄</td>
                  </tr>
              </thead>
              <tbody>
                  <tr v-for="(idx, item) in dataList">
                      <td>{{ item.name }}</td>
                      <td>{{ item.age }}</td>
                      <td><input type="button" value="删除" @click="deleteRow(idx)" :data-idx="idx"></td>
                      <td><input type="button" value="编辑" @click="editRow" :data-idx="idx"></td>
                  </tr>
                
              </tbody>
          </table>
      </div>  
  
      <script>
          var app = new Vue({
              el: '#app',
              data: {
                  name: "",
                  age: "",
                  title: "新建",
                  editIndex: undefined,
                  dataList: [
                      {name: 'Li Ming', age: 19},
                      {name:'Zhang Hua', age:22}
                  ],
              },
              methods: {
                  modifyUser: function () {
                      console.log(this.editIndex)
                      if(this.editIndex){
                          //编辑
                          this.dataList[this.editIndex].name = this.name;
                          this.dataList[this.editIndex].age = this.age;    
                          
                          //清空editIndex
                          this.editIndex = undefined;                     
                      }else{
                          //新增
                          // 创建行数据
                          let row = {
                              name: this.name,
                              age: this.age
                          };
                          // 添加到数据表格 -> 添加到dataList
                          this.dataList.push(row);
                      }
                      // 数据置空
                      this.name = "";
                      this.age = "";          
                      
                      //默认为新建
                      this.title = "新建"; 
  
                  },
                  deleteRow: function (idx) {
                      //根据索引删除dataList的值
                      this.dataList.splice(idx, 1);
  
                      //查看event参数中的idx
                      console.log(event.target.dataset.idx)
                  },
                  editRow: function () {
                      let idx = event.target.dataset.idx;
  
                      // 通过解包来获取变量
                      let {name, age} = this.dataList[idx];
                      
                      // 将值赋给输入框
                      this.name = name;
                      this.age = age;
  
                      //修改按钮value
                      this.title = "编辑";
  
                      //修改editIndex的值以执行编辑
                      this.editIndex = idx;
  
                  }
              }
          });
      </script> 
  </body>
  </html>
  ```

## 2.6 v-if指令

条件判断，条件成立则显示，不成立则不显示

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>v-if指令</title>
    <script src="..\..\static\js\vue.js"></script>  
</head>
<body>
    <div id="app">
        <a v-if="isLogin">您好，{{ user }}</a>
        <a v-else href="">登录</a>
    </div>  

    <script>
        var app = new Vue({
            el: '#app',
            data: {
                isLogin: false,
                user: "Li Minng",
            },
        });
    </script> 
</body>
</html>
```

if后面不一定必须有else，并且if和else可以连用

```vue
<a v-if="isA"></a>

<a v-else-if="isB"></a>

<a v-else-if="isC"></a>

<a v-else></a>
```

## 2.7 v-show指令

根据条件显示或者隐藏（但是标签都会渲染要页面，v-if是有和无，v-show是显示和隐藏`display=none`）

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>v-show指令</title>
    <script src="..\..\static\js\vue.js"></script>  
</head>
<body>
    <div id="app">
        <a v-show="v1">CXK</a>
        <a v-show="!v1">BASKETBALL</a>
        <hr>
        <input type="button" value="切换" @click="Switch">
    </div>  

    <script>
        var app = new Vue({
            el: '#app',
            data: {
                v1:true,
            },
            methods: {
                Switch: function () {
                    if(this.v1){
                        this.v1 = false;
                    }else{
                        this.v1 = true;
                    }
                }
            }
        });
    </script> 
</body>
</html>
```

简单的操作可以直接在`@click=""`中添加表达式而不使用函数

```vue
<input type="button" value="切换" @click="v1 ? v1=false : v1=true">
```

v-show的使用例子：短信验证码登录和用户名密码登录之间的切换

## 案例：用户登录（axios）

axios是一个HTTP库，可以发送HTTP请求

```vue
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

也可以下载下来后在本地进行导入

```vue
<script src="../../static/js/axios.min.js"></script>
```

在后期学习了脚手架，也可以通过npm安装来使用

一个使用例子：

```vue
<script src="../../static/js/axios.min.js"></script>
<script>
	axios({
        method: "post",
        url: "https://...",
        params: {
            v1: 123,
            v2: 456
        },
        data: {
            name: "ABC",
            pwd: "123"
        },
        headers: {
            "Content-Type": "application/json"
        }
    }).then(function (res) {
        console.log(res.data);
    }).catch(function (error) {
        console.log(error);
    })
</script>
```

案例：用户登录

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>案例：用户登录</title>
    <script src="../../static/js/vue.js"></script>
    <script src="../../static/js/axios.min.js"></script>
</head>
<body>
<div id="app">
    <input type="button" value="切换登录方式" @click="isSms ? isSms=false : isSms=true">
    <hr>
    <div v-show="isSms">
        <p>
            <label for="">手机号</label>
            <input type="text" placeholder="手机号" v-model="sms.mobile">
        </p>
        <p>
            <label for="">验证码</label>
            <input type="password" placeholder="验证码" v-model="sms.code">
        </p>
    </div>
    <div v-show="!isSms">
        <p>
            <label for="">用户名</label>
            <input type="text" placeholder="用户名" v-model="info.username">
        </p>
        <p>
            <label for="">密&emsp;码</label>
            <input type="password" placeholder="密码" v-model="info.password">
        </p>
    </div>
    <hr>
    <input type="button" value="登 录" @click="login">
</div>  

<script>
    var app = new Vue({
        el: '#app',
        data: {
            isSms: true,
            info: {
                username: "",
                password: "",
            },
            sms: {
                mobile: "",
                code: "",
            }
        },
        methods: {
            login: function () {
                // 1.获取用户输入的值
                let dataDict = this.isSms ? this.sms : this.info;

                // 2.向某个地址发送网络请求（基于axios）
                let url;
                if(this.isSms){
                    url = "https://api.luffycity.com/api/v1/auth/password/login/?loginWay=mobile"
                }else{
                    url = "https://api.luffycity.com/api/v1/auth/password/login/?loginWay=password"
                }
                axios({
                    method: "post",
                    url: url,
                    data: dataDict,
                    headers: {
                        "Content-Type": "application/json"
                    }
                }).then(function (res) {
                    console.log("res", res.data);
                    if(res.data.code === -1){
                        alert(res.data.msg);
                        return;
                    }
                    // 网络成功后跳转首页
                    window.location.href = "https://api.luffycity.com"
                }).catch(function (error) {
                    console.log("error", error);
                    alert("请求异常，请重新尝试")
                })
            }
        }
    });
</script> 
</body>
</html>
```

# 3.组件化开发

在开发过程中，我们可以将页面中的某一部分功能编写成一个组件，然后再页面上进行引用。

- 有利于划分功能模块的开发（HTML、CSS、JavaScript等相关代码都集成到组件中）
- 有利于重用

## 3.1 局部组件

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>局部组件</title>
    <script src="../../static/js/vue.js"></script>
    <script src="../../static/js/axios.min.js"></script>
</head>
<body>
<div id="app">
    <h1>======当前页面======</h1>
    <div>{{name}}</div>
    <hr>
    <h1>======引入子组件======</h1>
    <!--不影响其他Vue中的内容的使用-->
    <Demo></Demo>
    <!--组件也可以反复使用-->
    <Bb></Bb>
    <Bb></Bb>

</div>  

<script>
    // 创建子组件
    const Demo = {
        // 组件中的data是一个方法，并返回值（与Vue的对象不同）
        data: function () {
            return {
                msg:'hhhh'
            }
        },
        template: `
          <div>
            <h1>{{msg}}</h1>
            <input type="text" v-model="msg">
            <input type="button" @click="showMsg" value="点击这里展开msg">
          </div>
        `,
        methods: {
            showMsg: function () {
                alert(this.msg);
            }
        }
    }

    const Bili = {
        data: function () {
            return {
                dataList: [
                    {name: 'Li Ming', age: 19},
                    {name:'Zhang Hua', age:22}
                ],
            }
        },
        template: `
          <h3>数据列表</h3>
          <table>
            <thead>
            <tr>
              <td>姓名</td>
              <td>年龄</td>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(idx, item) in dataList">
              <td>{{ item.name }}</td>
              <td>{{ item.age }}</td>
            </tr>

            </tbody>
          </table>
        `
    }
    // 应用组件
    var app = new Vue({
        el: '#app',
        data: {
            name: 'Zhang Hua',
        },

        // 1.将组件挂载到vue对象中
        components: {
            // 挂在子组件
            Demo,
            Bb: Bili
        },
        methods: {}

    });
</script> 
</body>
</html>
```

## 3.2 全局组件

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>全局组件</title>
    <script src="../../static/js/vue.js"></script>
    <script src="../../static/js/axios.min.js"></script>
</head>
<body>
<div id="app">
    <h1>======当前页面======</h1>
    <div>{{name}}</div>
    <hr>
    <h1>======引入子组件======</h1>
    <!--不影响其他Vue中的内容的使用-->
    <Demo></Demo>
    <!--组件也可以反复使用-->
    <Bili></Bili>
    <Bili></Bili>

</div>  

<script>
    // 创建子组件
    Vue.component('Demo', {
            data: function () {
                return {
                    msg:'hhhh'
                }
            },
            template: `
              <div>
                <h1>{{msg}}</h1>
                <input type="text" v-model="msg">
                <input type="button" @click="showMsg" value="点击这里展开msg">
              </div>
            `,
            methods: {
                showMsg: function () {
                    alert(this.msg);
                }
            }
    });

    Vue.component('Bili', {
        data: function () {
            return {
                dataList: [
                    {name: 'Li Ming', age: 19},
                    {name:'Zhang Hua', age:22}
                ],
            }
        },
        template: `
          <h3>数据列表</h3>
          <table>
            <thead>
            <tr>
              <td>姓名</td>
              <td>年龄</td>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(idx, item) in dataList">
              <td>{{ item.name }}</td>
              <td>{{ item.age }}</td>
            </tr>

            </tbody>
          </table>
        `
    });

    // 应用组件
    var app = new Vue({
        el: '#app',
        data: {
            name: 'Zhang Hua',
        },

        // 无需挂载
        methods: {}

    });
</script> 
</body>
</html>
```

> 问题：为何vue中组件的`data`必须是一个函数？
>
> vue中组件的`data`必须是相互隔离的，必须只在使用这个组件的时候才会创建，因此必须使用data函数返回对象作为组件的状态
>
> 当某一处复用的地方组件内`data`数据被改变时，其他复用地方组件的`data`数据不受影响



# 4.vue-router组件

vue-router：统筹组件的第三方工具

通过vue + vue-router的使用，可以实现单页面应用（SPA），即全部的项目只包含一个页面

## 4.1 下载和引用

官方网站：[Vue Router (vuejs.org)](https://v3.router.vuejs.org/zh/)

下载地址：https://unpkg.com/vue-router@3/dist/vue-router.js

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>vue-router</title>
    <script src="../../static/js/vue.js"></script>
    
    <!--vue-router依赖于vue.js-->
    <script src="../../static/js/vue-router.js"></script>
</head>
<body>

</body>
</html>
```

后期学习脚手架，也可以通过npm下载和引用

## 4.2 快速上手

完成一个菜单，通过点击不同的按钮来加载不同的组件

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>vue-router应用</title>
    <style>
        body{
            margin: 0;
        }
        .container{
            width: 980px;
            margin: 0 auto;
        }
        .menu{
            height: 48px;
            background-color: #499ef3;
            line-height: 48px;
        }
        .menu a{
            color:white;
            text-decoration: none;
            padding: 0 10px;
        }
    </style>
    <script src="../../static/js/vue.js"></script>
    <script src="../../static/js/vue-router.js"></script>
</head>
<body>
<div id="app">
    <div class="menu">
        <div class="container">
            <router-link to="/">Logo</router-link>
            <router-link to="/home">首页</router-link>
            <router-link to="/course">课程</router-link>
            <router-link to="/news">资讯</router-link>
        </div>
    </div>
    <div class="container">
        <router-view></router-view>
    </div>
</div>

<script>

    const Home = {template: '<div>首页内容...</div>'};
    const Course = {template: '<div>课程内容...</div>'};
    const News = {template: '<div>资讯内容...</div>'};

    const router = new VueRouter({
        routes: [
            {path: '/', component: Home},
            {path: '/home', component: Home},
            {path: '/course', component: Course},
            {path: '/news', component: News}
        ],
    });

    var app = new Vue({
        el: '#app',
        data: {},
        methods: {},
        // 将router添加到vue中
        router: router,
    });
</script>
</body>
</html>
```

## 案例：router+axios

使用vue-router和axios实现多个案例发送不同的HTTP请求

> 1. 组件中的data、created、mounted执行顺序
>
>    data（初始定义） -> created（DOM树创建之前） -> mounted（DOM树创建之后）
>
> 2. then(res=>{})中的`res=>{}`不可以替换成`function(res){}`
>
>    原因：使用中`res=>{}`的`this.`表示的是它的上一级中的this，即Vue中的对象，而`function(res){}`中的`this.`表示Window中的对象
>
>    **举个例子：**
>
>    ```js
>    function x1(){
>        console.log(this);    //this -> Window
>    }
>    x1();	//等价于 window.x1
>    --------------------------------------------------------------
>    
>    x2 = {
>        name:'Li Ming',
>        f: function(){
>            console.log(this);//this -> Object
>    	}
>    }
>    x2.f();	//等价于 x2
>    --------------------------------------------------------------
>    
>    x3 = {
>        name:'Li Ming',
>        f:function(){
>            console.log(this);//this -> Object
>            function inner() {
>                console.log(this);
>            }
>            inner();
>        }
>    }
>    x3.f();	//当执行到inner时候，没有声明是由什么触发，默认使用Window，即此时的第二个this -> Window
>    ---------------------------------------------------------------
>        
>    x3 = {
>        name:'Li Ming',
>        f:function(){
>            console.log(this);//this -> Object
>            inner = () => {
>                console.log(this);//箭头函数中的this默认是上一级的this
>            }
>            inner();
>        }
>    }
>    x3.f();	//当执行到inner时候，使用的是上一级的this，即此时的第二个this -> Object  
>    ```
>
>    **关于这一点的原因**
>
>    > - 箭头函数根本没有自己的 this，导致箭头函数体内部的 this 就是外层函数体的 this，即从作用域链的上一层继承 this。
>    >   若普通函数是一个对象的方法，则它的 this 指针指向这个对象
>    > - ES6 之前，JavaScript 的 this 对象一直很令人头大，回调函数，经常看到 var self = this 这样的代码，为了将外部 this 传递到回调函数中，那么有了箭头函数，就不需要这样做了，直接使用 this 就行。
>    >   ————————————————
>    >
>    > 版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
>    >
>    > 原文链接：https://blog.csdn.net/Run_Bomb/article/details/115001897
>
> 3. Vue中`{{}}`与Django中模板语法中`{{}}`冲突的问题
>
>    > 解决方式：https://blog.csdn.net/RKun595/article/details/87179711#22_11

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>router+axios</title>
    <style>
        body{
            margin: 0;
        }
        .container{
            width: 980px;
            margin: 0 auto;
        }
        .menu{
            height: 48px;
            background-color: #499ef3;
            line-height: 48px;
        }
        .menu a{
            color:white;
            text-decoration: none;
            padding: 0 10px;
        }
    </style>
    <script src="../tatic/js/vue.js"></script>
    <script src="../static/js/vue-router.js"></script>
    <script src="../static/js/axios.min.js"></script>
</head>
<body>
{% verbatim myblock %}
<div id="app">
    <div class="menu">
        <div class="container">
            <router-link to="/main">Main</router-link>
            <router-link to="/data1">Data</router-link>
        </div>
    </div>
    <div class="container">
        <router-view></router-view>
    </div>
</div>
{% endverbatim myblock %}

<script>
    const Home= {template: '<div>首页内容...</div>'};

    const Data1= {
        data: function () {
            // 定义页面需要数据，使用函数返回对象，可以保证创建的对象只能在组件中使用
            return {
                dataList: [],
            }
        },
        created: function (){
            // 组件创建完毕后自动出发，发送HTTP请求
            // created在页面渲染之前执行，所哟不可以对DOM树进行操作
            axios({
                method:"get",
                url:'/data1/',
                headers: {
                    'Content-type': 'application/json'
                }
            }).then((res) => {
                this.dataList = res.data.data;
                for(item in this.dataList){
                    console.log(item)
                }
            })
        },
        mounted: function () {
            // mounted在页面渲染结束之后执行，可以对DOM树进行操作
        },
        template: `
          {% verbatim myblock %}
          <div>
            <div v-for="item in dataList">
              <a>{{item.name}}</a>
              <a>{{item.age}}</a>
            </div>
          </div>
          {% endverbatim myblock %}
        `
    };

    const router = new VueRouter({
        routes: [
            {path: '/main', component: Home},
            {path: '/data1', component: Data1},
        ],
    });

    var app = new Vue({
        el: '#app',
        data: {},
        methods: {},
        // 将router添加到vue中
        router: router,
    });
</script>
</body>
</html>
```

## 4.3 路由和传值

当某个组件可以根据某些参数值的不同，展示不同的效果时，需要用到动态路由。

如何设置动态路由？

- 定义路由

  ```javascript
  const router = new VueRouter({
      routers: [
          {path:'/', component: Home},
          {path:'/course', component: Course, name: 'Course'},
          {path:'/detail/:id', component:Detail, name:'Detail'}
      ],
  })
  ```

- HTML展示

  ```html
  <div>
      <router-link to="/">首页</router-link><!-- to= 后面只可以接path-->
      <router-link to="/course">课程</router-link>
      <router-link to="/detail/123">课程</router-link>
      
      <router-link :to="{path:'/course'}">课程</router-link>
      <router-link :to="{path:'/course?size=19&page=2'}">课程</router-link>
      <router-link :to="{path:'/course', query:{size:19, page:2}}">课程</router-link><!--自动拼接-->
      
      <router-link :to="{name: 'Course'}">课程</router-link>
      <router-link :to="{name: 'Course', query:{size:19, page:2}}">课程</router-link>
      <!--如果值是动态的例如vue中的data也可以-->
      <router-link :to="{name: 'Course', query:{size:data, page:2}}">课程</router-link>
      
      <router-link :to="{path:'/detail/22', query:{size:1}}">课程A</router-link>
      <router-link :to="{name:'Detail', params:{id:3}, query:{size:1}}">课程B</router-link>
      
      
  </div>
  ```
  
- 组件获取URL传值和GET参数

  ```javascript
  const Detail = {
      data: function () {
          return {
              title: '详细页面',
              paramDict: null,
              queryDict: null
          }
      },
      created: function () {
          this.paramDict = this.$route.params;
          this.queryDict = this.$route.query;
      },
      tenplate: `
      <div>
          <h2>{{title}}</h2>
          <div>当前请求的数据{{paramDict}} {{queryDict}}</div>
      </div>
      `
  }
  ```

## 案例：router+axios(2)

注意：当使用`<router-link :to="{name:'Detail', params:{id:3}, query:{size:1}}">课程B</router-link>`类型的路由，需要保证在`const router = new VueRouter`中对应的path有name属性

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>router+axios</title>
    <style>
        body{
            margin: 0;
        }
        .container{
            width: 980px;
            margin: 0 auto;
        }
        .menu{
            height: 48px;
            background-color: #499ef3;
            line-height: 48px;
        }
        .menu a{
            color:white;
            text-decoration: none;
            padding: 0 10px;
        }
    </style>
    <script src="../static/js/vue.js"></script>
    <script src="../static/js/vue-router.js"></script>
    <script src="../static/js/axios.min.js"></script>
</head>
<body>
{% verbatim myblock %}
<div id="app">
    <div class="menu">
        <div class="container">
            <router-link to="/main">Main</router-link>
            <router-link to="/data1">Data</router-link>
        </div>
    </div>
    <div class="container">
        <router-view></router-view>
    </div>
</div>
{% endverbatim myblock %}

<script>
    const Home= {template: '<div>首页内容...</div>'};

    const Data1 = {
        data: function () {
            return {
                dataList: [],
                size: 2,
            }
        },
        created: function (){
            // 组件创建完毕后自动触发，发送HTTP请求
            axios({
                method:"get",
                url:'/data1/',
                headers: {
                    'Content-type': 'application/json'
                }
            }).then((res) => {
                this.dataList = res.data.data;
            })
        },
        template: `
          {% verbatim myblock %}
          <div>
            <div v-for="item in dataList">
              <router-link :to="{name: 'Detail', params:{id:item.id}, query:{page:2, size:size}}">点击查看用户详情</router-link>
                <a>{{item.id}}</a>
                <a>{{item.name}}</a>
                <a>{{item.age}}</a>
            </div>
          </div>
          {% endverbatim myblock %}
        `
    };

    const Detail = {
        data: function () {
            return {
                title: "详细页面",
                userid: null,
            }
        },
        created: function () {
            this.userid = this.$route.params.id;
            // 此处可以根据用户id发送ajax请求
            let queryDict = this.$route.query;
            console.log(queryDict);

        },
        template: `
          {% verbatim myblock %}
          <div>
            <h2>用户详情</h2>
            <div>当前用户ID为{{userid}}</div>
          </div>
          {% endverbatim myblock %}
        `
    }

    const router = new VueRouter({
        routes: [
            {path: '/main', component: Home},
            {path: '/data1', component: Data1},
            {path:'/detail/:id', component: Detail, name: 'Detail'}<!--没有name会报错无法找到Detail-->
        ],
    });

    var app = new Vue({
        el: '#app',
        data: {},
        methods: {},
        // 将router添加到vue中
        router: router,
    });
</script>
</body>
</html>
```

## 4.4 页面不刷新BUG

当在组件中的template定义了调用自己的路径，用户点击后会发生页面不刷新的BUG

```javascript
    const Detail = {
        data: function () {
            return {
                title: "详细页面",
                userid: null,
                dataList: []
            }
        },
        created: function () {
            this.userid = this.$route.params.id;
            // 此处可以根据用户id发送ajax请求
            axios({
                method:"get",
                url:'/data1/',
                headers: {
                    'Content-type': 'application/json'
                }
            }).then((res) => {
                this.dataList = res.data.data;
            })

        },
        template: `
          {% verbatim myblock %}
          <div>
            <h2>用户详情</h2>
            <div>当前用户ID为{{userid}}</div>
            
            <!--无法执行以下内容，因为组件在调用自己，不会刷新created的内容-->
            
            <h2>其他用户</h2>
            <div v-for="item in dataList">
              <router-link :to="{name: 'Detail', params:{id:item.id}}">
                点击查看用户{{item.name}}的详情
              </router-link>
            </div>

          </div>
          {% endverbatim myblock %}
        `
    }
```

**如何解决呢？**

在Detail组件中设置watch属性，watch会监测`$route`值，一旦发生变化，就立即执行相应的函数

```javascript
const Detail = {
    ...
    watch: {
        $route: function (to, from) { //to表示路由变化后的地址，from表示变化前
            this.userid = to.params.id;
            // 如果有ajax请求，此处也要发送，可以通过在methods中写ajax请求，然后直接调用即可
            getUserDetail();

        }
    },
    method: {
        getUserDetail: function () {
            //根据this.userid来执行ajax请求
        }
    }
}
```

## 案例：router+axios(3)

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>router+axios</title>
    <style>
        body{
            margin: 0;
        }
        .container{
            width: 980px;
            margin: 0 auto;
        }
        .menu{
            height: 48px;
            background-color: #499ef3;
            line-height: 48px;
        }
        .menu a{
            color:white;
            text-decoration: none;
            padding: 0 10px;
        }
    </style>
    <script src="../static/js/vue.js"></script>
    <script src="../static/js/vue-router.js"></script>
    <script src="../static/js/axios.min.js"></script>
</head>
<body>
{% verbatim myblock %}
<div id="app">
    <div class="menu">
        <div class="container">
            <router-link to="/main">Main</router-link>
            <router-link to="/data1">Data</router-link>
        </div>
    </div>
    <div class="container">
        <router-view></router-view>
    </div>
</div>
{% endverbatim myblock %}

<script>
    const Home= {template: '<div>首页内容...</div>'};

    const Data1 = {
        data: function () {
            return {
                dataList: [],
                size: 2,
            }
        },
        created: function (){
            // 组件创建完毕后自动触发，发送HTTP请求
            axios({
                method:"get",
                url:'/data1/',
                headers: {
                    'Content-type': 'application/json'
                }
            }).then((res) => {
                this.dataList = res.data.data;
            })
        },
        template: `
          {% verbatim myblock %}
          <div>
            <div v-for="item in dataList">
              <router-link :to="{name: 'Detail', params:{id:item.id}, query:{page:2, size:size}}">点击查看用户详情</router-link>
                <a>{{item.id}}</a>
                <a>{{item.name}}</a>
                <a>{{item.age}}</a>
            </div>
          </div>
          {% endverbatim myblock %}
        `
    };

    const Detail = {
        data: function () {
            return {
                title: "详细页面",
                userid: null,
                dataList: []
            }
        },
        created: function () {
            this.userid = this.$route.params.id;
            // 此处可以根据用户id发送ajax请求
            axios({
                method:"get",
                url:'/data1/',
                headers: {
                    'Content-type': 'application/json'
                }
            }).then((res) => {
                this.dataList = res.data.data;
            })
        },
        watch: {
            $route: function (to, from) {
                this.userid = to.params.id;
            }
        },
        template: `
          {% verbatim myblock %}
          <div>
            <h2>用户详情</h2>
            <div>当前用户ID为{{userid}}</div>
            <h2>其他用户</h2>
            <hr>
            <div v-for="item in dataList">
              <router-link :to="{name: 'Detail', params:{id:item.id}}">
                点击查看用户{{item.name}}的详情
              </router-link>
            </div>

          </div>
          {% endverbatim myblock %}
        `
    }

    const router = new VueRouter({
        routes: [
            {path: '/main', component: Home},
            {path: '/data1', component: Data1},
            {path:'/detail/:id', component: Detail, name: 'Detail'}
        ],
    });

    var app = new Vue({
        el: '#app',
        data: {},
        methods: {},
        // 将router添加到vue中
        router: router,
    });
</script>
</body>
</html>
```

## 4.6 路由嵌套

一个组件包含多个组件的实现方法：路由嵌套

```javascript
const router = new VueRouter({
    routers: [
        {
            path: '/pins/',
            component: Pins,
            childern: [
                {
                    // 当 /pins/hot 匹配成功，
                    // Hot组件会被渲染在Pins的<router-view>中
                    path: 'hot',
                    component: Hot
                },
                {
                    // 当 /pins/following 匹配成功，
                    // Following组件会被渲染在Pins的 <router-view> 中
                    path: 'following',
                    component: Following
                }
            ]
        }
    ]
})
```

## 案例：router+axios(4)

通过路由嵌套实现在一个组件下通过不同的标签展示不同的子组件

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>router+axios</title>
    <style>
        body{
            margin: 0;
        }
        .container{
            width: 980px;
            margin: 0 auto;
        }
        .menu{
            height: 48px;
            background-color: #499ef3;
            line-height: 48px;
        }
        .menu a{
            color:white;
            text-decoration: none;
            padding: 0 10px;
        }
    </style>
    <script src="../static/js/vue.js"></script>
    <script src="../static/js/vue-router.js"></script>
    <script src="../static/js/axios.min.js"></script>
</head>
<body>
{% verbatim myblock %}
<div id="app">
    <div class="menu">
        <div class="container">
            <router-link to="/main">Main</router-link>
            <router-link to="/data1">Data</router-link>
            <router-link to="/pins/">Pins</router-link>
        </div>
    </div>
    <div class="container">
        <router-view></router-view>
    </div>
</div>
{% endverbatim myblock %}

<script>
    const Home= {template: '<div>首页内容...</div>'};

    const Data1 = {
        data: function () {
            return {
                dataList: [],
                size: 2,
            }
        },
        created: function (){
            // 组件创建完毕后自动触发，发送HTTP请求
            axios({
                method:"get",
                url:'/data1/',
                headers: {
                    'Content-type': 'application/json'
                }
            }).then((res) => {
                this.dataList = res.data.data;
            })
        },
        template: `
          {% verbatim myblock %}
          <div>
            <div v-for="item in dataList">
              <router-link :to="{name: 'Detail', params:{id:item.id}, query:{page:2, size:size}}">点击查看用户详情</router-link>
                <a>{{item.id}}</a>
                <a>{{item.name}}</a>
                <a>{{item.age}}</a>
            </div>
          </div>
          {% endverbatim myblock %}
        `
    };

    const Detail = {
        data: function () {
            return {
                title: "详细页面",
                userid: null,
                dataList: []
            }
        },
        created: function () {
            this.userid = this.$route.params.id;
            // 此处可以根据用户id发送ajax请求
            axios({
                method:"get",
                url:'/data1/',
                headers: {
                    'Content-type': 'application/json'
                }
            }).then((res) => {
                this.dataList = res.data.data;
            })
        },
        watch: {
            $route: function (to, from) {
                this.userid = to.params.id;
            }
        },
        template: `
          {% verbatim myblock %}
          <div>
            <h2>用户详情</h2>
            <div>当前用户ID为{{userid}}</div>

            <hr>
            <h2>其他用户</h2>
            <div v-for="item in dataList">
              <router-link :to="{name: 'Detail', params:{id:item.id}}">
                点击查看用户{{item.name}}的详情
              </router-link>
            </div>

          </div>
          {% endverbatim myblock %}
        `
    };

    const Pins = {
        data: function () {
            return {}
        },
        template: `
          {% verbatim myblock %}
          <div>
            <h2>Pins专区</h2>
            <router-link :to="{name: 'Hot'}">Hot</router-link>
            <router-link :to="{name: 'Following'}">Following</router-link>
            <hr>
            <router-view></router-view>
          </div>
          {% endverbatim myblock %}
        `
    };

    const Hot = {
        template: `
          {% verbatim myblock %}
          <div>
            <h2>Hot界面</h2>
          </div>
          {% endverbatim myblock %}
        `
    };
    const Following = {
        template: `
          {% verbatim myblock %}
          <div>
            <h2>Following界面</h2>
          </div>
          {% endverbatim myblock %}
        `
    };

    const router = new VueRouter({
        routes: [
            {path: '/main', component: Home},
            {path: '/data1', component: Data1},
            {path:'/detail/:id', component: Detail, name: 'Detail'},
            {
                path: '/pins/',
                component: Pins,
                children: [
                    {
                        // 当 /pins/hot 匹配成功，
                        // Hot组件会被渲染在Pins的<router-view>中
                        path: 'hot',
                        component: Hot,
                        name: 'Hot',
                    },
                    {
                        // 当 /pins/following 匹配成功，
                        // Following组件会被渲染在Pins的 <router-view> 中
                        path: 'following',
                        component: Following,
                        name: 'Following',
                    }
                ]
            }
        ],
    });

    var app = new Vue({
        el: '#app',
        data: {},
        methods: {},
        // 将router添加到vue中
        router: router,
    });
</script>
</body>
</html>
```

另外，通过`redirect: {name: 'Module'}`或者`redirect: '/path'`也可以在router中重定向

```javascript
children:[
    {
    	path:"",
    	redirect:{name:'Hot'} // 默认情况下，加载Hot组件，即进来之后就会显示/pins/hot页面
	}
]
```

## 4.7 编程式导航

除了使用`<router-link>`，也可以借助router的实例方法，通过编写代码来实现。

想要导航到不同的URL，则使用`router.push`方法。**这个方法会向history栈添加一个新的记录**，所以，当用户点击浏览器后退按钮时，则回到之前的URL。

- router.push

  ```javascript
  // 字符串 将home的URL添加到栈里，同时跳转过去
  router.push("home")
  
  // 对象
  router.push({path: "home"})
  
  // 命名的路由
  router.push({name:'user', params: {userId:'123'}}) // "/user/:userId" -> /user/123
  
  // 带查询参数，变成/register?plan=private
  router.push({path:'register', query:{plan:'private'}})
  ```

- router.replace 把当前的地址替换（无法再通过后退按钮返回到之前的地址）

  ```javascript
  //和push一样的使用方法，只是不会添加到history栈
  ```

- router.go 这个方法的参数是一个整数，表示在history记录中向前或者向后退多少

  ```javascript
  router.go(1) //在浏览器中前进一步，等同于history.forward()
  
  router.go(-1) //后退一步，等同于history.back()
  
  router.go(3) //前进或者后退多步同理
  ```

## 案例：登录跳转

```javascript
const Login = {
    data: function () {
        return {
            user: '',
            pwd: ''
        }
    },
    methods: {
        doLogin: function () {
            this.$router.push({name:'Home'});
        }
    },
    template:`
      <div>
        <p>
          <label for="">用户名</label>
          <input type="text" placeholder="用户名" v-model="user">
        </p>
        <p>
          <label for="">密&emsp;码</label>
          <input type="password" placeholder="密码" v-model="pwd">
        </p>
        <hr>
        <input type="button" value="登 录" @click="doLogin">
      </div>
    `
}
```

## 4.8 导航守卫（navigation guard）

在基于vue-router实现访问跳转时，都会执行一个钩子

```javascript
const router = new VueRouter({...});
router.beforeEach((to, from, next) => {
    // to:Router: 即将要进入的目标 路由对象
    // from: Router: 当前导航正要离开的路由
    // next() 继续向后执行
    // next(false) 中断导航，保持当前所在的页面
    // next('/')	next({path:'/'})	next(name:'Login')	跳转到指定页面，由此可以实现未登录跳转已登录 
})
```

## 案例：路由拦截

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>router+axios</title>
    <style>
    </style>
    <script src="../static/js/vue.js"></script>
    <script src="../static/js/vue-router.js"></script>
    <script src="../static/js/axios.min.js"></script>
</head>
<body>
{% verbatim myblock %}
<div id="app">
    <div class="menu">
        <div class="container">
            <router-link to="/main">Main</router-link>
            <router-link to="/data1">Data</router-link>
            <router-link to="/pins/">Pins</router-link>
            <router-link style="float:right" to="/login">Login</router-link>
        </div>
    </div>
    <div class="container">
        <router-view></router-view>
    </div>
</div>
{% endverbatim myblock %}

<script>
	...

    const Login = {
        data: function () {
            return {
                user: '',
                pwd: ''
            }
        },
        methods: {
            doLogin: function () {
                // 添加到session
                sessionStorage.setItem("isLogin", true);
                this.$router.push({name:'Home'});
            }
        },
        template:`
          <div>
            <p>
              <label for="">用户名</label>
              <input type="text" placeholder="用户名" v-model="user">
            </p>
            <p>
              <label for="">密&emsp;码</label>
              <input type="password" placeholder="密码" v-model="pwd">
            </p>
            <hr>
            <input type="button" value="登 录" @click="doLogin">
          </div>
        `
    }

    const router = new VueRouter({
        routes: [
            ...
            {path: '/login', component: Login, name:'Login'}
        ],
    });

    // 拦截器
    router.beforeEach((to, from, next) => {
        // 如果已经登录，则可以继续访问目标地址
        if(sessionStorage.getItem('isLogin')){
            next();
            return;
        }
        // 未登录，访问登陆页面
        if(to.name === 'Login'){
            next();
            return;
        }
        // 未登录，跳转登陆页面
        next({name: 'Login'});
    })

    var app = new Vue({
        el: '#app',
        data: {},
        methods: {},
        // 将router添加到vue中
        router: router,
    });
</script>
</body>
</html
```

 如果在routes中为某个path添加`beforeEnter`，则可以实现对某一个路径进行拦截守卫

```javascript
const router = new VueRouter({
    routes: [
        {
            path: '/home',
            component: Home,
            name: 'Home',
            children: [...],
            beforeEnter: (to, from, next) => {
            	...
        	}
        }
    ]
})
```





















