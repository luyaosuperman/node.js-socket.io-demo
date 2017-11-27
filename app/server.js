var app  = require('express')();
var http = require('http').Server(app)
var io   = require('socket.io')(http)

app.get('/health',function(req,res){res.send('Hello World')} )

io.on('connection',function(socket){
  console.log('a user connected');
  socket.on('disconnected',function(){
    console.log('user disconnected')
  })
})

http.listen(8080)
