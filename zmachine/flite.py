#!/usr/bin/env python3

import os
import sys
import tempfile
import subprocess
import sounddevice as sd
import soundfile as sf

class speak():
    def __init__(self):
        # any config?
        pass

    def text(self, text):
        # find the voice
        voice_file = os.path.abspath(os.path.join("voices", "cmu_us_aew.flitevox"))
        cmd = [
            'flite',
            '-voice', voice_file,
            '-t', text
        ]
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=True) as f:
            cmd.append(f.name)
            subprocess.call(cmd)
            self.play(f.name)
    
    def play(self, filename):
        '''
        Plays the sounds.
        :filename: The input file name
        '''
        try:
            data, fs = sf.read(filename, dtype='float32')
            sd.play(data, fs)
            status = sd.wait() # externalize wait.
            if status:
                print('Error during playback: ' + str(status))

        except Exception as e:
            print(type(e).__name__ + ': ' + str(e), file=sys.stderr)
            print(sd.query_devices())

def main():
    speak().text("This is a test. I'm sorry you have to listen to it.")

if __name__ == '__main__':
    main()