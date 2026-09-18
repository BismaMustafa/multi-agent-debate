# Multi-Agent Debate Arena 🚀

An enterprise-grade, event-driven web application that orchestrates real-time debates between multiple AI agents to write, critique, and optimize code.

### 🎥 Live Demonstration
*(Drag and drop your screen recording .mp4 here)*

### 🏗️ Architecture & Tech Stack
* **The AI Engine (Python, LangChain, Groq API):** Defines strict, specialized personas (Senior Developer vs. QA Expert) that interact autonomously.
* **The Real-Time Bridge (Node.js, Express, Socket.io):** A robust middleware that executes the Python engine and streams the stdout/stderr buffers in real-time to the client.
* **The Arena Interface (React, Vite, Tailwind CSS):** A split-pane IDE-style dashboard with custom parsing logic to dynamically separate agent outputs and render live Markdown/Syntax Highlighting.

### ✨ Core Features
* Real-time WebSocket streaming (no loading spinners, instant text rendering).
* Dynamic Stream Parsing (automatically detects agent signatures and routes them to isolated UI cards).
* Secure OS execution environment configuration (`PYTHONIOENCODING=utf-8`).
