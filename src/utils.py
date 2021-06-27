import subprocess
import speech_recognition as sr
from record import RecordAudio
import speech
import time
import csv

speech_key = {
    'do': '2',
    'dude': '2',
    'run': '1',
    'he': '3',
    'size': '5',
    'fired': '5',
    'Ford': '4',
    'I\'m lady': 'I\'m ready',
    'Zebulon': '7',
    'Kevin': '7',
    'Devin': '7', 
    'sweet': '3',
    'I\'m already': 'I\'m ready',
    'already': 'ready',
    'Siri': '3'
}

def speak( text ):
    print("[TTS] " + text)
    # tts_cmd = 'espeak -a 200 -v mb-en1 -s 150 "' + text + '" --stdout | aplay'
    tts_cmd = './google-tts.sh "' + text + '"'
    subprocess.check_output(tts_cmd, shell=True)

def play( music, start, stop ):
    print('[Playing] ' + music)
    cmd = 'mplayer -ss ' + str(start) + ' -endpos ' + str(stop) + ' ' + music
    # cmd = 'cvlc --play-and-exit --gain 7 ' + music + " --start-time=" + str(start) + " --stop-time=" + str(stop)
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

def log( id, text ):
    current_time = time.localtime(time.time())
    filename = "logs/study-" + id + '-' + str(current_time.tm_mon) + '-' + str(current_time.tm_mday) + '.log'
    file_ = open(filename, 'a')
    text = '[' + str(current_time.tm_hour) + ":" + str(current_time.tm_sec) + '] ' + text + '\n'
    file_.write(text)
    file_.close()

def csvSimple( log ):
    with open('logs/participant-log-simple.csv', mode='a') as csv_:
        writer_ = csv.writer(csv_, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer_.writerow(log)

def csvMulti( log ):
    with open('logs/participant-log-multi.csv', mode='a') as csv_:
        writer_ = csv.writer(csv_, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer_.writerow(log)
