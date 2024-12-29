#coding:utf-8
import cv2
from ultralytics import YOLO

# 所需加载的模型目录
path = 'models/best.pt'
# 需要检测的图片地址
video_path = "testfiles/vids/1.mp4"

# Load the YOLO model
model = YOLO(path)
cap = cv2.VideoCapture(video_path)

# category_dict = {
#     0: "车辆",  # 假设 0 对应车辆
#     1: "行人",  # 假设 1 对应行人
#     2: "障碍物"   # 假设 2 对应障碍
# }
# category_dict = {
#     0: "Person",      # 假设 0 对应行人
#     1: "Car",         # 假设 1 对应车辆
#     2: "Traffic cone" # 假设 2 对应障碍物
# }
#
# # 映射到你需要的提示语
# message_dict = {
#     "Car": "减速慢行",
#     "Person": "请停车",
#     "Traffic cone": "请避让"
# }

# Loop through the video frames
# 确保视频加载成功
# if not cap.isOpened():
#     print("Error: Could not open video.")
#     exit()
#
# # category_dict 和 message_dict 用于目标映射
# category_dict = {
#     0: "Person",  # 假设 0 对应行人
#     1: "Car",  # 假设 1 对应车辆
#     2: "Traffic cone"  # 假设 2 对应障碍物
# }
#
# message_dict = {
#     "Car": "减速慢行",
#     "Person": "请停车",
#     "Traffic cone": "请避让"
# }
#
# # Loop through the video frames
# while cap.isOpened():
#     # 读取视频的一帧
#     success, frame = cap.read()
#
#     if not success:
#         print("Error: Failed to read frame or video ended.")
#         break
#
#     try:
#         # 对帧进行YOLOv8推理
#         results = model(frame)
#
#         # 获取推理结果
#         boxes = results[0].boxes  # 获取所有检测框的预测结果
#         class_ids = boxes.cls  # 获取所有预测目标的类别ID
#         conf = boxes.conf  # 获取每个预测的置信度
#         labels = results[0].names  # 获取类别名称
#
#         # 打印检测到的目标信息
#         detected_objects = []
#         for class_id in class_ids:
#             class_id = int(class_id)
#             if class_id in category_dict:
#                 detected_objects.append(category_dict[class_id])
#
#         # 构造输出信息
#         if detected_objects:
#             # 输出目标的信息
#             objects_str = ', '.join(detected_objects)
#             output_message = f"0: {frame.shape[0]}x{frame.shape[1]} {len(detected_objects)} {objects_str}, {conf.mean():.1f}ms 检测到 {objects_str}，"
#             # 根据检测到的目标，输出相应的提示信息
#             for obj in detected_objects:
#                 output_message += message_dict.get(obj, "") + " "
#
#             print(output_message)
#         else:
#             print("未检测到目标")
#
#         # 可视化结果
#         annotated_frame = results[0].plot()
#
#         # 显示注释后的帧
#         cv2.imshow("YOLO Inference", annotated_frame)
#
#     except Exception as e:
#         print(f"Error during inference: {e}")
#
#     # 按'q'键退出循环
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# 释放视频捕捉对象并关闭窗口


# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        # annotated_frame = cv2.resize(annotated_frame, dsize=None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
        #print(results)
        # Display the annotated frame
        cv2.imshow("YOLO11 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# while cap.isOpened():
#     try:
#         # 读取视频的一帧
#         success, frame = cap.read()
#
#         if not success:
#             print("视频帧读取失败，退出...")
#             break
#
#         # 如果帧为空，跳过当前帧
#         if frame is None or len(frame) == 0:
#             print("空帧，跳过...")
#             continue
#
#         # 对帧进行YOLOv8推理
#         results = model(frame)
#
#         # 获取推理结果
#         annotations = results[0].boxes  # 获取所有检测框的预测结果
#         class_ids = annotations.cls  # 获取所有预测目标的类别ID
#         conf = annotations.conf  # 获取每个预测的置信度
#         labels = results[0].names  # 获取类别名称
#
#         # 打印检测到的目标信息
#         detected_objects = []
#         for class_id in class_ids:
#             class_id = int(class_id)
#             if class_id in category_dict:
#                 detected_objects.append(category_dict[class_id])
#
#         # 构造输出信息
#         if detected_objects:
#             # 将检测到的目标信息拼接成字符串
#             objects_str = ', '.join(detected_objects)
#             output_message = f"0: {frame.shape[0]}x{frame.shape[1]} {len(detected_objects)} {objects_str}, {conf.mean():.1f}ms 检测到 {objects_str}，"
#             if '车辆' in detected_objects:
#                 output_message += "减速慢行。"
#             elif '行人' in detected_objects:
#                 output_message += "请停车。"
#             elif '障碍' in detected_objects:
#                 output_message += "请避让。"
#             print(output_message)
#         else:
#             print("未检测到目标")
#
#         # 可视化结果
#         annotated_frame = results[0].plot()
#
#         # 显示注释后的帧
#         cv2.imshow("YOLO Inference", annotated_frame)
#
#         # 延迟，确保图像可以正常显示
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     except Exception as e:
#         print(f"发生错误: {e}")
#         break
# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()