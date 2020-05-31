var app=new Vue({
    el:'#app-1',
    delimiters: ['{[', ']}'],
    data:{
        message:'hello vue!'
    }
})

var app2 = new Vue({
  el: '#app-2',
  data: {
    message: '页面加载于 ' + new Date().toLocaleString()
  }
})

var app4 = new Vue({
  el: '#app-4',
  delimiters: ['{[', ']}'],
  data: {
    todos: [
      { text: '学习 JavaScript' },
      { text: '学习 Vue' },
      { text: '整个牛项目' }
    ]
  }
})

var app5 = new Vue({
    el:'#app-5',
    delimiters: ['{[', ']}'],
    data:{
        message:"hello vue!"
    },
    // 计算属性computed是基于它们的响应式依赖进行缓存的,只在相关响应式依赖发生改变时它们才会重新求值。
    // 这就意味着只要 message 还没有发生改变，多次访问 reversedMessage 计算属性会立即返回之前的计算结果，
    // 而不必再次执行函数。
    // computed:{
    //     reverseMessage:function () {
    //         this.message=this.message.split('').reverse().join('')
    //     }

    // 相比之下，每当触发重新渲染时，调用方法methods将总会再次执行函数。
    methods:{
        reverseMessage:function () {
            this.message=this.message.split('').reverse().join('')
        }
    }
})

var app6 = new Vue({
    el: '#app-6',
    delimiters: ['{[', ']}'],
    data: {
    message: 'Hello Vue!'
  }
})

Vue.component('todo-item', {
    // todo-item 组件现在接受一个
    // "prop"，类似于一个自定义 attribute。
    // 这个 prop 名为 todo。
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>'
})

var app7 = new Vue({
  el: '#app-7',
  data: {
    groceryList: [
      { id: 0, text: '蔬菜' },
      { id: 1, text: '奶酪' },
      { id: 2, text: '随便其它什么人吃的东西' }
    ]
  }
})
