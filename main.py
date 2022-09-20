import speech_recognition as sr
from os import path
from pydub import AudioSegment
import sys

sound = AudioSegment.from_mp3(sys.argv[1])
sound.export("output.wav", format="wav")

Audio_File = "output.wav"

r = sr.Recognizer()
with sr.AudioFile(Audio_File) as source:
    audio = r.record(source)
    output = ['Transcription: ' + r.recognize_google(audio)]
    with open('output.txt', 'w') as f:
        f.writelines(output)
