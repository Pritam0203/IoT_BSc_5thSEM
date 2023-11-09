// echoServer.js
const net = require('net');

const PORT = 8080;

const server = net.createServer((socket) => {
    console.log('Client connected!');

    // When data is received from a client, echo it back
    socket.on('data', (data) => {
        socket.write(data);
    });

    socket.on('end', () => {
        console.log('Client disconnected.');
    });
});

server.listen(PORT, () => {
    console.log(`Echo server started on port ${PORT}`);
});
