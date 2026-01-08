# Image Optimizer - Flask Backend

A robust, high-performance REST API for image optimization using OpenCV and Flask.

## Features

✨ **Core Features:**
- 🚀 **High Performance**: Uses OpenCV (cv2) for blazing fast processing.
- 📦 **Smart Compression**: Intelligent JPEG optimization with Huffman coding.
- 🧠 **Smart Quality Handling**: 
  - Returns original file if quality is 100% (prevents bloat).
  - Progressive JPEG support for better web performance.
- 🔒 **Security**: Strict file type validation and secure filename handling.
- 🛡️ **CORS Enabled**: Ready for frontend integration.
- ⚡ **In-Memory**: Processes images without disk I/O overhead.

## Tech Stack

- **Framework**: Flask 3.x
- **Image Processing**: OpenCV (headless)
- **Utilities**: NumPy, Python-Dotenv
- **Testing**: Pytest

## Prerequisites

- Python 3.9+
- pip

## Installation

1. Navigate to the app directory:
   ```bash
   cd imageoptimizer.app
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Start the Server

```bash
python3 run.py
```
Server runs on `http://127.0.0.1:8080` by default.

### API Endpoints

#### `POST /api/upload`

Uploads and optimizes an image.

**Request:**
- **Content-Type**: `multipart/form-data`
- **Fields**:
  - `file`: (Required) The image file to process.
  - `quality`: (Optional) Integer 0-100. Default: 50.

**Response:**
- **200 OK**: Binary content of the optimized image.
- **400 Bad Request**: Invalid file or parameters.

**Example (cURL):**
```bash
curl -X POST -F "file=@photo.jpg" -F "quality=80" http://localhost:8080/api/upload > optimized.jpg
```

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `8080` |
| `DEBUG` | Flask debug mode | `True` |
| `ALLOWED_EXTENSIONS` | Supported formats | `jpg, jpeg, png, gif` |

## Project Structure

```
imageoptimizer.app/
├── app/
│   ├── api/            # API blueprints & routes
│   ├── services/       # Image processing logic
│   └── __init__.py     # App factory & CORS setup
├── config.py           # Configuration class
├── run.py              # Entry point
└── requirements.txt    # Dependencies
```

## License

MIT License
