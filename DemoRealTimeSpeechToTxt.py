import os
import time
import azure.cognitiveservices.speech as speechsdk
from tkinter import *
import tkinter as tk

timestr = time.strftime("%Y%m%d-%H%M%S")
print (timestr)
filepath = r"C:/Demo Code/TwitchCaptioner-master/test123"+timestr+".txt"
print (filepath)
f = open(filepath, 'a', buffering=1)
appHeight = 150
padding = 20
labelText = NONE

def recognizing(args):
    global labelText
    labelText.set(args.result.text)

def recognized(args):
    global f
    if args.result.text.strip() != '':
        print(args.result.text + "\n")
        f.write(args.result.text + "\n")

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "b1a9ae31784041d9a1db9697dcdb3e20", "eastus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Say something...")

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

speech_recognizer.recognizing.connect(recognizing)
speech_recognizer.recognized.connect(recognized)
speech_recognizer.start_continuous_recognition()


time.sleep(15)