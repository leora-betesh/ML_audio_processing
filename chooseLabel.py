# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:52:30 2019

@author: Leora Betesh and Yael Chomski Bar-Siman-Tov

Create a small dataset from AudioSet for initial testing of NNs
"""
import pandas as pd
import os
from shutil import copyfile

source_dir = "/BC2/Transfer_Learning/Data/AudioSet/student_files/"
input_csv_file = "no_music_speech_min.csv"
#output_csv_file = "small_dataset.csv"

class_dict = {"Microwave":  "/m/0fx9l", 
           "Doorbell": "/m/03wwcy",
           "Blender": "/m/02pjr4",
           "Thunderstorm": "/m/0jb2l",
           "Fire": "/m/02_41",
           "Waterfall": "/m/0j2kx",
           "Bark": "/m/05tny_",
           "Meow": "/m/07qrkrw",
           "Aircraft": "/m/0k5j",
           "Heart": "/m/01jg02"}


NUM_INSTANCES = 70

data = pd.read_csv(input_csv_file)
data.rename(columns={'#YTID':'YTID'}, inplace=True)
data = data[data.YTID != "#NAME?"]
data = data[data.YTID != "#VALUE!"]          

for key, item in class_dict.items():
    print("------------",key,"------------")
    samples = data[data.L1 == item ]["YTID"][0:NUM_INSTANCES]
    for file_id in samples:
        if os.path.isfile(source_dir+file_id+".wav"):
            print("Copying", source_dir+file_id+".wav to ", "/"+key+"/"+file_id+".wav")            
            copyfile(source_dir+file_id+".wav", key+"/"+file_id+".wav")
 	       
