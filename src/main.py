from comparative import simpleComparative, multiComparative
from descriptive import simpleDescriptive, multiDescriptive
from imagery import simpleImagery, multiImagery
from control import simpleControl, multiControl
import utils
from record import RecordAudio
import speech

import time
import random
import speech_recognition as sr

# Main function
def main():
    # Initialize speech recognition
    rec = sr.Recognizer()
    mic = RecordAudio()

    # Randomize between the different conditions
    l = list(range(4))
    l_random = random.sample(l, len(l))

    ## Add sample interaction with the participant
    
    ### SIMPLE CHOICE TASK

    print("SIMPLE CHOICE TASK")
    utils.speak("Welcome. Please give a command.")

    # Iterate over the list to execute different simple choice conditions
    for i in l_random:
        # Wait for the recommend command
        command = utils.recognize( rec, mic )
        while not (command == 'recommend some music'):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
            command = utils.recognize( rec, mic)

        if i is 0:
            print("Control Condition")
            simpleControl(rec, mic)
        elif i is 1:
            print("Descriptive Condition")
            simpleDescriptive(rec, mic)
        elif i is 2:
            print("Comparative Condition")
            simpleComparative(rec, mic)
        else:
            print("Imagery Condition")
            simpleImagery(rec, mic)
        
        # Satisfaction
        text = 'How much were you satisfied with the music? Please rate \
            your overall satisfaction with your experience on this music \
            recommendation from one, completely dissatisfied to seven, completely satisfied.'
        utils.speak( text )
        sat = utils.recognize( rec, mic )
        
        while sat not in ['1', '2', '3', '4', '5', '6', '7']:
            utils.speak("I'm sorry, I did not catch that. Please speak again.")
            sat = utils.recognize( rec, mic )
        print('Satisfaction: ' + sat)

        # End instructions
        text = 'Thank you for the feedback. Please fill out the survey on the laptop, and \
                say you are ready when you want to move to the next part.'
        utils.speak( text )

        time.sleep(5)

        command = utils.recognize( rec, mic )
        while not ("ready" in command):
            if (not command == ""):
                utils.speak( "I'm sorry, I did not catch that. Please speak again." )
            command = utils.recognize( rec, mic)

        # Introduction
        text = "Okay, please give a command."
        utils.speak( text )
    
    ### MULTIPLE CHOICE TASK

    print("MULTIPLE CHOICE TASK")

    # Iterate over the list to execute different simple choice conditions
    for i in l_random:
        # Wait for the recommend command
        command = utils.recognize( rec, mic )
        while not (command == 'recommend some music'):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
            command = utils.recognize( rec, mic)

        if i is 2:
            print("Control Condition")
            multiControl(rec, mic)
        elif i is 0:
            print("Descriptive Condition")
            multiDescriptive(rec, mic)
        elif i is 3:
            print("Comparative Condition")
            multiComparative(rec, mic)
        else:
            print("Imagery Condition")
            multiImagery(rec, mic)
        
        # Satisfaction
        text = 'How much were you satisfied with the music? Please rate \
            your overall satisfaction with your experience on this music \
            recommendation from one, completely dissatisfied to seven, completely satisfied.'
        utils.speak( text )
        sat = utils.recognize( rec, mic )
        
        while sat not in ['1', '2', '3', '4', '5', '6', '7']:
            utils.speak("I'm sorry, I did not catch that. Please speak again.")
            sat = utils.recognize( rec, mic )
        print('Satisfaction: ' + sat)

        if (i != l_random[-1] ): 
            # End instructions
            text = 'Thank you for the feedback. Please fill out the survey on the laptop, and \
                    say you are ready when you want to move to the next part.'
            utils.speak( text )

            time.sleep(5)

            command = utils.recognize( rec, mic )
            while not ("ready" in command):
                utils.speak( "I'm sorry, I did not catch that. Please speak again." )
                command = utils.recognize( rec, mic)

            # Introduction
            text = "Okay, please give a command."
            utils.speak( text )
        else :
            # Last condition
            text = 'Thank you for the feedback. Please fill out the survey on the laptop.'
            utils.speak( text )


try:
    main()
except KeyboardInterrupt:
    print("Exception. Exit.")
