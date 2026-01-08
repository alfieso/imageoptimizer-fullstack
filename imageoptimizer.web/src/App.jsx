import { useState, useRef } from 'react'
import './App.css'

// API Configuration from environment variables
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8080'

function App() {
  const [selectedFile, setSelectedFile] = useState(null)
  const [previewUrl, setPreviewUrl] = useState(null)
  const [processedImageUrl, setProcessedImageUrl] = useState(null)
  const [quality, setQuality] = useState(85)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [dragActive, setDragActive] = useState(false)
  const [originalSize, setOriginalSize] = useState(null)
  const [processedSize, setProcessedSize] = useState(null)

  const fileInputRef = useRef(null)

  const handleDrag = (e) => {
    e.preventDefault()
    e.stopPropagation()
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true)
    } else if (e.type === "dragleave") {
      setDragActive(false)
    }
  }

  const handleDrop = (e) => {
    e.preventDefault()
    e.stopPropagation()
    setDragActive(false)

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFileSelect(e.dataTransfer.files[0])
    }
  }

  const handleFileSelect = (file) => {
    if (!file) return

    // Validate file type
    const validTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/bmp']
    if (!validTypes.includes(file.type)) {
      setError('Please select a valid image file (JPEG, PNG, GIF, or BMP)')
      return
    }

    setSelectedFile(file)
    setOriginalSize(file.size)
    setError(null)
    setProcessedImageUrl(null)
    setProcessedSize(null)

    // Create preview
    const reader = new FileReader()
    reader.onloadend = () => {
      setPreviewUrl(reader.result)
    }
    reader.readAsDataURL(file)
  }

  const handleFileInputChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      handleFileSelect(e.target.files[0])
    }
  }

  const handleUpload = async () => {
    if (!selectedFile) {
      setError('Please select a file first')
      return
    }

    setLoading(true)
    setError(null)
    setProcessedImageUrl(null)

    const formData = new FormData()
    formData.append('file', selectedFile)
    formData.append('quality', quality)

    try {
      const response = await fetch(`${API_BASE_URL}/api/upload`, {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.error || 'Upload failed')
      }

      // Get the processed image as a blob
      const blob = await response.blob()
      setProcessedSize(blob.size)

      // Create object URL for the processed image
      const url = URL.createObjectURL(blob)
      setProcessedImageUrl(url)
    } catch (err) {
      setError(err.message || 'Failed to process image')
      console.error('Upload error:', err)
    } finally {
      setLoading(false)
    }
  }

  const handleDownload = () => {
    if (!processedImageUrl) return

    const link = document.createElement('a')
    link.href = processedImageUrl
    link.download = `optimized_${selectedFile.name.replace(/\.[^/.]+$/, '')}.jpg`
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }

  const formatFileSize = (bytes) => {
    if (!bytes) return '0 Bytes'
    const k = 1024
    const sizes = ['Bytes', 'KB', 'MB', 'GB']
    const i = Math.floor(Math.log(bytes) / Math.log(k))
    return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i]
  }

  const getCompressionRatio = () => {
    if (!originalSize || !processedSize) return 0
    return Math.round(((originalSize - processedSize) / originalSize) * 100)
  }

  return (
    <div className="app">
      <header className="header">
        <h1>Image Optimizer</h1>
        <p className="subtitle">Compress and optimize your images with ease</p>
      </header>

      <div className="upload-container">
        <div className="upload-card glass">
          <div
            className={`upload-zone ${dragActive ? 'drag-active' : ''}`}
            onClick={() => fileInputRef.current?.click()}
            onDragEnter={handleDrag}
            onDragLeave={handleDrag}
            onDragOver={handleDrag}
            onDrop={handleDrop}
          >
            <div className="upload-icon">📸</div>
            <div className="upload-text">
              <h3>{selectedFile ? selectedFile.name : 'Choose an image'}</h3>
              <p>Drag and drop or click to browse</p>
              <p style={{ fontSize: '0.85rem', marginTop: '0.5rem' }}>
                Supports JPEG, PNG, GIF, BMP
              </p>
            </div>
            <input
              ref={fileInputRef}
              type="file"
              accept="image/*"
              onChange={handleFileInputChange}
              className="upload-input"
            />
          </div>

          {selectedFile && (
            <div className="quality-control">
              <div className="quality-label">
                <span>Compression Quality</span>
                <span className="quality-value">{quality}%</span>
              </div>
              <input
                type="range"
                min="1"
                max="100"
                value={quality}
                onChange={(e) => setQuality(parseInt(e.target.value))}
                className="quality-slider"
              />
              <button
                onClick={handleUpload}
                disabled={loading || !selectedFile}
                className="upload-button"
              >
                {loading ? 'Processing...' : 'Optimize Image'}
              </button>
            </div>
          )}

          {error && (
            <div className="error-message">
              ⚠️ {error}
            </div>
          )}
        </div>
      </div>

      {loading && (
        <div className="upload-card glass loading">
          <div className="spinner"></div>
          <p className="loading-text">Optimizing your image...</p>
        </div>
      )}

      {(previewUrl || processedImageUrl) && !loading && (
        <div className="preview-section">
          <div className="preview-grid">
            {previewUrl && (
              <div className="preview-card glass">
                <h3>Original Image</h3>
                <div className="preview-image-container">
                  <img src={previewUrl} alt="Original" className="preview-image" />
                </div>
                <div className="preview-info">
                  <div className="preview-info-row">
                    <span>File Size:</span>
                    <strong>{formatFileSize(originalSize)}</strong>
                  </div>
                  <div className="preview-info-row">
                    <span>Format:</span>
                    <strong>{selectedFile?.type.split('/')[1].toUpperCase()}</strong>
                  </div>
                </div>
              </div>
            )}

            {processedImageUrl && (
              <div className="preview-card glass">
                <h3>Optimized Image</h3>
                <div className="preview-image-container">
                  <img src={processedImageUrl} alt="Processed" className="preview-image" />
                </div>
                <div className="preview-info">
                  <div className="preview-info-row">
                    <span>File Size:</span>
                    <strong>{formatFileSize(processedSize)}</strong>
                  </div>
                  <div className="preview-info-row">
                    <span>Format:</span>
                    <strong>JPEG</strong>
                  </div>
                  <div className="preview-info-row">
                    <span>Reduction:</span>
                    <strong style={{ color: '#00d4aa' }}>
                      {getCompressionRatio()}% smaller
                    </strong>
                  </div>
                </div>
                <button onClick={handleDownload} className="download-button">
                  ⬇️ Download Optimized Image
                </button>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  )
}

export default App
