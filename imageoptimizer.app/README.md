# Image Optimizer API

A Flask-based REST API for detailed image optimization using OpenCV.

## Features
- Smart JPEG compression
- Automatic format detection
- Quality control (0-100%)
- Prevents file size bloat at high quality settings
- CORS enabled for frontend integration

## Installation

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

Start the development server (runs on port 8080):
```bash
python3 run.py
```

## API Endpoints

### POST `/api/upload`
Accepts `multipart/form-data` with:
- `file`: The image file (JPEG, PNG, GIF, etc.)
- `quality`: (Optional) Integer 0-100, defaults to 50

Returns the optimized image file.
