# AI Recipe Finder Frontend - Deployment Guide

## Overview
This document provides instructions for deploying and using the AI Recipe Finder frontend application. The frontend allows users to capture images of ingredients and retrieve recipes through the AI Recipe Agent API.

## Prerequisites
- Python 3.6+ (for local development server)
- Web browser (Chrome, Firefox, Safari, or Edge)
- Backend API running (see backend deployment instructions)

## Deployment Options

### 1. Local Development Deployment
For development and testing purposes:

1. Ensure the backend API is running on `http://localhost:8000`
2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
3. Start a simple HTTP server:
   ```bash
   python -m http.server 8080
   ```
4. Open your web browser and navigate to `http://localhost:8080`

### 2. Production Deployment
For production environments, you can deploy the frontend using any web server:

#### Using Apache
1. Copy all files from the `frontend` directory to your web server's document root
2. Ensure the web server is configured to serve static files
3. Update the `API_BASE_URL` in `app.js` to point to your production backend API

#### Using Nginx
1. Copy all files from the `frontend` directory to your web server's document root
2. Configure Nginx to serve static files:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           root /path/to/frontend/files;
           index index.html;
           try_files $uri $uri/ =404;
       }
   }
   ```
3. Update the `API_BASE_URL` in `app.js` to point to your production backend API

#### Using GitHub Pages
1. Create a GitHub repository for your frontend files
2. Push the contents of the `frontend` directory to the repository
3. Enable GitHub Pages in the repository settings
4. Update the `API_BASE_URL` in `app.js` to point to your production backend API

## Configuration
Before deploying, update the configuration in `app.js`:

```javascript
const CONFIG = {
    // Replace with your actual API endpoint
    API_BASE_URL: 'http://localhost:8000',  // Change this to your backend API URL
    // Replace with your actual Google API key
    GOOGLE_API_KEY: 'YOUR_GOOGLE_API_KEY_HERE'  // Add your Google API key
};
```

## Usage Instructions

### Capturing Images
1. Open the application in a web browser
2. Click "Use Camera" to take a picture of your ingredients or "Upload Image" to select an image file
3. The application will automatically identify ingredients in the image
4. Review the identified ingredients and remove any incorrect ones
5. Click "Get Recipe" to retrieve a recipe based on the ingredients
6. The recipe will be displayed on the screen

### Supported Browsers
- Chrome (latest version)
- Firefox (latest version)
- Safari (latest version)
- Edge (latest version)

### Mobile Usage
The application is fully responsive and works on mobile devices:
1. Access the application through your mobile browser
2. Allow camera permissions when prompted
3. Use the "Use Camera" button to take pictures directly from your mobile device

## Troubleshooting

### Common Issues
1. **CORS Errors**: Ensure the backend API has proper CORS configuration
2. **Camera Access Denied**: Check browser permissions for camera access
3. **API Connection Failed**: Verify the backend API is running and accessible
4. **No Ingredients Identified**: Try a clearer image with well-defined ingredients

### Browser Compatibility
- Ensure JavaScript is enabled in your browser
- For camera functionality, use HTTPS in production environments
- Clear browser cache if experiencing issues with updated files

## Security Considerations
- In production, do not expose API keys in client-side code
- Use HTTPS for all communications
- Implement proper authentication and authorization if needed
- Sanitize all user inputs on the backend

## Performance Optimization
- Optimize images before uploading for faster processing
- Use a CDN for static assets in production
- Implement caching strategies for better user experience
- Minify CSS and JavaScript files for production

## Maintenance
- Regularly update dependencies
- Monitor API usage and performance
- Backup configuration files before making changes
- Test thoroughly after any updates

## Support
For issues or questions, please refer to the main project documentation or contact the development team.