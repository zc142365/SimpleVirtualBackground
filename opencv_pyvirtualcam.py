import pyvirtualcam
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import mediapipe

# import flask
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import numpy as np

app = FastAPI()

class ImageString(BaseModel): #요청모델
    base64image: str

class CamState(BaseModel):
    state: str

class AppState(BaseModel):
    state: str

class ImageState(BaseModel):
    state: str

# class GetUser(BaseModel): #응답모델
#     name: str

@app.post('/post/image')
async def getImageString(imageString : ImageString):
    print(imageString + '\n입력')
    return 'Succeus'

@app.post('/post/camState')
async def getCamState(camState : CamState):
    if 'camOn' in camState:
        print('Cam On')
        return 'Cam On'
    elif 'camOff' in camState:
        print('Cam Off')
        return 'Cam Off'
    else:
        print('signal is not accurate')
        return 'signal is not accurate'

@app.post('/post/appState')
async def getAppState(appState : AppState):
    if 'appStart' in appState:
        print('App Start')
        return 'App Start'
    elif 'appStop' in appState:
        print('App Stop')
        return 'App Stop'
    else:
        print('signal is not accurate')
        return 'Signal is not accurate'

@app.port('/post/imageState')
async def getImageState(imageState : ImageState):
    if 'imageOn' in imageState:
        print('Image On')
        return 'Image On'
    elif 'imageOff' in imageState:
        print('Image Off')
        return 'Image Off'
    else: 
        print('signal is not accurate')
        return 'Signal is not accurate'

def capture():
    print('video capture start')
    cap = cv2.VideoCapture(0)
    camFps = (cap.get(cv2.CAP_PROP_FRAME_COUNT))
    camWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    camHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fmt = pyvirtualcam.PixelFormat.BGR
    segmentor = SelfiSegmentation()
    imgRead = cv2.imread('library1920.jpg')

def image_resize(imgRead,camWidth,camHeight):
    imgBackground = cv2.resize(imgRead, (camWidth, camHeight))

def cam_image_change():
    with pyvirtualcam.Camera(width=camWidth, height=camHeight, fps=camFps, fmt=fmt) as cam:
        print('ESC input is program end')
        while True:
            ret_val, frame = cap.read()
            # example
            # frameOut = segmentor.remove BG(frame, (0,255,0), threshold=0.9)
            frameOut = segmentor.removeBG(frame, imgBackground, threshold=0.87)
            
            cv2.imshow('myCaptureVideo', frameOut)
            
            cam.send(frameOut)
            cam.sleep_until_next_frame()
            if cv2.waitKey(1) == 27:
                break  # esc to quit
        cv2.destroyAllWindows()