from ultralytics import YOLO

model = YOLO("yolov8s.pt")

model.train(data="dataset/data.yaml", epochs=5, device=[-1, -1])

model.export(format="onnx")
