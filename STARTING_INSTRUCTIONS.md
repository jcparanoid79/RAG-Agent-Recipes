# AI Recipe Finder - Starting Instructions

## Prerequisites
1. Python 3.6+ installed
2. Required Python packages installed (run `pip install -r requirements.txt`)
3. Google API key configured in environment variables

## Starting the Application

### Option 1: Using the Batch Script (Windows)
1. Double-click on `start_all.bat` to start both the backend API and frontend
2. The script will automatically:
   - Start the backend API on `http://localhost:8000`
   - Start the frontend on `http://localhost:8080`
   - Open command windows for both services

### Option 2: Manual Start

#### Starting the Backend API:
1. Open a terminal/command prompt
2. Navigate to the project root directory
3. Run the following command:
   ```bash
   python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
4. The API will be available at `http://localhost:8000`

#### Starting the Frontend:
1. Open a second terminal/command prompt
2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
3. Start the HTTP server:
   ```bash
   python -m http.server 8080
   ```
4. The frontend will be available at `http://localhost:8080`

## Accessing the Application
1. Open your web browser
2. Navigate to `http://localhost:8080`
3. Start using the application to capture ingredient images and get recipes!

## Stopping the Application
- Close the terminal/command prompt windows
- Or press `CTRL+C` in each terminal to stop the services gracefully

## Troubleshooting
1. **Port Conflicts**: If ports 8000 or 8080 are already in use, modify the start commands to use different ports
2. **Missing Dependencies**: Run `pip install -r requirements.txt` to install all required packages
3. **API Key Issues**: Ensure your Google API key is properly configured in environment variables