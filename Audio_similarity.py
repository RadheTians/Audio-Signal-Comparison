# -*- coding: utf-8 -*-
"""Copy of audio_similarity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gYQzDXqzu5YQCin93EOKjjH8EChbhQnX
"""

import scipy.fftpack as fft
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt 
import numpy as np
from scipy.signal import get_window
import math
import os


def cosine_similar(v1,v2):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)
path = '/home/radhetians/IPA/sound'
files = os.listdir(path)
(sample_rate2,cepstral_coefficents2) = wav.read("0001.wav") 
for i in files:
	try:
		(sample_rate1,cepstral_coefficents1) = wav.read(i) 
		if cepstral_coefficents1.shape[1] < cepstral_coefficents2.shape[1]:
		  th = cosine_similar(cepstral_coefficents1,cepstral_coefficents2[0:cepstral_coefficents1.shape[0]])
		else:
		  th = cosine_similar(cepstral_coefficents1[0:cepstral_coefficents2.shape[0]],cepstral_coefficents2)
		print(th)
	except Exception:
		pass



