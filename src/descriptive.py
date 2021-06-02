import speech_recognition as sr
from record import RecordAudio
import speech
import utils

def simpleDescriptive(id, rec, mic, num):
    log = {'simple-choice-' + str(num): 'Descriptive Condition'}
    utils.log(id, "S1: Descriptive Condition")

    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not ('recommend' in command):
        if ('repeat' in command):
            utils.speak("Welcome. Please give a command.")
        else:
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)
        
    # Recommend music
    text = "Here is the music titled River Flows In You by Yiruma"
    utils.speak( text )
    utils.play( 'music-files/1_Simple_01_River\ Flows\ In\ You.mp3', 0, 30 )
    utils.log(id, "Playing: River Flows In You")

    # Check
    text = 'Do you want to continue this music?'
    utils.speak( text )
    start_time = time.time()
    command = utils.recognize( rec, mic )

    while not ('yes' in command or 'no' in command):
        if ('repeat' in command):
            utils.speak("Do you want to continue this music?")
        else:
            utils.speak( "I'm sorry, I did not catch that. Please speak again.")
        command = utils.recognize( rec, mic )

    continued_time = time.time() - start_time
    utils.log(id, "Continue?: " + command )
    log['continued-' + str(num)] = command
    log['continued-time' + str(num)] = str(continued_time)
    if command == 'yes':
        print('Yes')
        utils.play( 'music-files/1_Simple_01_River\ Flows\ In\ You.mp3', 30, 60 )

    # Satisfaction
    text = 'How much were you satisfied with the music? Please rate \
        your overall satisfaction with your experience on this music \
        recommendation. From one, completely dissatisfied. To seven, completely satisfied.'
    utils.speak( text )
    start_time = time.time()
    sat = utils.recognize( rec, mic )
    
    while sat not in ['1', '2', '3', '4', '5', '6', '7']:
        if ('repeat' in sat): 
            utils.speak( text )
        else:
            utils.speak("I'm sorry, I did not catch that. Please speak again.")
        sat = utils.recognize( rec, mic )
    sat_time = time.time() - start_time
    print('Satisfaction: ' + sat)
    utils.log(id, "Satisfaction: " + sat)
    log['satisfaction' + str(num)] = sat
    log['satisfaction-time' + str(num)] = sat_time

    # End instructions
    text = 'Thank you for the feedback. Please fill out the survey on the laptop by clicking the next button, and \
            say you are ready when you want to move to the next part.'
    utils.speak( text )
    
    command = utils.recognize( rec, mic )
    while not ("ready" in command):
        if (not command == ""):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)

    return log


def multiDescriptive(id, rec, mic):
    utils.log(id, "M2: Descriptive Condition")
    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not ('recommend' in command):
        if ('repeat' in command):
            utils.speak("Welcome. Please give a command.")
        else:
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)

    # Recommend music, give choices
    text = "Here are 3 music recommendations for you. The first one is piano music titled When the Love Falls. The second is called Because I Love you. And the last one is music titled Fairy Tale. Which music do you wish to listen to? 1, 2, or 3?"
    utils.speak( text )

    choice = utils.recognize( rec, mic )
    while choice not in ['1', '2', '3']:
        if ('repeat' in choice):
            utils.speak(text)
        else:
            utils.speak("I'm sorry, I did not catch that. Please speak again.")
        choice = utils.recognize( rec, mic )

    utils.log(id, "Choice: " + choice)
    if choice == '1':
        print("Choice 1: When The Love Falls by Yiruma")
        utils.speak("Okay, playing 1.")
        utils.play( 'music-files/2_Multiple_01_01_When\ The\ Love\ Falls.mp3', 0, 30 )
    elif choice == '2':
        print("Choice 2: Because I Love You by Yiruma")
        utils.speak("Okay, playing 2.")
        utils.play( 'music-files/2_Multiple_01_02_Because\ I\ Love\ You.mp3', 0, 30 )
    elif choice == '3':
        print("Choice 3: Fairy Tale by Yiruma")
        utils.speak("Okay, playing 3.")
        utils.play( 'music-files/2_Multiple_01_02_Fairy\ Tale.mp3', 0, 30 )

    # Check
    text = 'Do you want to continue this music?'
    utils.speak( text )
    command = utils.recognize( rec, mic )

    while not ('yes' in command or 'no' in command):
        if ('repeat' in command):
            utils.speak("Do you want to continue this music?")
        else:
            utils.speak( "I'm sorry, I did not catch that. Please speak again.")
        command = utils.recognize( rec, mic )

    utils.log(id, "Continue?: " + command)
    if command == 'yes':
        print('Yes')
        if choice == '1':
            utils.play( 'music-files/2_Multiple_01_01_When\ The\ Love\ Falls.mp3', 30, 60 )
        elif choice == '2':
            utils.play( 'music-files/2_Multiple_01_02_Because\ I\ Love\ You.mp3', 30, 60 )
        elif choice == '3':
            utils.play( 'music-files/2_Multiple_01_02_Fairy\ Tale.mp3', 30, 60 )

    # Satisfaction
    text = 'How much were you satisfied with the music? Please rate \
        your overall satisfaction with your experience on this music \
        recommendation. From one, completely dissatisfied. To seven, completely satisfied.'
    utils.speak( text )
    sat = utils.recognize( rec, mic )
    
    while sat not in ['1', '2', '3', '4', '5', '6', '7']:
        if ('repeat' in sat): 
            utils.speak( text )
        else:
            utils.speak("I'm sorry, I did not catch that. Please speak again.")
        sat = utils.recognize( rec, mic )
    print('Satisfaction: ' + sat)
    utils.log(id, "Satisfaction: " + sat)

    # End instructions
    text = 'Thank you for the feedback. Please fill out the survey on the laptop by clicking the next button, and \
            say you are ready when you want to move to the next part.'
    utils.speak( text )

    command = utils.recognize( rec, mic )
    while not ("ready" in command):
        if (not command == ""):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)