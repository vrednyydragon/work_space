# FastAPI Streaming Service

This is a simple FastAPI application that provides two endpoints for streaming images. One endpoint streams images 
from local files, and the other streams an image from a URL.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To start the server, run the following command:

```bash
uvicorn main:app --reload
```

Then, you can access the following endpoints:

- `http://localhost:8000/` - Returns a plain text response saying 'Hello, It works!'
- `http://localhost:8000/stream/img/` - Streams images from local files `image1.jpg`, `image2.jpg`, and `image3.jpg`.
- `http://localhost:8000/stream/url/` - Streams an image from a specified URL.

## Note

The images to be streamed should be in the same directory as the `main.py` file. The URL for the image to be streamed 
is hardcoded in the `main.py` file and can be changed as per requirement.
```

