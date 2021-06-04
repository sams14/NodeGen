const express = require('express');

var port = 3000
var app = express()

const schedular = require('node-schedule');
const job = schedular.scheduleJob('8 20 * * *', function(){
    const { spawn } = require('child_process');
    const childP = spawn('python', ['demo.py']);
    childP.stdout.on('data', (data)=>{
        console.log(`stdout: ${data}`);
    });
    childP.stderr.on('data', (data)=>{
        console.log(`stderr: ${data}`);
    });
});

app.get('/', (req, res)=>{
    res.send("Hello World!");
});

app.listen(port, ()=>{
    console.log("server is listening at port = ", port);
});