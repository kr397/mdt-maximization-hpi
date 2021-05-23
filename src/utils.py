import subprocess
import speech_recognition as sr
from record import RecordAudio
import speech

speech_key = {
    'do': '2',
    'dude': '2',
    'run': '1',
    'he': '3',
    'size': '5',
    'fired': '5',
}

def speak( text ):
    print("[TTS] " + text)
    # tts_cmd = 'espeak -a 200 -v mb-en1 -s 150 "' + text + '" --stdout | aplay'
    tts_cmd = '../google-tts.sh "' + text + '"'
    subprocess.check_output(tts_cmd, shell=True)

def play( music, start, stop ):
    print('[Playing] ' + music)
    cmd = 'cvlc --play-and-exit ' + music + " --start-time=" + str(start) + " --stop-time=" + str(stop)
    # cmd = 'omxplayer --no-keys -o local ' + music
    subprocess.check_output(cmd, shell=True)

def recognize( rec, mic ):
    running = True
    result = ""
    print("[Recognizing]")

    mic.record()
    result = speech.recognize(mic.save())

    # Check in variations
    if result in speech_key:
        result = speech_key[result]

    return result
