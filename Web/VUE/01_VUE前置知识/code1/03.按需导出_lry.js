// export let s1 = 'aaa'
// export let s2 = 'ccc'
// export function say() {}

// export default {
//   a: 20
// }

// 按需导出

export let lry_a = 'aaa'
export let lry_b = 'bbb'
export function lry_say (){
  console.log('我说啥了')
}

export default {
  lry_sex : 'male'
}



// ********************************z注意******************************
// ① 每个模块中可以使用多次按需导出
// ② 按需导入的成员名称必须和按需导出的名称保持一致
// ③ 按需导入时，可以使用 as 关键字进行重命名
// ④ 按需导入可以和默认导入一起使用