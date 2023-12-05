const net = require('net');
const readline = require('readline');

const PORT = 3000;

const server = net.createServer((socket) => {
    console.log('Client connected');

    // Display messages from client
    socket.on('data', (data) => {
        console.log('Client:', data.toString());
    });

    // Input handling
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.on('line', (input) => {
        socket.write(input); // Send input to client
    });

    socket.on('end', () => {
        console.log('Client disconnected');
        rl.close();
    });
});

server.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});
