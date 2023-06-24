let n1 = 10
let n2 = 20
function show() {
  console.log('lirongyaoper')
}

export default {
  n1,
  show
}
//默认导出语法  export default {}


// 每个模块中，只允许使用唯一的一次 export default，否则会报错！

// export default {
//   n2
// }