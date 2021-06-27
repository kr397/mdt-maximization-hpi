import speech_recognition as sr
import time
from record import RecordAudio
import speech
import utils

def simpleDescriptive(id, rec, mic):
    log = [id, 'Descriptive Condition']
    # log = {'participant-id':id, 'simple-choice':'Descriptive Condition'}
    utils.log(id, "S1: Descriptive Condition")

    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not ('recommend' in command):
        if ('repeat' in command):
            utils.speak("Okay, how can I help you?")
        elif (not command == ''):
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
        elif (not command == ''):
            utils.speak( "I'm sorry, I did not catch that. Please speak again.")
        command = utils.recognize( rec, mic )

    continued_time = time.time() - start_time
    utils.log(id, "Continue?: " + command )
    log.append(command)
    log.append(str(continued_time))
    # log['continued'] = command
    # log['continued-time'] = str(continued_time)
    if command == 'yes':
        print('Yes')
        utils.play( 'music-files/1_Simple_01_River\ Flows\ In\ You.mp3', 30, 60 )

    # Satisfaction
    text = 'How much were you satisfied with the music recommendation? Please rate your overall satisfaction with your experience on this music recommendation.' 
    utils.speak( text )
    utils.speak('From one, completely dissatisfied. To seven completely satisfied.')
    start_time = time.time()
    sat = utils.recognize( rec, mic )
    
    while sat not in ['1', '2', '3', '4', '5', '6', '7']:
        if ('repeat' in sat): 
            text = 'How much were you satisfied with the music recommendation? Please rate your overall satisfaction with your experience on this music recommendation.' 
            utils.speak( text )
            utils.speak('From one, completely dissatisfied. To seven completely satisfied.')
        elif (not sat == ''):
            utils.speak("I'm sorry, I did not catch that. Please speak again.")
        sat = utils.recognize( rec, mic )
    sat_time = time.time() - start_time
    print('Satisfaction: ' + sat)
    utils.log(id, "Satisfaction: " + sat)
    log.append(sat)
    log.append(str(sat_time))
    # log['satisfaction'] = sat
    # log['satisfaction-time'] = str(sat_time)

    # End instructions
    text = 'Thank you for the feedback. Please fill out the survey on the laptop by clicking the next button, and \
            say you are ready when you want to move to the next part.'
    utils.speak( text )
    
    command = utils.recognize( rec, mic )
    while not ("ready" in command):
        if ("repeat" in command):
            text = 'Thank you for the feedback. Please fill out the survey on the laptop by clicking the next button, and \
say you are ready when you want to move to the next part.'
            utils.speak( text )
        elif (not command == ""):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)

    # Add log to CSV
    utils.csvSimple(log)


def multiDescriptive(id, rec, mic):
    utils.log(id, "M2: Descriptive Condition")
    log = [id, 'Descriptive Condition']
    # log = {'participant-id':id, 'multiple-choice': 'Descriptive Condition'}

    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not ('recommend' in command):
        if ('repeat' in command):
            utils.speak("Okay, how can I help you?")
        elif (not command == ''):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)

    # Recommend music, give choices
    text = "Here are 3 music recommendations for you. The first one is piano music titled When the Love Falls. \
        The second is called Because I Love you. And the last one is music titled Fairy Tale."
    utils.speak( text )
    utils.speak("Which music do you wish to listen to? 1, 2, or 3?")
    start_time = time.time()

    choice = utils.recognize( rec, mic )
    while choice not in ['1', '2', '3']:
        if ('repeat' in choice):
            text = "Here are 3 music recommendations for you. The first one is piano music titled When the Love Falls. \
The second is called Because I Love you. And the last one is music titled Fairy Tale."
            utils.speak( text )
            utils.speak("Which music do you wish to listen to? 1, 2, or 3?")
        elif (not choice == ''):
            utils.speak("I'm sorry, I did not catch that. Please speak again.")
        choice = utils.recognize( rec, mic )

    choice_time = time.time() - start_time
    log.append(choice)
    log.append(str(choice_time))
    # log['choice'] = choice
    # log['choice-time'] = str(choice_time)
    utils.log(id, "Choice: " + choice)
    if choice == '1':
        print("Choice 1: When The Love Falls by Yiruma")
        utils.speak("Okay, playing music titled When The Love Falls by Yiruma.")
        utils.play( 'music-files/2_Multiple_01_01_When\ The\ Love\ Falls.mp3', 0, 30 )
    elif choice == '2':
        print("Choice 2: Because I Love You by Yiruma")
        utils.speak("Okay, playing music titled Because I Love You by Yiruma.")
        utils.play( 'music-files/2_Multiple_01_02_Because\ I\ Love\ You.mp3', 0, 30 )
    elif choice == '3':
        print("Choice 3: Fairy Tale by Yiruma")
        utils.speak("Okay, playing music titled Fairy Tale by Yiruma.")
        utils.play( 'music-files/2_Multiple_01_02_Fairy\ Tale.mp3', 0, 30 )

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
    log.append(command)
    log.append(str(continued_time))
    # log['continued'] = command
    # log['continued-time'] = str(continued_time)
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
    text = 'How much were you satisfied with the music recommendation? Please rate your overall satisfaction with your experience on this music recommendation.' 
    utils.speak( text )
    utils.speak('From one, completely dissatisfied. To seven completely satisfied.')
    start_time = time.time()

    sat = utils.recognize( rec, mic )
    while sat not in ['1', '2', '3', '4', '5', '6', '7']:
        if ('repeat' in sat): 
            text = 'How much were you satisfied with the music recommendation? Please rate your overall satisfaction with your experience on this music recommendation.' 
            utils.speak( text )
            utils.speak('From one, completely dissatisfied. To seven completely satisfied.')
        elif (not sat == ''):
            utils.speak("I'm sorry, I did not catch that. Please speak again.")
        sat = utils.recognize( rec, mic )
    print('Satisfaction: ' + sat)
    sat_time = time.time() - start_time
    utils.log(id, "Satisfaction: " + sat)
    log.append(sat)
    log.append(str(sat_time))
    # log['satisfaction'] = sat
    # log['satisfaction-time'] = str(sat_time)

    # End instructions
    text = 'Thank you for the feedback. Please fill out the survey on the laptop by clicking the next button, and \
            say you are ready when you want to move to the next part.'
    utils.speak( text )

    command = utils.recognize( rec, mic )
    while not ("ready" in command):
        if ("repeat" in command):
            text = 'Thank you for the feedback. Please fill out the survey on the laptop by clicking the next button, and \
say you are ready when you want to move to the next part.'
            utils.speak( text )
        elif (not command == ""):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)

    # Add log to CSV
    utils.csvMulti(log)