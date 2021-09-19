import json
from PIL import Image
import cv2
import pytesseract 
import sys  
import os
import numpy as np
import re
import datetime
import joblib

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
clf = joblib.load("trained_model.sav")

def pred():
    with open("data.json","r") as f:
        data = json.load(f)
    pred = clf.predict(np.array(data).reshape(1,-1))
    ans = ["no you cannot claim your insurance","yes you can claim your insurance"]
    #print(ans[pred[0]])
    return ans[pred[0]]
    

if __name__ == "__main__":
    pred()
