# Image Optimizer - Full Stack Project

A comprehensive, full-stack application for intelligent image optimization, featuring a high-performance Flask backend and a premium React frontend.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![React](https://img.shields.io/badge/react-18-61dafb)
![Vite](https://img.shields.io/badge/vite-4.0%2B-646cff)

## 🚀 Project Overview

This monorepo contains two main modules that work together to provide a seamless image optimization experience:

### 1. **[Backend API](./imageoptimizer.app)**
A robust Flask-based REST API powered by **OpenCV**.
- 🐍 Built with Python & Flask
- ⚡ Smart compression logic (keeps 100% quality files intact)
- 🔒 Secure file handling & CORS support

### 2. **[Frontend Web App](./imageoptimizer.web)**
A modern React application built with **Vite**.
- ⚛️ Built with React 18
- 🎨 Beautiful Glassmorphism UI
- 📤 Drag-and-drop & Real-time previews

## 📂 Repository Structure

```
imageoptimizer-fullstack/
├── imageoptimizer.app/   # Python/Flask Backend
└── imageoptimizer.web/   # React/Vite Frontend
```

## ⚡ Quick Start Guide

### Prerequisites
- Python 3.9+
- Node.js 18+

### Step 1: Start the Backend

```bash
cd imageoptimizer.app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 run.py
```
> Server starts at `http://localhost:8080`

### Step 2: Start the Frontend

Open a new terminal:
```bash
cd imageoptimizer.web
npm install
npm run dev
```
> App opens at `http://localhost:5173`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
