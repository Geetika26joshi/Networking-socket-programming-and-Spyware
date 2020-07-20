#Geetika Joshi
#2019h1030124h

import pyaudio
import wave

# output file name
name = "recordedAud.mp3"
chunk = 1024
# sample format
FORMAT = pyaudio.paInt16
channels = 1
# 44100 samples per second
sample_rate = 44100
record_seconds = 10
# initialize PyAudio object
obj = pyaudio.PyAudio()
# open stream object as input & output
stream = obj.open(format=FORMAT,
                channels=channels,
                rate=sample_rate,
                input=True,
                output=True,
                frames_per_buffer=chunk)
frames = []
print("Recording audio...")
for i in range(int(44100 / chunk * record_seconds)):
    data = stream.read(chunk)
    frames.append(data)
print("Finished recording.")

stream.stop_stream()
stream.close()
# terminate pyaudio object
obj.terminate()
wfile = wave.open(name, "wb")

wfile.setnchannels(channels)
wfile.setsampwidth(obj.get_sample_size(FORMAT))

wfile.setframerate(sample_rate)

wfile.writeframes(b"".join(frames))
wfile.close()
