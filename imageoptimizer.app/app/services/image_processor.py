import cv2
import numpy as np
import logging

logger = logging.getLogger(__name__)

def process_image(file_storage, quality=50):
    """
    Reads an image file, compresses it as JPEG, and returns the bytes.
    
    :param file_storage: Werkzeug FileStorage object
    :param quality: JPEG compression quality (0-100)
    :return: Bytes of the processed image
    """
    # Store original filename for format detection
    original_filename = file_storage.filename.lower() if file_storage.filename else ''
    is_jpeg = original_filename.endswith(('.jpg', '.jpeg'))
    
    # Read file content into memory
    file_bytes = np.frombuffer(file_storage.read(), np.uint8)
    original_size = len(file_bytes)
    
    # If quality is 100% and already a JPEG, return original to avoid bloat
    if quality == 100 and is_jpeg:
        logger.info(f"Quality 100% on JPEG file - returning original ({original_size} bytes)")
        return file_bytes.tobytes()
    
    # Validate image content
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    if image is None:
        logger.warning("imdecode failed to decode bytes")
        raise ValueError("Invalid image content")
    
    # Set JPEG encoding parameters
    # IMWRITE_JPEG_OPTIMIZE: optimize Huffman coding (reduces size without quality loss)
    # IMWRITE_JPEG_PROGRESSIVE: create progressive JPEG (better compression)
    encode_params = [
        int(cv2.IMWRITE_JPEG_QUALITY), int(quality),
        int(cv2.IMWRITE_JPEG_OPTIMIZE), 1,
        int(cv2.IMWRITE_JPEG_PROGRESSIVE), 1
    ]
    
    # Compress image to memory buffer
    success, encoded_image = cv2.imencode('.jpg', image, encode_params)
    
    if not success:
        logger.error("cv2.imencode returned False")
        raise ValueError("Could not encode image")
    
    processed_bytes = encoded_image.tobytes()
    processed_size = len(processed_bytes)
    
    # If processed size is larger than original at high quality (95%+), return original
    if quality >= 95 and is_jpeg and processed_size > original_size:
        logger.info(f"Processed JPEG larger than original ({processed_size} > {original_size}) - returning original")
        return file_bytes.tobytes()
        
    return processed_bytes
