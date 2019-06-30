# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:13:38 2019

@author: User1
"""                
                
with open('C:\\LeoraProjects\\bootcamp\\DSPG\\DownloadingAudioSet\\output\\urls_batch_no_music_speech_edited.txt','r') as source:
    lines_src = source.readlines()
with open('C:\\LeoraProjects\\bootcamp\\DSPG\\DownloadingAudioSet\\uri_downloadedfiles.txt','r') as f:
    lines_f = f.readlines()
destination = open("C:\\LeoraProjects\\bootcamp\\DSPG\\DownloadingAudioSet\\output\\urls_batch_no_music_speech_new.txt","w")
for data in lines_src:
    if data.split('https://www.youtube.com/watch?v=')[1].split('&feature=youtu.be')[0] + '.wav\n' not in lines_f:
        destination.write(data)
destination.close()