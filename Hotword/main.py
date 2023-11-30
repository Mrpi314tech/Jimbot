#!/bin/python3
import os
import time
import struct
import pyaudio
import pvporcupine
import sys
porcupine = None
pa = None
audio_stream = None

try:
    from Hotword import hinfo as hinfo
    pvp_passkey=hinfo.pvp_passkey
except:
    try:
        import hinfo
        pvp_passkey=hinfo.pvp_passkey
    except:
        os.system('~/Jimbot/Bash/Jimbotterminal python3 ~/Jimbot/Hotword/Access_key.py')
        sys.exit()
        exit()
pvp_passkey=hinfo.pvp_passkey
try:
    porcupine = pvporcupine.create(keyword_paths=["~/Jimbot/Hotword/Jimbot.ppn"], access_key=pvp_passkey)

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
                    rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)

    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            os.system("window_id=$(wmctrl -l | grep 'Jimbot' | awk '{print $1}') && wmctrl -i -a $window_id")
            os.system('xdotool key F10')
finally:
    if porcupine is not None:
        porcupine.delete()

    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
        pa.terminate()
