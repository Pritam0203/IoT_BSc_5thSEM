const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

io.on('connection', (socket) => {
    console.log('User connected');

    socket.on('join', (room) => {
        socket.join(room);
        console.log(`User joined room ${room}`);
    });

    socket.on('leave', (room) => {
        socket.leave(room);
        console.log(`User left room ${room}`);
    });

    socket.on('message', ({ room, msg }) => {
        io.to(room).emit('message', msg);
    });

    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});

app.use(express.static(__dirname));  // Serve static files
server.listen(3000, () => {
    console.log('Server is listening on port 3000');
});
