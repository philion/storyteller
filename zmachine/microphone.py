#!/usr/bin/env python3

import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import json

class recognizer():
    def __init__(self):
        self.q = queue.Queue()
        self.model = vosk.Model(lang="en-us")
        self.device = 0
        self.samplerate = 44100 # reasonable defaults, for now

    def callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print("ERR:", status, file=sys.stderr)
        self.q.put(bytes(indata))

    def get_input(self):
        #print("Listening with device={}, samplerate={}", self.device, self.samplerate)
        print(".")
        with sd.RawInputStream(samplerate=self.samplerate, blocksize=8000, device=self.device, 
                            dtype='int16', channels=1, callback=self.callback):

            # timeout?
            rec = vosk.KaldiRecognizer(self.model, self.samplerate)
            while True:
                data = self.q.get()
                if rec.AcceptWaveform(data):
                    rslt = json.loads(rec.Result())
                    return rslt['text']

def main():
    rec = recognizer()
    result = rec.get_input()
    print("result:", result)

if __name__ == '__main__':
    main()