#!/usr/bin/env python3

import queue
import sounddevice as sd
import vosk
import sys
import json

class hear():
    def __init__(self):
        vosk.SetLogLevel(-1) # Turn off vosk logging

        self.q = queue.Queue()
        self.model = vosk.Model(lang="en-us")
        self.device = 0
        self.samplerate = 44100 # reasonable defaults, for now

    def callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print("ERR:", status, file=sys.stderr)
        self.q.put(bytes(indata))

    def text(self):
        #print("Listening with device={}, samplerate={}", self.device, self.samplerate)
        #print(".")
        with sd.RawInputStream(samplerate=self.samplerate, blocksize=8000, device=self.device, 
                            dtype='int16', channels=1, callback=self.callback):

            # timeout?
            rec = vosk.KaldiRecognizer(self.model, self.samplerate)
            while True:
                data = self.q.get()
                if rec.AcceptWaveform(data):
                    rslt = json.loads(rec.FinalResult())
                    return rslt['text']

def main():
    print("result:", hear().text())

if __name__ == '__main__':
    main()