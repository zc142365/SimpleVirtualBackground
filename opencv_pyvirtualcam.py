import pyvirtualcam
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import mediapipe

print('비디오 캡쳐 시작')
cap = cv2.VideoCapture(0)
camFps = (cap.get(cv2.CAP_PROP_FRAME_COUNT))
camWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
camHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fmt = pyvirtualcam.PixelFormat.BGR
segmentor = SelfiSegmentation()
imgRead = cv2.imread('library1920.jpg')
imgBackground = cv2.resize(imgRead, (camWidth, camHeight))
with pyvirtualcam.Camera(width=camWidth, height=camHeight, fps=camFps, fmt=fmt) as cam:
    print('ESC입력시 종료')
    while True:
        ret_val, frame = cap.read()
        # frameOut = segmentor.remove BG(frame, (0,255,0), threshold=0.9)
        frameOut = segmentor.removeBG(frame, imgBackground, threshold=0.87)
        
        # 수정된 프레임 보는 코드
        # cv2.imshow('myCaptureVideo', frameOut)
        
        cam.send(frameOut)
        cam.sleep_until_next_frame()
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()