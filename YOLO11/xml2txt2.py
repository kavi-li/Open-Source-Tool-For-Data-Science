# -*- coding: utf-8 -*-
"""
---------------------------------
Name: lijiayi
IDE: PyCharm
FileName: xml2txt2.py
Date: 2024/12/9 20:29
"""
import xml.etree.ElementTree as ET

import pickle
import os
from os import listdir, getcwd
from os.path import join
import glob

xml_folder = '/Users/karidalee/Desktop/finalpre/xml/'
txt_folder = '/Users/karidalee/Desktop/finalpre/txt/'


classes = ["Person", "Car", "Traffic Cone"]


def convert(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (round(x, 6), round(y, 6), round(w, 6), round(h, 6))

def convert_annotation(image_name):
    in_file = open('/Users/karidalee/Desktop/finalpre/xml/' + image_name[:-3] + 'xml')  # xml文件路径
    out_file = open('/Users/karidalee/Desktop/finalpre/txt/' + image_name[:-3] + 'txt', 'w')  # 转换后的txt文件存放路径
    f = in_file
    xml_text = f.read()
    root = ET.fromstring(xml_text)
    f.close()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            print(cls)
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()

if __name__ == '__main__':

    filenames = os.listdir('/Users/karidalee/Desktop/finalpre/xml/')

    for label_path in filenames:
        print(label_path)
        convert_annotation(label_path)

