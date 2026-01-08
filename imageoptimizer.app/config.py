import os

class Config:
    DEBUG = True
    PORT = 8080
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    COMPRESSION_QUALITY = 50
    
    # Static folder is usually relative to the app folder (app/static)
    # We can determine the absolute path dynamically
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    STATIC_FOLDER = os.path.join(BASE_DIR, 'app', 'static')
    UPLOAD_FOLDER = os.path.join(STATIC_FOLDER, 'uploads')
