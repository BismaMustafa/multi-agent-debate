const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const { spawn } = require('child_process');
const cors = require('cors');

const app = express();
app.use(cors());

const server = http.createServer(app);
const io = new Server(server, {
    cors: { origin: "*" } // React frontend ko connect hone ki ijazat
});

io.on('connection', (socket) => {
    console.log('🟢 Frontend Connected to Node Bridge');

    // Jab frontend se naya debate problem aaye
    socket.on('start_debate', (problemStatement) => {
        console.log(`Received task: ${problemStatement}`);
        
        // Python script ko background mein run karein
        // PYTHONIOENCODING: "utf-8" add kiya gaya hai taake emojis crash na karein
        const pythonProcess = spawn('python', ['../ai-engine/main.py', problemStatement], {
            env: { ...process.env, PYTHONUNBUFFERED: "1", PYTHONIOENCODING: "utf-8" }
        });

        // Jaise hi Python se text aaye, usey React (frontend) ko bhej dein
        pythonProcess.stdout.on('data', (data) => {
            const text = data.toString();
            socket.emit('debate_stream', text);
        });

        pythonProcess.stderr.on('data', (data) => {
            console.error(`Error: ${data}`);
            socket.emit('debate_stream', `\n[System Error]: ${data.toString()}`);
        });

        pythonProcess.on('close', (code) => {
            socket.emit('debate_end', '\n✅ Debate Concluded.');
            console.log('Debate finished.');
        });
    });

    socket.on('disconnect', () => {
        console.log('🔴 Frontend Disconnected');
    });
});

const PORT = 5000;
server.listen(PORT, () => {
    console.log(`🚀 Node.js Bridge Server running on http://localhost:${PORT}`);
});