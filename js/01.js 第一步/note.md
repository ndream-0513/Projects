### `JavaScript`的引用

- 内部`JS`

  一般都是放在`</body>`前面，因为`html`中的代码是从上到下执行的，而执行`js`代码需要在`html`和`css`执行完之后，不然就有可能会报错，所以很多都是把`js`代码放到最后面。

  内部`JS`如果想要把`JS`代码放在`html`的`<body>`前，可以加一个事件监听器，它监听浏览器的 "`DOMContentLoaded`" 事件，即 HTML 文档体加载、解释完毕事件。

  ```javascript
  document.addEventListener("DOMContentLoaded", function() {
    . . .(javascript代码)
  });
  ```

- 外部`JS`

  使用`<script src="js文件位置"> </script>`来调用`js`文件，一般也是放在`</body>`前面，可以用上面内部`JS`的方法将这条引用语句放在任意位置

  也可以使用了`JavaScript` 的一项现代技术（`async` “异步”属性）来解决这一问题，它告知浏览器在遇到 `<script>` 元素时不要中断后续 HTML 内容的加载

  ```javascript
  <script src="js文件位置" async> </script>
  ```

  - 如果脚本无需等待页面解析，且无依赖独立运行，那么应使用 `async`。
  - 如果脚本需要等待页面解析，且依赖于其它脚本，调用这些脚本时应使用 `defer`，将关联的脚本按所需顺序置于 HTML 中。

  详解：[什么是 JavaScript？ - 学习 Web 开发 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/First_steps/What_is_JavaScript#脚本调用策略)

- 内联`JS`

  在`html`标签中绑定函数，`mdn`里面说不推荐使用，但是`vue`中不是很多在标签上绑定的用法吗。。



### 浏览器的`console`中可以运行`javascript`代码



### `javascript`的`for`循环

```javascript
const fruits = ['apples', 'bananas', 'cherries'];
for (const fruit of fruits) {
  console.log(fruit);
}
```



### 用到的对象及对象的一些属性和方法

- 引用`input`标签的对象，有`foucus()`方法（特有的），值的属性为`value`，还有`disabled`属性`true`为禁止输入，`false`为可以输入
- 引用`p`标签的对象，值的属性为`textContent`
- 所有的引用标签的对象都有`style`属性，可以使用`javascript`来动态的设置`css`样式



### 常见错误

- ```“TypeError：guessSubmit.addeventListener is not a function”```：`addeventListener`应该要写为`addEventListener`，`e`要大写
- ```“TypeError：lowOrHi is null”```：选择器没有找到引用



### 变量

`let`、`var`：`var`可以重新定义相同的变量名，`let`不可以，这是`let`的一个优点

变量类型包括：`number`、`string`、`boolean`、`array`、`object`（`array`声明使用`[ ]`，`object`声明使用`{ key : value, }`）

`JS`是一种”动态类型语言“，他根据当前值的内容来决定变量是什么类型，不需要给它指定类型，只需要使用`let`或`var`声明



### 字符串

字符串后面可以直接加数字，`javascript`会看做是两个字符串进行相加

每一个数字都有`toString()`方法，用来转化为字符串

字符串转数字可以用`Number(stringName)`来实现

`javascript`中可使用`typeof(varName)`来判断当前变量的类型

常用方法：

- `string.length`属性：返回字符串长度
- `string.indexOf(para)`：在字符串中查找子字符串，没有则返回-1
- `string.slice(begin, end)`：字符串切片
- `string.toLowerCase()`、`string.toUpperCase()`：大小写转换
- `string.replace(old, new)`：替换字符串的某部分

### 数组

常用方法：

- `string.split(',')`：将字符串转换为数组，每一项以`,`分隔
- `array.join(',')`：将数组转换为字符串，每一项以`,`连接
- `array.toString()`：将数组转换为字符串，只能以`,`连接
- `array.push('element1', 'element2', ……)`：在数组末尾加入一个或多个元素
- `array.pop()`：删除数组中的最后一个元素
- `unshift()`和`shift()`从功能上与`push()`和`pop()`完全相同，只是它们分别作用于数组的开始，而不是结尾。