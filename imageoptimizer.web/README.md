# Image Optimizer - React Frontend

A modern, high-performance interface for the Image Optimizer application, built with React and Vite.

## Features

✨ **Core Features:**
- 🖼️ **Drag-and-Drop Upload**: Intuitive zone for easy image selection.
- 🎨 **Glassmorphism UI**: Premium dark theme with gradients and blur effects.
- 🔄 **Real-time Preview**: Side-by-side comparison of original vs. optimized images.
- 🎚️ **Interactive Controls**: Adjustable quality slider (0-100%).
- 📊 **Smart Feedback**: Instant calculation of file size savings.
- ⬇️ **One-Click Download**: Easy export of optimized assets.
- 📱 **Responsive Design**: Flawless experience on desktop and mobile.

## Tech Stack

- **Framework**: React 18
- **Build Tool**: Vite
- **Styling**: Vanilla CSS3 (Variables, Flexbox, Grid)
- **State Management**: React Hooks
- **Icons**: Native Emojis & CSS Shapes

## Prerequisites

- Node.js 18+
- npm or yarn
- Backend running on `http://localhost:8080`

## Installation

1. Navigate to the web directory:
   ```bash
   cd imageoptimizer.web
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

The app will be available at [http://localhost:5173](http://localhost:5173).

## Configuration

This project uses environment variables for configuration.

1. Copy the example file:
   ```bash
   cp .env.example .env.local
   ```

2. Edit `.env.local` to set your backend URL:
   ```env
   VITE_API_BASE_URL=http://localhost:8080
   ```

## Project Structure

```
src/
├── App.jsx        # Main application logic & UI
├── App.css        # Component-specific styles
├── index.css      # Global design system & variables
├── main.jsx       # Application entry point
└── assets/        # Static assets
```

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## License

MIT License - feel free to use this project for personal or commercial purposes.
