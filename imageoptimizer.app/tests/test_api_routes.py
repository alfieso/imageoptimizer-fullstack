import pytest
import io


class TestUploadEndpoint:
    """Test suite for the /api/upload endpoint."""
    
    def test_missing_file_part(self, client, caplog):
        """Test that missing file part returns 400 and logs warning."""
        response = client.post('/api/upload')
        
        assert response.status_code == 400
        assert response.json['error'] == 'No file part'
        assert 'Upload request missing file part' in caplog.text
    
    def test_empty_filename(self, client, caplog):
        """Test that empty filename returns 400 and logs warning."""
        data = {'file': (io.BytesIO(b''), '')}
        response = client.post('/api/upload', data=data)
        
        assert response.status_code == 400
        assert response.json['error'] == 'No selected file'
        assert 'Upload request with empty filename' in caplog.text
    
    def test_invalid_file_type(self, client, caplog):
        """Test that invalid file extension returns 400 and logs warning."""
        data = {'file': (io.BytesIO(b'test'), 'test.txt')}
        response = client.post('/api/upload', data=data)
        
        assert response.status_code == 400
        assert response.json['error'] == 'File type not allowed'
        assert 'File type not allowed: test.txt' in caplog.text
    
    def test_invalid_quality_parameter(self, client, valid_image_bytes, caplog):
        """Test that invalid quality parameter returns 400 and logs warning."""
        data = {
            'file': (io.BytesIO(valid_image_bytes), 'test.png'),
            'quality': '200'
        }
        response = client.post('/api/upload', data=data)
        
        assert response.status_code == 400
        assert response.json['error'] == 'Quality must be between 0 and 100'
        assert 'Invalid quality parameter: 200' in caplog.text
    
    def test_invalid_image_content(self, client, invalid_image_bytes, caplog):
        """Test that invalid image content returns 400 and logs warning."""
        data = {'file': (io.BytesIO(invalid_image_bytes), 'fake.png')}
        response = client.post('/api/upload', data=data)
        
        assert response.status_code == 400
        assert response.json['error'] == 'Invalid image content'
        assert 'Validation error' in caplog.text
    
    def test_successful_upload_default_quality(self, client, valid_image_bytes, caplog):
        """Test successful image upload with default quality."""
        data = {'file': (io.BytesIO(valid_image_bytes), 'test.png')}
        response = client.post('/api/upload', data=data)
        
        assert response.status_code == 200
        assert response.content_type == 'image/jpeg'
        assert len(response.data) > 0
        assert 'Processing image: test.png with quality 50' in caplog.text
    
    def test_successful_upload_custom_quality(self, client, valid_image_bytes, caplog):
        """Test successful image upload with custom quality."""
        data = {
            'file': (io.BytesIO(valid_image_bytes), 'test.png'),
            'quality': '10'
        }
        response = client.post('/api/upload', data=data)
        
        assert response.status_code == 200
        assert response.content_type == 'image/jpeg'
        assert 'Processing image: test.png with quality 10' in caplog.text
    
    def test_quality_affects_file_size(self, client, valid_image_bytes):
        """Test that different quality settings produce different file sizes."""
        # High quality
        data_high = {
            'file': (io.BytesIO(valid_image_bytes), 'test.png'),
            'quality': '90'
        }
        response_high = client.post('/api/upload', data=data_high)
        
        # Low quality
        data_low = {
            'file': (io.BytesIO(valid_image_bytes), 'test.png'),
            'quality': '10'
        }
        response_low = client.post('/api/upload', data=data_low)
        
        # High quality should produce larger file
        assert len(response_high.data) > len(response_low.data)
