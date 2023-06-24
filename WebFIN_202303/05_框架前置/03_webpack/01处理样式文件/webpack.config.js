//导入path模块
const path = require('path');

//导出
//Node.js出
module.exports = {
    //1.入口
    entry:'./src/index.js',//入口文件，相对路径
    //2.出口
    output:{
        filename:'main.js',//打包成的文件名
        path:path.resolve(__dirname,'dist')
    },
    //3.模式 development：开发环境，production：生产环境，默认值
    mode:'production',
    //4.loader:转换器，转换非js文件
    module:{
        rules:[
            {
                test:/\.css$/,
                use:['style-loader','css-loader']
            },
            {
                test:/\.less$/,
                use:['style-loader','css-loader','less-loader']
            },
        ]
    }
}