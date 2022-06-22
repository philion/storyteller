#!/usr/bin/env python3

import queue
import sounddevice as sd
import sys
import json

try:
    import pyttsx3
    tts = True
except:
    tts = False

class speak():
    def __init__(self):
        if tts:
            self.engine = pyttsx3.init() # speak!
        else:
            print("pip install pyttsx3")

    def text(self, text):
        if tts:
            self.engine.say(text)
            self.engine.runAndWait()
        else:
            print(text)

def main():
    speak().text("this is a test.")

if __name__ == '__main__':
    main()