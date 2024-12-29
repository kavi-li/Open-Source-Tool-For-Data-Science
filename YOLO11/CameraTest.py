#coding:utf-8
import cv2
from ultralytics import YOLO
import time

path = 'models/best.pt'

# Load the YOLO model
model = YOLO(path)

ID = 0

while(ID<10):
    cap = cv2.VideoCapture(ID)
    # get a frame
    ret, frame = cap.read()
    if ret == False:
        ID += 1
    else:
        print('摄像头ID:',ID)
        break

category_labels = {0: "Car", 1: "Pedestrain", 2: "Traffic Cone"}
category_messages = {
    0: "Vehicle detected, please slow down.",
    1: "Pedestrian detected, please stop.",
    2: "Obstacle detected, please make way."
}

# while cap.isOpened():
#     # 读取视频帧
#     success, frame = cap.read()
#
#     if success:
#         # 使用YOLO进行推理
#         results = model(frame)
#
#         # 获取推理结果
#         annotations = results[0].boxes  # 获取所有检测框的预测结果
#         class_ids = annotations.cls  # 获取所有预测目标的类别ID
#         conf = annotations.conf  # 获取每个预测的置信度
#         labels = results[0].names  # 获取类别名称
#
#         # 判断检测到的目标并输出不同信息
#         output_message = f"0: {frame.shape[0]}x{frame.shape[1]} "
#
#         # 目标数量
#         num_objects = len(class_ids)
#
#         # 检测到的目标类别处理
#         detected_objects = []
#
#         for i in range(num_objects):
#             class_id = int(class_ids[i])
#             if class_id == 0:  # 车辆
#                 detected_objects.append("车辆")
#             elif class_id == 1:  # 行人
#                 detected_objects.append("行人")
#             elif class_id == 2:  # 障碍物
#                 detected_objects.append("障碍")
#
#         # 拼接检测结果信息
#         if num_objects > 0:
#             objects_str = ', '.join(detected_objects)
#             output_message += f"{num_objects} {objects_str}, {conf.mean():.1f}ms"
#         else:
#             output_message += "未检测到目标, 0ms"
#
#         # 输出检测信息
#         print(output_message)
#
#         # 可视化结果
#         annotated_frame = results[0].plot()
#
#         # 显示注释后的帧
#         cv2.imshow("YOLO Inference", annotated_frame)
#
#     # 按'q'键退出循环
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     else:
#         # 视频结束后退出循环
#         break

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLO inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLO11 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break



# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()