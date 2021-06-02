import speech_recognition as sr
from record import RecordAudio
import speech
import utils

def simpleImagery(id, rec, mic):
    log = {'simple-choice-' + str(num): 'Imagery Condition'}
    utils.log(id, "S4: Imagery Condition")

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
    text = "Here is comfortable and cozy piano music."
    utils.speak( text )
    utils.play( 'music-files/1_Simple_03_May\ Be.mp3', 0, 30 )
    utils.log(id, "Playing: May Be")

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
        utils.play( 'music-files/1_Simple_03_May\ Be.mp3', 0, 30 )

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

def multiImagery(id, rec, mic):
    utils.log(id, "M4: Imagery Condition")

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
    text = "Here are 3 music recommendations for you. The first one is front porch piano music. The second is cozy coffee piano music. And the last one is sweater weather music content. Which music do you wish to listen to? 1, 2, or 3?"
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
        print("Choice 1: Hope by Yiruma")
        utils.speak("Okay, playing 1.")
        utils.play( 'music-files/2_Multiple_03_01_Hope.mp3', 0, 30 )
    elif choice == '2':
        print("Choice 2: Painted by Yiruma")
        utils.speak("Okay, playing 2.")
        utils.play( 'music-files/2_Multiple_03_02_Painted.mp3', 0, 30 )
    elif choice == '3':
        print("Choice 3: Sky by Yiruma")
        utils.speak("Okay, playing 3.")
        utils.play( 'music-files/2_Multiple_03_03_Sky.mp3', 0, 30 )

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
            utils.play( 'music-files/2_Multiple_03_01_Hope.mp3', 30, 60 )
        elif choice == '2':
            utils.play( 'music-files/2_Multiple_03_02_Painted.mp3', 30, 30 )
        elif choice == '3':
            utils.play( 'music-files/2_Multiple_03_03_Sky.mp3', 30, 30 )
    
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
    text = 'Thank you for the feedback. Please fill out the survey on the laptop clicking the next button, and \
            say you are ready when you want to move to the next part.'
    utils.speak( text )

    command = utils.recognize( rec, mic )
    while not ("ready" in command):
        if (not command == ""):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)