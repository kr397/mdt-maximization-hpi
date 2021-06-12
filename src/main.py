from comparative import simpleComparative, multiComparative
from descriptive import simpleDescriptive, multiDescriptive
from imagery import simpleImagery, multiImagery
from control import simpleControl, multiControl
from practice import simplePractice, multiPractice
import utils
from record import RecordAudio
import speech

import sys
import time
import random
import speech_recognition as sr

# Main function
def main():
    # Get participant ID
    p_id = input("Participant ID: ")

    # Initialize speech recognition
    rec = sr.Recognizer()
    mic = RecordAudio()

    # Prepare the sequence of conditions depending on command line args
    scond_l = []
    mcond_l = []
    done_l = []
    # Default setting 
    rand_l = list(range(1,5))
    rand_l = random.sample(rand_l, len(rand_l))
    for i in rand_l:
        scond_l.append('S' + str(i))
    for i in rand_l:
        mcond_l.append('M' + str(i))

    print(scond_l)

    # Sessions done already
    if ( len(sys.argv) > 1 ):
        done_l = sys.argv[1:]
    print(done_l)

    # Randomize between the different conditions
    l = list(range(4))
    l_random = random.sample(l, len(l))
    
    ### SIMPLE CHOICE TASK

    print("SIMPLE CHOICE TASK")
    utils.log(p_id, "SIMPLE CHOICE TASK")

    if ( len(done_l) == 0 ):
        utils.speak("Phase 1. Practice Round.")
        simplePractice(p_id, rec, mic)
    elif ( len(done_l) < 4 ) :
        text = 'Please say you are ready when you want to move to the next part.'
        utils.speak( text )

        command = utils.recognize( rec, mic )
        while not ("ready" in command):
            if (not command == ""):
                utils.speak( "I'm sorry, I did not catch that. Please speak again." )
            command = utils.recognize( rec, mic)

    # Iterate over the list to execute different simple choice conditions
    for i in scond_l:
        print(i)
        if i == 'S1' and not 'S1' in done_l:
            print("S1: Control Condition")
            simpleControl(p_id, rec, mic)
        elif i == 'S2' and not 'S2' in done_l:
            print("S2: Descriptive Condition")
            simpleDescriptive(p_id, rec, mic)
        elif i == 'S3' and not 'S3' in done_l:
            print("S3: Comparative Condition")
            simpleComparative(p_id, rec, mic)
        elif i == 'S4' and not 'S4' in done_l:
            print("S4: Imagery Condition")
            simpleImagery(p_id, rec, mic)

    ### MULTIPLE CHOICE TASK

    print("MULTIPLE CHOICE TASK")
    if  ( len(done_l) < 5 ):
        utils.speak("Phase 2. Practice Round.")
        multiPractice(p_id, rec, mic)
    
    # Iterate over the list to execute different simple choice conditions
    for i in mcond_l:
        if i == 'M1' and not 'M1' in done_l:
            print("M1: Control Condition")
            multiControl(p_id, rec, mic)
        elif i == 'M2' and not 'M2' in done_l:
            print("M2: Descriptive Condition")
            multiDescriptive(p_id, rec, mic)
        elif i == 'M3' and not 'M3' in done_l:
            print("M3: Comparative Condition")
            multiComparative(p_id, rec, mic)
        elif i == 'M4' and not 'M4' in done_l:
            print("M4: Imagery Condition")
            multiImagery(p_id, rec, mic)

try:
    main()
except KeyboardInterrupt:
    print("Exception. Exit.")
