import os
import numpy
import librosa
import urllib.request

def download_google_drive(url, name):
    file_id = url[url.find("=")+1:]
    url = "https://drive.google.com/uc?export=download&id={0}".format(file_id)
    urllib.request.urlretrieve(url, name)
