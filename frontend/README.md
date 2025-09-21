# AI Recipe Finder Frontend

A web-based frontend application that allows users to capture images of ingredients and retrieve recipes through the AI Recipe Agent API.

## Features

- Capture images using device camera or upload from file system
- Ingredient identification from images (simulated in this version)
- Recipe retrieval based on identified ingredients
- Responsive design that works on mobile, tablet, and desktop devices
- Clean and intuitive user interface

## Files

- `index.html` - Main HTML structure
- `styles.css` - Styling and responsive design
- `app.js` - JavaScript functionality and API integration

## Setup Instructions

1. **Place the frontend files** in a web-accessible directory on your server or local machine.

2. **Configure the API endpoint** in `app.js`:
   ```javascript
   const CONFIG = {
       API_BASE_URL: 'http://localhost:8000',  // Change this to your backend API URL
       GOOGLE_API_KEY: 'YOUR_GOOGLE_API_KEY_HERE'  // Add your Google API key
   };
   ```

3. **Serve the files** using any web server:
   - For development, you can use Python's built-in server:
     ```bash
     python -m http.server 8080
     ```
   - Or use any other web server like Apache, Nginx, etc.

4. **Access the application** by navigating to the server URL in your web browser.

## Usage

1. Open the application in a web browser
2. Click "Use Camera" to take a picture of your ingredients or "Upload Image" to select an image file
3. The application will automatically identify ingredients in the image (simulated in this version)
4. Review the identified ingredients and remove any incorrect ones
5. Click "Get Recipe" to retrieve a recipe based on the ingredients
6. The recipe will be displayed on the screen

## Integration with Backend API

This frontend is designed to work with the AI Recipe Agent REST API. Make sure the backend is running and accessible from the frontend.

### API Endpoints Used

- `POST /api/v1/recipes` - To retrieve recipes based on ingredients

## Browser Compatibility

This application uses modern web technologies and works best in recent versions of:
- Chrome
- Firefox
- Safari
- Edge

## Security Considerations

- In a production environment, the Google API key should not be exposed in client-side code
- Consider implementing the image recognition functionality on the backend for better security
- Use HTTPS for all API communications

## Future Improvements

1. Implement actual Google Gemini API integration for ingredient identification
2. Add image preprocessing for better recognition accuracy
3. Implement caching of previously identified ingredients
4. Add support for dietary preferences
5. Improve error handling and user feedback
6. Add unit tests for JavaScript functions