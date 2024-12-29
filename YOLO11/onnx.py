# -*- coding: utf-8 -*-
"""
---------------------------------
Name: lijiayi
IDE: PyCharm
FileName: onnx.py
Date: 2024/12/14 14:48
"""
from ultralytics import YOLO

# load the model
model = YOLO(r"./models/best.pt")

model.export(
    format="onnx",
    imgsz=(640, 640),
    keras=False,
    optimize=False,
    half=False,
    int8=False,
    dynamic=False,
    simplify=True,
    opset=None,
    workspace=4.0,
    nms=False,
    batch=1,
    device="cpu"
)
