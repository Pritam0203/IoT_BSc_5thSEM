// echoClient.js
const net = require('net');

const PORT = 8080;
const HOST = '127.0.0.1';

const client = new net.Socket();

client.connect(PORT, HOST, () => {
    console.log('Connected to the server!');
    client.write('Hello, Echo Server!');
});

client.on('data', (data) => {
    console.log('Received:', data.toString());
    // After receiving the echo, disconnect the client
    client.destroy();
});

client.on('close', () => {
    console.log('Connection closed.');
});
