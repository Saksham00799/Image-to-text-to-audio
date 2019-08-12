import pytesseract
from PIL import Image
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import cv2

from googletrans import Translator
translator = Translator()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

img=cv2.imread('2.png')

grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 115, 1)

blur=cv2.GaussianBlur(grayscaled,(5,5),0)

canny=cv2.Canny(blur,50,150)
    
text=pytesseract.image_to_string(grayscaled)

trans=translator.translate(text, dest='hi')
cv2.imshow('img',img)
cv2.imshow('grayscaled',grayscaled)
cv2.imshow('gaus',gaus)
cv2.imshow('canny',canny)

print(text)
speak(text)
print("\n\ntranslated text is given below \n")
print(trans)
cv2.waitKey(0)
cv2.destroyAllWindows()

