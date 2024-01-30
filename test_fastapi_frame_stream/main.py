from fastapi import FastAPI
from fastapi.responses import StreamingResponse, PlainTextResponse
import time
import requests


app = FastAPI()


@app.get("/")
async def start():

    return PlainTextResponse('Hello, It works!')


@app.get("/stream/img/")
async def stream_from_img():
    return StreamingResponse(content=generate(), media_type="multipart/x-mixed-replace;boundary=frame")


@app.get("/stream/url/")
async def stream_from_url():
    return StreamingResponse(content=generate_url(), media_type="multipart/x-mixed-replace;boundary=frame")


def generate():
    while True:
        for image_path in ['image1.jpg', 'image2.jpg', 'image3.jpg']:
            with open(image_path, 'rb') as img:
                frame = img.read()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(1)


def generate_url():
    url: str = 'https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg'
    while True:
        # Fetch the image from the URL
        response = requests.get(url, stream=True)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + response.content + b'\r\n')
        time.sleep(1)

