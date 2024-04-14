from ultralytics import YOLO
import cv2


#model = YOLO("models\model_v0.pt") #load created model
model = YOLO("yolov8n.pt") #load pretrained model

video_path = 'videos\test_ball_detection.gif'
cap = cv2.VideoCapture(video_path)

ret = True

while ret:

    if ret:
        ret, frame = cap.read()

        results = model.track(frame, persist=True)
        frame_ = results[0].plot()


        cv2.imshow('frame', frame_)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
