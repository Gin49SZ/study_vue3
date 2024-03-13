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





















