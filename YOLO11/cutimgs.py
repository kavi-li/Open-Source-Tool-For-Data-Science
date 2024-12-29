# -*- coding: utf-8 -*-
"""
---------------------------------
Name: lijiayi
IDE: PyCharm
FileName: cutimgs.py
Date: 2024/12/5 19:33
"""
import cv2
import os

def extract_frames(video_folder, output_folder, interval=15):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # get all files
    video_files = [f for f in os.listdir(video_folder) if f.lower().endswith(('.mp4', '.avi', '.mov'))]

    # go through each video file
    for video_file in video_files:
        video_path = os.path.join(video_folder, video_file)

        # open the video file
        cap = cv2.VideoCapture(video_path)

        # gets the frame rate of the video
        fps = cap.get(cv2.CAP_PROP_FPS)

        # gets the total number of frames of the video
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Calculate the number of frames per 10 seconds
        frame_interval = int(fps * interval)

        print(
            f"Processing video: {video_file}, FPS: {fps}, Total Frames: {total_frames}, Frame Interval: {frame_interval}")

        # initialize
        frame_count = 0
        image_count = 1

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # grab an image every 10 seconds
            if frame_count % frame_interval == 0:
                image_filename = f"{image_count}.jpg"
                image_path = os.path.join(output_folder, image_filename)
                cv2.imwrite(image_path, frame)
                print(f"Saved: {image_filename}")
                image_count += 1

            frame_count += 1

        # release
        cap.release()

    print("All videos processed successfully.")

video_folder = '/Users/karidalee/Desktop/train/'
output_folder = '/Users/karidalee/Desktop/train/videos/'

extract_frames(video_folder, output_folder)