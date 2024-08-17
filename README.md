
<h1>Django Weather App</h1>
<br>
A simple web application built with Django that allows users to get current weather information for any city using the OpenWeatherMap API.
<br>
Features:
<br>
-User-friendly interface for entering city names.
<br>
-Displays current temperature, humidity, country code, and coordinates.
<br>
-Uses OpenWeatherMap API to fetch real-time weather data.
<br>
-Securely manages API key using environment variables.
<br>
Prerequisites:
<br>
-Python 3.x
<br>
-Django 3.x or later
<br>
-OpenWeatherMap API Key
<br>


<br>

Usage:
<br>
Enter the name of the city you want to get the weather information for in the input field.
Click on the "Get Weather" button.
The app will display the current weather details, including temperature, humidity, country code, and coordinates.
<br>

Code Overview
<br>
views.py:
The views.py file contains the main logic for fetching and displaying the weather data.
<br>
weather.html:
The weather.html template file provides the frontend for the app.
<br>

Acknowledgements:
Django
OpenWeatherMap
python-decouple

# Hacker News API with FastAPI

## Overview

This project provides a FastAPI-based API that interacts with the Hacker News API to fetch and display top news items. It features caching with `cachetools`, error handling, and can be run using Docker or directly in a virtual environment.

## Features

- **API Endpoint**: Retrieves top news items from Hacker News.
- **Caching**: Uses in-memory caching with `cachetools` to store results for 10 minutes.
- **Error Handling**: Manages cases where the Hacker News API is unavailable or returns an error.
- **Dockerization**: The application is containerized for easy deployment.
- **Logging**: Includes logging for debugging and monitoring.

## Prerequisites

- **Docker** (optional, for containerized setup)
- **Python 3.11** (if not using Docker)
- **pip** (Python package installer)

## Setup Instructions

### Using Docker

1. **Build the Docker Image**

```
   docker build -t fastapi-app . 
```   
   
2. **Run the Docker Container**

```
  docker run -d --name fastapi-container -p 8000:8000 fastapi-app
```  

3. **Access the API**

Open your browser and navigate to http://localhost:8000 or use curl to test the API:

```
  curl http://localhost:8000/top-news?count=5
```  


5. **Without Docker**
## Set Up a Virtual Environment

```
python -m venv venv
```
```
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

6. **Install Dependencies**

```
pip install -r requirements.txt
```
7. **Run the Application**

```
Copy code
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

8. **Access the API**

Open your browser and navigate to http://localhost:8000 or use curl:

```
curl http://localhost:8000/top-news?count=5
```

## API Endpoint

### GET /top-news
Retrieve the top news items from Hacker News.

#### Query Parameters:
- **count** (optional): The number of top news items to return. Defaults to 10 if not specified.

#### Responses:
- **200 OK**: Returns a JSON array of top news items.
- **500 Internal Server Error**: Returns an error message if there is an issue with the Hacker News API.


### Assumptions
- **API Rate Limiting**: It is assumed that the Hacker News API does not impose strict rate limits. The application handles errors gracefully if rate limits are exceeded.

- **Dependencies**: All dependencies are specified in requirements.txt, including pytest, httpx, fastapi, uvicorn, and cachetools.
- **Environment**: The application is designed to run in both Docker and a local virtual environment. The Dockerfile uses Python 3.11 and the requirements.txt file includes all necessary packages.

## Additional Notes
- **Caching**: In-memory caching is implemented using cachetools to minimize API calls to Hacker News. The cache duration is set to 10 minutes.
- **Logging**: Logging is implemented to track API requests and responses, which aids in debugging and monitoring.


