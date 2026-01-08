# Image Optimizer Project

A full-stack application for intelligent image optimization, featuring a Flask backend and a modern React frontend.

## Project Structure

- **[imageoptimizer.app](./imageoptimizer.app)** - Flask REST API with OpenCV image processing
- **[imageoptimizer.web](./imageoptimizer.web)** - React + Vite frontend with premium UI

## Quick Start

### 1. Start the Backend
```bash
cd imageoptimizer.app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 run.py
```

### 2. Start the Frontend
```bash
cd imageoptimizer.web
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) to view the application.
