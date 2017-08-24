# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:46:31 2017

@author: Ronak
"""

import os
from glob import glob
import pandas as pd
import cv2

def load_images_from_folder(folder):
    images = []
    heights = []
    widths = []
    print folder
    for filename in glob(folder):
        img = cv2.imread(filename)
        height, width, channels = img.shape
        images.append(img)
        heights.append(height)
        widths.append(width)
    print len(images)
    return heights,widths


def csv_to_csv(df):
    filenames=[]
    xmins=[]
    ymins=[]
    xmaxs=[]
    ymaxs=[]
    for i in range(len(df)):      
        filenames.append(df.filename[i])
        xmins.append(df.x1[i])
        ymins.append(df.y1[i])
        xmaxs.append(df.x2[i])
        ymaxs.append(df.y2[i])
    df2=pd.DataFrame()
    df2['filename']=filenames
    df2['xmin']=xmins
    df2['ymin']=ymins
    df2['xmax']=xmaxs
    df2['ymaxs']=ymaxs
    return df2
    
    
def main():
    image_path = "C:\Users\Ronak\Desktop\Important\FastAI\\testingimages\\train\\Tee\*.jpg"
    info_path = "C:\Users\Ronak\Desktop\Important\FastAI\\blouse_info.csv"
    df= pd.read_csv(info_path)
    df3= csv_to_csv(df)
    heights,widths= load_images_from_folder(image_path)
    print len(heights), len(list(df3.filename))
    df3['height']=heights
    df3['width']=widths
    print df3.head()
#    xml_df = img_to_csv(image_path)
    df3.to_csv('raccoon_labels.csv', index=None)
    print('Successfully converted xml to csv.')


main()