// Configuration
const CONFIG = {
    // Replace with your actual API endpoint
    API_BASE_URL: 'http://localhost:8000',
    // Replace with your actual Google API key
    GOOGLE_API_KEY: 'YOUR_GOOGLE_API_KEY_HERE'
};

// DOM Elements
const elements = {
    imagePreview: document.getElementById('imagePreview'),
    cameraButton: document.getElementById('cameraButton'),
    uploadButton: document.getElementById('uploadButton'),
    fileInput: document.getElementById('fileInput'),
    ingredientsSection: document.getElementById('ingredientsSection'),
    ingredientsList: document.getElementById('ingredientsList'),
    recipeSection: document.getElementById('recipeSection'),
    recipeTitle: document.getElementById('recipeTitle'),
    recipeIngredients: document.getElementById('recipeIngredients'),
    recipeInstructions: document.getElementById('recipeInstructions'),
    getRecipeButton: document.getElementById('getRecipeButton'),
    clearButton: document.getElementById('clearButton'),
    newRecipeButton: document.getElementById('newRecipeButton'),
    loadingIndicator: document.getElementById('loadingIndicator'),
    loadingText: document.getElementById('loadingText'),
    errorMessage: document.getElementById('errorMessage'),
    errorText: document.getElementById('errorText'),
    closeError: document.getElementById('closeError')
};

// State
let currentImage = null;
let identifiedIngredients = [];

// Initialize the app
function init() {
    // Event listeners
    elements.cameraButton.addEventListener('click', captureImage);
    elements.uploadButton.addEventListener('click', () => elements.fileInput.click());
    elements.fileInput.addEventListener('change', handleFileSelect);
    elements.getRecipeButton.addEventListener('click', getRecipe);
    elements.clearButton.addEventListener('click', clearAll);
    elements.newRecipeButton.addEventListener('click', resetApp);
    elements.closeError.addEventListener('click', hideError);
    
    // Check for API key
    if (CONFIG.GOOGLE_API_KEY === 'YOUR_GOOGLE_API_KEY_HERE') {
        showError('Please set your Google API key in the app.js file.');
    }
}

// Capture image using device camera
async function captureImage() {
    try {
        showLoading('Accessing camera...');
        
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        const video = document.createElement('video');
        video.srcObject = stream;
        video.play();
        
        // Wait for video to be ready
        await new Promise(resolve => {
            video.onloadedmetadata = () => resolve();
        });
        
        // Create a canvas to capture the image
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        // Stop the camera
        stream.getTracks().forEach(track => track.stop());
        
        // Convert to blob and display
        canvas.toBlob(blob => {
            const imageUrl = URL.createObjectURL(blob);
            displayImage(imageUrl);
            currentImage = blob;
            hideLoading();
            
            // Automatically identify ingredients
            identifyIngredients(blob);
        }, 'image/jpeg', 0.8);
    } catch (error) {
        hideLoading();
        showError('Failed to access camera: ' + error.message);
    }
}

// Handle file selection
function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file && file.type.startsWith('image/')) {
        const imageUrl = URL.createObjectURL(file);
        displayImage(imageUrl);
        currentImage = file;
        
        // Automatically identify ingredients
        identifyIngredients(file);
    } else {
        showError('Please select a valid image file.');
    }
}

// Display image in preview area
function displayImage(imageUrl) {
    elements.imagePreview.innerHTML = '';
    const img = document.createElement('img');
    img.src = imageUrl;
    img.alt = 'Captured ingredients';
    elements.imagePreview.appendChild(img);
}

// Identify ingredients using backend API
async function identifyIngredients(imageBlob) {
    try {
        showLoading('Identifying ingredients...');
        
        // Convert blob to base64
        const base64Image = await blobToBase64(imageBlob);
        
        // Send image to backend for ingredient identification
        const response = await fetch(`${CONFIG.API_BASE_URL}/api/v1/identify-ingredients`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                image_data: base64Image
            })
        });
        
        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }
        
        const data = await response.json();
        const ingredients = data.ingredients;
        
        if (ingredients.length > 0) {
            identifiedIngredients = ingredients;
            displayIngredients(ingredients);
            elements.ingredientsSection.style.display = 'block';
        } else {
            showError('Could not identify any ingredients in the image. Please try another image.');
        }
        
        hideLoading();
    } catch (error) {
        hideLoading();
        showError('Failed to identify ingredients: ' + error.message);
    }
}

