import pytest
import io
import numpy as np
import cv2
from app import create_app


@pytest.fixture
def app():
    """Create and configure a test Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    yield app


@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()


@pytest.fixture
def valid_image_bytes():
    """Generate a valid test image as bytes."""
    # Create a simple 100x100 RGB image
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    image[:, :] = [255, 0, 0]  # Blue image
    
    # Encode to PNG
    success, encoded = cv2.imencode('.png', image)
    assert success, "Failed to create test image"
    
    return encoded.tobytes()


@pytest.fixture
def invalid_image_bytes():
    """Generate invalid image bytes (plain text)."""
    return b"This is not an image file"
