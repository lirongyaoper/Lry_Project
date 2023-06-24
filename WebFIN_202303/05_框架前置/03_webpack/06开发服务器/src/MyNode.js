const express = require('express');
const app = express();
app.get('/', (req, res) => {
    res.send({
        info: '后台的数据',
        status: 200
    })
})

app.listen(3000, () => {
    console.log(3000);
})