// Convert blob to base64
function blobToBase64(blob) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onloadend = () => resolve(reader.result);
        reader.onerror = reject;
        reader.readAsDataURL(blob);
    });
}

// Display identified ingredients
function displayIngredients(ingredients) {
    elements.ingredientsList.innerHTML = '';
    
    ingredients.forEach((ingredient, index) => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span>${ingredient}</span>
            <button class="remove-ingredient" data-index="${index}">Remove</button>
        `;
        elements.ingredientsList.appendChild(li);
    });
    
    // Add event listeners to remove buttons
    document.querySelectorAll('.remove-ingredient').forEach(button => {
        button.addEventListener('click', function() {
            const index = parseInt(this.getAttribute('data-index'));
            removeIngredient(index);
        });
    });
}

// Remove an ingredient
function removeIngredient(index) {
    identifiedIngredients.splice(index, 1);
    displayIngredients(identifiedIngredients);
    
    // Hide ingredients section if no ingredients left
    if (identifiedIngredients.length === 0) {
        elements.ingredientsSection.style.display = 'none';
    }
}

// Get recipe from backend API
async function getRecipe() {
    if (identifiedIngredients.length === 0) {
        showError('Please identify some ingredients first.');
        return;
    }
    
    try {
        showLoading('Getting recipe...');
        
        const response = await fetch(`${CONFIG.API_BASE_URL}/api/v1/recipes`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                ingredients: identifiedIngredients
            })
        });
        
        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }
        
        const recipe = await response.json();
        
        displayRecipe(recipe);
        elements.recipeSection.style.display = 'block';
        
        hideLoading();
    } catch (error) {
        hideLoading();
        showError('Failed to get recipe: ' + error.message);
    }
}

// Display recipe
function displayRecipe(recipe) {
    elements.recipeTitle.textContent = recipe.title;
    
    // Display ingredients
    elements.recipeIngredients.innerHTML = '';
    const ingredientsList = document.createElement('ul');
    recipe.ingredients.forEach(ingredient => {
        const li = document.createElement('li');
        li.textContent = ingredient;
        ingredientsList.appendChild(li);
    });
    elements.recipeIngredients.appendChild(ingredientsList);
    
    // Display instructions
    elements.recipeInstructions.textContent = recipe.instructions;
}

// Clear all
function clearAll() {
    // Reset image preview
    elements.imagePreview.innerHTML = '<p>No image captured yet</p>';
    
    // Reset ingredients
    identifiedIngredients = [];
    elements.ingredientsList.innerHTML = '';
    elements.ingredientsSection.style.display = 'none';
    
    // Reset recipe
    elements.recipeSection.style.display = 'none';
    
    // Reset file input
    elements.fileInput.value = '';
    
    currentImage = null;
}

// Reset app for new recipe
function resetApp() {
    // Hide recipe section
    elements.recipeSection.style.display = 'none';
    
    // Keep ingredients visible for modification
    elements.ingredientsSection.style.display = 'block';
}

// Show loading indicator
function showLoading(text = 'Processing...') {
    elements.loadingText.textContent = text;
    elements.loadingIndicator.style.display = 'flex';
}

// Hide loading indicator
function hideLoading() {
    elements.loadingIndicator.style.display = 'none';
}

// Show error message
function showError(message) {
    elements.errorText.textContent = message;
    elements.errorMessage.style.display = 'block';
}

// Hide error message
function hideError() {
    elements.errorMessage.style.display = 'none';
}

// Initialize the app when the DOM is loaded
document.addEventListener('DOMContentLoaded', init);