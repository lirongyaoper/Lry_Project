    // maxlength 是一个表单属性, 作用是给表单设置一个最大长度

    // 模拟数据
    let dataArr = [
        { uname: '司马懿', imgSrc: './images/9.5/01.jpg' },
        { uname: '女娲', imgSrc: './images/9.5/02.jpg' },
        { uname: '百里守约', imgSrc: './images/9.5/03.jpg' },
        { uname: '亚瑟', imgSrc: './images/9.5/04.jpg' },
        { uname: '虞姬', imgSrc: './images/9.5/05.jpg' },
        { uname: '张良', imgSrc: './images/9.5/06.jpg' },
        { uname: '安其拉', imgSrc: './images/9.5/07.jpg' },
        { uname: '李白', imgSrc: './images/9.5/08.jpg' },
        { uname: '阿珂', imgSrc: './images/9.5/09.jpg' },
        { uname: '墨子', imgSrc: './images/9.5/10.jpg' },
        { uname: '鲁班', imgSrc: './images/9.5/11.jpg' },
        { uname: '嬴政', imgSrc: './images/9.5/12.jpg' },
        { uname: '孙膑', imgSrc: './images/9.5/13.jpg' },
        { uname: '周瑜', imgSrc: './images/9.5/14.jpg' },
        { uname: '老夫子', imgSrc: './images/9.5/15.jpg' },
        { uname: '狄仁杰', imgSrc: './images/9.5/16.jpg' },
        { uname: '扁鹊', imgSrc: './images/9.5/17.jpg' },
        { uname: '马可波罗', imgSrc: './images/9.5/18.jpg' },
        { uname: '露娜', imgSrc: './images/9.5/19.jpg' },
        { uname: '孙悟空', imgSrc: './images/9.5/20.jpg' },
        { uname: '黄忠', imgSrc: './images/9.5/21.jpg' },
        { uname: '百里玄策', imgSrc: './images/9.5/22.jpg' },
      ]
      // 需求1：检测用户输入字数
      //   1. 注册input事件
      //   2. 将文本的内容的长度赋值给对应的数值
      //   3. 表单的maxlength属性可以直接限制在200个数之间
      let textarea = document.querySelector('textarea')
      let useCount = document.querySelector('.useCount')
      // 发布按钮
      let send = document.querySelector('#send')
      // ul
      let ul = document.querySelector('#list')
      textarea.addEventListener('input', function () {
        // console.log(this.value.length)
        useCount.innerHTML = this.value.length
      })
  
      // 需求2： 输入不能为空
      //   点击button之后判断
      //   判断如果内容为空，则提示不能输入为空, 并且直接return 不能为空
      //   防止输入无意义空格, 使用字符串.trim()去掉首尾空格
      // console.log('  str')
      // console.log('  str '.trim())
      //   并将表单的value值设置为空字符串
      //   同时下面红色为设置为0
      send.addEventListener('click', function () {
        if (textarea.value.trim() === '') {
          //   并将表单的value值设置为空字符串
          textarea.value = ''
          //   同时下面红色为设置为0
          useCount.innerHTML = 0
          return alert('内容不能为空')
        }
        // 随机数
        function getRandom(min, max) {
          return Math.floor(Math.random() * (max - min + 1)) + min
        }
        let random = getRandom(0, dataArr.length - 1)
        // 需求3：   新增留言  写到send 的里面
        // 创建一个小li，然后里面通过innerHTML追加数据
        let li = document.createElement('li')
        // 随机获取数据数组里面的内容, 替换newNode的图片和名字以及留言内容
        li.innerHTML = `
         <div class="info">
        <img class="userpic" src=${dataArr[random].imgSrc}>
        <span class="username">${dataArr[random].uname}</span>
        <p class="send-time"> ${new Date().toLocaleString()} </p>
        </div>
        <div class="content">${textarea.value}</div>
        <span class="the_del">X</span>
        `
              // 需求4：删除留言  放到追加的前面
        // 在事件处理函数里面获取点击按钮, 注册点击事件
        //   (易错点: 必须在事件里面获取, 外面获取不到)
        // 删除对应的元素(通过this获取对应的那条需要删除的元素)
        // 教你一招: 放到追加进ul的前面，这样创建元素的同时顺便绑定了事件，赞~~
        // 使用 li.querySelector()
        let del = li.querySelector('.the_del')
        del.addEventListener('click', function () {
          // 删除操作  点击的是X  删除的小li  父元素.removeChild(子元素)
          ul.removeChild(li)
        })
  

        // 利用时间对象将时间动态化       new Date().toLocaleString()
        // 追加给 ul  用  父元素.insertBefore(子元素, 那个元素的前面)
        ul.insertBefore(li, ul.children[0])
        // 需求5：重置
        // 将表单域内容重置为空
        // 将userCount里面的内容重置为0
        textarea.value = ''
        //   同时下面红色为设置为0
        useCount.innerHTML = 0
      })

