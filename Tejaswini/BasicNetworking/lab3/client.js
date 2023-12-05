const net = require('net');
const readline = require('readline');

const HOST = 'localhost'; // or the IP of the machine hosting the server
const PORT = 3000;

const client = net.createConnection({ port: PORT, host: HOST }, () => {
    console.log('Connected to server');
});

// Display messages from server
client.on('data', (data) => {
    console.log('Server:', data.toString());
});

// Input handling
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (input) => {
    client.write(input); // Send input to server
});

client.on('end', () => {
    console.log('Disconnected from server');
    rl.close();
});
