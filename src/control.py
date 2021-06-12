import speech_recognition as sr
import time
from record import RecordAudio
import speech
import utils

def simpleControl(id, rec, mic):
    log = {'participant-id':id, 'simple-choice': 'Control Condition'}
    utils.log( id, "S1: Control Condition")

    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not ('recommend' in command):
        if ('repeat' in command):
            utils.speak("Welcome. Please give a command.")
        elif (not command == ''):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)
    
    # Recommend music
    text = "Here is piano music from Spotify."
    utils.speak( text )
    utils.play( 'music-files/1_Simple_04_Love\ Me.mp3', 0, 30 )
    utils.log(id, "Playing: Love Me")

    # Check
    text = 'Do you want to continue this music?'
    utils.speak( text )
    start_time = time.time()
    command = utils.recognize( rec, mic )

    while not ('yes' in command or 'no' in command):
        if ('repeat' in command):
            utils.speak("Do you want to continue this music?")
        elif (not command == ''):
            utils.speak( "I'm sorry, I did not catch that. Please speak again.")
        command = utils.recognize( rec, mic )

    continued_time = time.time() - start_time
    utils.log(id, "Continue?: " + command )
    log['continued'] = command
    log['continued-time'] = str(continued_time)
    if command == 'yes':
        print('Yes')
        utils.play( 'music-files/1_Simple_04_Love\ Me.mp3', 30, 60 )
        
    # Satisfaction
    text = 'How much were you satisfied with the music recommendation? Please rate \
        your overall satisfaction with your experience on this music \
        recommendation. From one, completely dissatisfied. To seven, completely satisfied.'
    utils.speak( text )
    start_time = time.time()
    sat = utils.recognize( rec, mic )
    
    while sat not in ['1', '2', '3', '4', '5', '6', '7']:
        if ('repeat' in sat): 
            utils.speak( text )
        elif (not sat == ''):
            utils.speak("I'm sorry, I did not catch that. Please speak again.")
        sat = utils.recognize( rec, mic )

    sat_time = time.time() - start_time
    print('Satisfaction: ' + sat)
    utils.log(id, "Satisfaction: " + sat)
    log['satisfaction'] = sat
    log['satisfaction-time'] = str(sat_time)

    # End instructions
    text = 'Thank you for the feedback. Please fill out the survey on the laptop by clicking the next button, and \
            say you are ready when you want to move to the next part.'
    utils.speak( text )
    
    command = utils.recognize( rec, mic )
    while not ("ready" in command):
        if (not command == ""):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)

    # Add log to CSV
    utils.csvSimple(log)

def multiControl(id, rec, mic):
    utils.log(id, "M1: Control Condition")
    log = {'participant-id':id, 'multiple-choice': 'Control Condition'}

    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not ('recommend' in command):
        if ('repeat' in command):
            utils.speak("Welcome. Please give a command.")
        elif (not command == ''):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)
    
    # Recommend music, give choices
    text = "Here are 3 music recommendations for you from Spotify. Which music do you wish to listen to? 1, 2, or 3?"
    utils.speak( text )
    start_time = time.time()

    choice = utils.recognize( rec, mic )
    while choice not in ['1', '2', '3']:
        if ('repeat' in choice):
            utils.speak(text)
        elif (not choice == ''):
            utils.speak("I'm sorry, I did not catch that. Please speak again.")
        choice = utils.recognize( rec, mic )

    choice_time = time.time() - start_time
    log['choice'] = choice
    log['choice-time'] = str(choice_time)
    utils.log(id, "Choice: " + choice)
    if choice == '1':
        print("Choice 1: Indigo by Yiruma")
        utils.speak("Okay, playing Indigo by Yiruma")
        utils.play( 'music-files/2_Multiple_04_01_Wait\ There.mp3', 0, 30 )
    elif choice == '2':
        print("Choice 2: Wait There by Yiruma")
        utils.speak("Okay, playing Wait There by Yiruma")
        utils.play( 'music-files/2_Multiple_04_02_Indigo.mp3', 0, 30 )
    elif choice == '3':
        print("Choice 3: Yellow Room by Yiruma")
        utils.speak("Okay, playing Yellow Room by Yiruma")
        utils.play( 'music-files/2_Multiple_04_03_Yellow\ Room.mp3', 0, 30 )

    # Check
    text = 'Do you want to continue this music?'
    utils.speak( text )
    start_time = time.time()

    command = utils.recognize( rec, mic )
    while not ('yes' in command or 'no' in command):
        if ('repeat' in command):
            utils.speak("Do you want to continue this music?")
        elif (not command == ''):
            utils.speak( "I'm sorry, I did not catch that. Please speak again.")
        command = utils.recognize( rec, mic )

    continued_time = time.time() - start_time
    log['continued'] = command
    log['continued-time'] = str(continued_time)
    utils.log(id, "Continue?: " + command)
    if command == 'yes':
        print('Yes')
        if choice == '1':
            utils.play( 'music-files/2_Multiple_04_01_Wait\ There.mp3', 30, 60 )
        elif choice == '2':
            utils.play( 'music-files/2_Multiple_04_02_Indigo.mp3', 30, 60 )
        elif choice == '3':
            utils.play( 'music-files/2_Multiple_04_03_Yellow\ Room.mp3', 30, 60 )

    # Satisfaction
    text = 'How much were you satisfied with the music recommendation? Please rate \
        your overall satisfaction with your experience on this music \
        recommendation. From one, completely dissatisfied. To seven, completely satisfied.'
    utils.speak( text )
    start_time = time.time()
    sat = utils.recognize( rec, mic )
    
    while sat not in ['1', '2', '3', '4', '5', '6', '7']:
        if ('repeat' in sat): 
            utils.speak( text )
        elif (not sat == ''):
            utils.speak("I'm sorry, I did not catch that. Please speak again.")
        sat = utils.recognize( rec, mic )
    print('Satisfaction: ' + sat)
    utils.log(id, "Satisfaction: " + sat)
    sat_time = time.time() - start_time
    log['satisfaction'] = sat
    log['satisfaction-time'] = str(sat_time)

    # End instructions
    text = 'Thank you for the feedback. Please fill out the survey on the laptop by clicking the next button, and \
            say you are ready when you want to move to the next part.'
    utils.speak( text )

    command = utils.recognize( rec, mic )
    while not ("ready" in command):
        if (not command == ""):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)

    # Add log to CSV
    utils.csvMulti(log)
