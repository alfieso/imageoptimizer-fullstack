from flask import request, jsonify, current_app, send_file
from . import api
from app.services.image_processor import process_image
import io

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@api.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        current_app.logger.warning("Upload request missing file part")
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        current_app.logger.warning("Upload request with empty filename")
        return jsonify({'error': 'No selected file'}), 400
        
    if not allowed_file(file.filename):
        current_app.logger.warning(f"File type not allowed: {file.filename}")
        return jsonify({'error': 'File type not allowed'}), 400
        
    quality = request.form.get('quality', type=int)
    if quality is None:
        quality = current_app.config['COMPRESSION_QUALITY']
    elif not (0 <= quality <= 100):
        current_app.logger.warning(f"Invalid quality parameter: {quality} for file {file.filename}")
        return jsonify({'error': 'Quality must be between 0 and 100'}), 400
        
    try:
        current_app.logger.info(f"Processing image: {file.filename} with quality {quality}")
        image_bytes = process_image(file, quality)
        
        return send_file(
            io.BytesIO(image_bytes),
            mimetype='image/jpeg',
            as_attachment=False,
            download_name='processed.jpg'
        )
    except ValueError as e:
        current_app.logger.warning(f"Validation error for file {file.filename}: {str(e)}")
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Internal error processing file {file.filename}: {str(e)}", exc_info=True)
        return jsonify({'error': f"Internal error: {str(e)}"}), 500
