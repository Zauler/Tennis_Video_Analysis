from ultralytics import YOLO

model = YOLO('models/yolov8x')

results = model.track('input_videos/input_video.mp4', conf=0.2, save = True)
print(results)
print("boxes:")
for box in results[0].boxes:
    print(box)