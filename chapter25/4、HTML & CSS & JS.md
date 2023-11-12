## 一、HTML

### （一）基本标签

页面构成的标签元素：

[HTML 系列教程 (w3school.com.cn)](https://www.w3school.com.cn/h.asp)

- 标题 (h1,h2...)
- 段落 (p)
- 链接跳转 (a href)
- 图片 (img src)
- 块标签 (div)
- 内联标签 (span...)
- 表格标签 (table)
- 列表标签 (ul、ol)

### （二）表单标签

- form

## 二、CSS

## 三、JavaScript

### （一）注释

```javascript
单行注释：// 注释内容
多行注释：/* 注释内容 */
```

### （二）代码块

```javascript
if (count == 3) { 
   alert(count); 
} 
```

### （三）输出语句

```javascript
window.alert("hello")
console.log("log")
```

### （四）变量

```javascript
// 定义全局变量
var age = 20;
// 局部变量
let i = 0;
```

### （五）数据类型

```javascript
// number 数字类型 let 
let age = 20;
// string 字符、字符串，单双引皆可
let ch = 'a';
// boolean 布尔。true，false
var flag = true;
// null 对象为空
var obj = null;
alert(typeof obj);//结果是 object
// undefined 当声明的变量未初始化时，该变量的默认值是 undefined
var a ;
alert(typeof a); //结果是 undefined
```

### （六）运算符

JavaScript 提供了如下的运算符。大部分和 Java语言 都是一样的

- 一元运算符：++，--
- 算术运算符：+，-，*，/，%
- 赋值运算符：=，+=，-=…
- 关系运算符：>，<，>=，<=，!=，\==，===…
- 逻辑运算符：&&，||，!
- 三元运算符：条件表达式 ? true_value : false_value 

 \==和===区别：

- ==：

  1. 判断类型是否一样，如果不一样，则进行类型转换
  2. 再去比较其值

- ===：js 中的全等于

  1. 判断类型是否一样，如果不一样，直接返回false
  2. 再去比较其值

  ### （七）流程控制

  JavaScript 中提供了和 Java 一样的流程控制语句，如下

  - if 
  - switch
  - for
  - while
  - dowhile

#### 1、if 语句

```js
var count = 3;
if (count == 3) {
    alert(count);
}
```

#### 2、switch 语句

```js
var num = 3;
switch (num) {
    case 1:
        alert("星期一");
        break;
    case 2:
        alert("星期二");
        break;
    case 3:
        alert("星期三");
        break;
    case 4:
        alert("星期四");
        break;
    case 5:
        alert("星期五");
        break;
    case 6:
        alert("星期六");
        break;
    case 7:
        alert("星期日");
        break;
    default:
        alert("输入的星期有误");
        break;
}
```

#### 3、for 循环语句

```js
var sum = 0;
for (let i = 1; i <= 100; i++) { //建议for循环小括号中定义的变量使用let
    sum += i;
}
alert(sum);
```

#### 4、while 循环语句

```js
var sum = 0;
var i = 1;
while (i <= 100) {
    sum += i;
    i++;
}
alert(sum);
```

#### 5、do while 循环语句

```js
var sum = 0;
var i = 1;
do {
    sum += i;
    i++;
}
while (i <= 100);
alert(sum);
```

### （七）函数

函数（就是Java中的方法）是被设计为执行特定任务的代码块；JavaScript 函数通过 function 关键词进行定义。

#### 1、 定义格式

函数定义格式有两种：

- 方式1

  ```js
  function 函数名(参数1,参数2..){
      要执行的代码
  }
  ```

- 方式2

  ```js
  var 函数名 = function (参数列表){
      要执行的代码
  }
  ```

> ==注意：==
>
> - 形式参数不需要类型。因为JavaScript是弱类型语言
>
>   ```js
>   function add(a, b){
>       return a + b;
>   }
>   ```
>
>   上述函数的参数 a 和 b 不需要定义数据类型，因为在每个参数前加上 var 也没有任何意义。
>
> - 返回值也不需要定义类型，可以在函数内部直接使用return返回即可

#### 2、函数调用

函数调用函数：

```js
函数名称(实际参数列表);
```

eg：

```js
let result = add(10,20);
```

> ==注意：==
>
> - JS中，函数调用可以传递任意个数参数
>
> - 例如  `let result = add(1,2,3);` 
>
>   它是将数据 1 传递给了变量a，将数据 2 传递给了变量 b，而数据 3 没有变量接收。

### （八）Array对象

JavaScript Array对象用于定义数组

#### 1、定义格式

数组的定义格式有两种：

- 方式1

  ```js
  var 变量名 = new Array(元素列表); 
  ```

  例如：

  ```js
  var arr = new Array(1,2,3); //1,2,3 是存储在数组中的数据（元素）
  ```

- 方式2

  ```js
  var 变量名 = [元素列表];
  ```

  例如：

  ```js
  var arr = [1,2,3]; //1,2,3 是存储在数组中的数据（元素）
  ```

  ==注意：Java中的数组静态初始化使用的是{}定义，而 JavaScript 中使用的是 [] 定义==

#### 2、元素访问

访问数组中的元素和 Java 语言的一样，格式如下：

```js
arr[索引] = 值;
```

**代码演示：**

```js
 // 方式一
var arr = new Array(1,2,3);
// alert(arr);

// 方式二
var arr2 = [1,2,3];
//alert(arr2);

// 访问
arr2[0] = 10;
alert(arr2)
```

## 四、js对页面的操作

- 改变html内容
- 修改指定标签的属性
- 对表单进行校验

### （一）BOM对象

Browser Object Model 浏览器对象模型。也就是 JavaScript 将浏览器的各个组成部分封装为对象。

 BOM 中包含了如下对象：

- Window：浏览器窗口对象
- Navigator：浏览器对象
- Screen：屏幕对象
- History：历史记录对象
- Location：地址栏对象

![](images/image-20210815194911914.png)

###  （二）DOM对象

DOM：Document Object Model 文档对象模型。也就是 JavaScript 将 HTML 文档的各个组成部分封装为对象。

将HTML内容解析：

- Document：整个文档对象
- Element：元素对象
- Attribute：属性对象
- Text：文本对象

JavaScript 通过 DOM， 就能够对 HTML进行操作了

- 改变 HTML 元素的内容
- 改变 HTML 元素的样式（CSS）
- 对 HTML DOM 事件作出反应
- 添加和删除 HTML 元素

#### 1、标签操作

- 定位标签（id="content"， class="content"）
- 改变标签内容

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="content">
    hello
</div>

<script>
    var c = document.getElementById("content")
    c.innerText = "world"
    console.log(c)
</script>
</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="content1">
    hello
</div>
<div id="content2">
    hello
</div>
<script>
    var divs = document.getElementsByTagName("div")
    // console.log(c, typeof c)
    for(let i=0; i<divs.length; i++) {
        divs[i].innerText="您好";
    }
</script>
</body>
</html>
```

#### 2、事件监听

- 事件绑定

方式一：

```html
<body>
提交：<input type="button" onclick="on()"/>

<script>
    function on() {
        window.alert("提交数据")
    }
</script>
</body>
```

方式二：

```html
<body>
提交2：<input type="button" id="btn"/>

<script>
    document.getElementById("btn").onclick = function () {
        window.alert("提交数据2")
    }
</script>
</body>
```

- 事件类型

| 事件属性名  | 说明                     |
| ----------- | ------------------------ |
| onclick     | 鼠标单击事件             |
| onblur      | 元素失去焦点             |
| onfocus     | 元素获得焦点             |
| onload      | 某个页面或图像被完成加载 |
| onsubmit    | 当表单提交时触发该事件   |
| onmouseover | 鼠标被移到某元素之上     |
| onmouseout  | 鼠标从某元素移开         |

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form id="register" action="#">
    <input type="text" name="username" id="username"/>
    <input type="submit" value="提交"/>
</form>

<script>
    document.getElementById("username").onblur = function () {
        console.log("onblur")
    }

    document.getElementById("username").onfocus = function () {
        console.log("onfocus")
    }

    document.getElementById("register").onsubmit = function () {
        window.alert("提交数据")
    }
</script>
</body>
</html>
```

#### 3、表单验证

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div>
    <h1>欢迎注册</h1>

    <form>
        <table>
            <tr>
                <td>用户名：</td>
                <td>
                    <input type="text" name="username" id="username"/>
                    <span id="username_err" style="color:red;display: none">用户名不符合条件</span>
                </td>
            </tr>
            <tr>
                <td>密码：</td>
                <td><input type="password" name="password" id="password"/></td>
            </tr>
        </table>
        <div>
            <input type="submit" id="reg_btn" value="注册"/>
        </div>
    </form>
</div>

<script>
    var usernameInput = document.getElementById("username")
    usernameInput.onblur = function () {
        let usernameValue = usernameInput.value.trim(); //获取值，去空格
        // 
        if(usernameValue.length >= 6 && usernameValue.length <= 12) {
            // 符合条件

        } else {
           document.getElementById("username_err").style.display="";
        }
    }


</script>
</body>
</html>
```

#### 4、正则表达式

书写方式：/^\w{6,12}$/

[JavaScript 正则表达式 | 菜鸟教程 (runoob.com)](https://www.runoob.com/js/js-regexp.html)

## 五、Bootstrap 

[Bootstrap 入门 · Bootstrap v5 中文文档 v5.3 | Bootstrap 中文网 (bootcss.com)](https://v5.bootcss.com/docs/getting-started/introduction/)





