import speech_recognition as sr
from record import RecordAudio
import speech
import utils

def simplePractice(id, rec, mic):
    utils.log(id, "S0: Practice Task")
    utils.speak("Hello, how can I help you?")

    # Practice round
    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not ('recommend' in command or 'play' in command):
        if ('repeat' in command):
            utils.speak("Hello, how can I help you?")
        elif (not command == ''):
            utils.speak( "I'm sorry, please speak again." )
        command = utils.recognize( rec, mic)

    # Recommend music
    text = "Okay, here is piano music."
    utils.speak( text )
    utils.play( 'music-files/1_Simple_00_Practice_Room\ With\ A\ View.mp3', 0, 30 )
    utils.log(id, "Playing: Room With A View")

    # Check
    text = 'Do you want to continue this music?'
    utils.speak( text )
    command = utils.recognize( rec, mic )

    while not ('yes' in command or 'no' in command):
        if ('repeat' in command):
            utils.speak("Do you want to continue this music?")
        elif (not command == ''):
            utils.speak( "I'm sorry, please speak again.")
        command = utils.recognize( rec, mic )

    utils.log(id, "Continue?: " + command)
    if command == 'yes':
        print('Yes')
        utils.play( 'music-files/1_Simple_00_Practice_Room\ With\ A\ View.mp3', 30, 60 )

    # Satisfaction
    text = 'Please rate your overall satisfaction with your experience on this music recommendation. From one, completely dissatisfied. To seven, completely satisfied.' 
    utils.speak( text )
    sat = utils.recognize( rec, mic )
    
    while sat not in ['1', '2', '3', '4', '5', '6', '7']:
        if ('repeat' in sat): 
            text = 'Please rate your overall satisfaction with your experience on this music recommendation. From one, completely dissatisfied. To seven, completely satisfied.' 
            utils.speak( text )
        elif (not sat == ''):
            utils.speak("I'm sorry, please speak again.")
        sat = utils.recognize( rec, mic )
    print('Satisfaction: ' + sat)
    utils.log(id, "Satisfaction: " + sat)

    # End instructions
    text = 'Thank you for the feedback. This is the end of the practice round. Please click the next button on the computer.'
    utils.speak( text )
    utils.speak('This is the end of the practice round.')

    command = utils.recognize( rec, mic )
    while not ("ready" in command):
        if ('repeat' in command):
            text = 'Thank you for the feedback. This is the end of the practice round. Please click the next button on the computer.'
            utils.speak( text )
        elif (not command == ""):
            utils.speak( "I'm sorry, please speak again." )
        command = utils.recognize( rec, mic)

def multiPractice(id, rec, mic):
    utils.log(id, "M0: Practice Task")
    utils.speak("Okay ,how can I help you?")

    # Practice round
    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not ('recommend' in command or 'play' in command):
        if ('repeat' in command):
            utils.speak("Okay how can I help you?")
        elif (not command == ''):
            utils.speak( "I'm sorry, please speak again." )
        command = utils.recognize( rec, mic)

    # Recommend music, give choices
    text = "Okay, here are 3 music recommendations for you. Which music do you wish to listen to? 1, 2, or 3?"
    utils.speak( text )

    choice = utils.recognize( rec, mic )
    while choice not in ['1', '2', '3']:
        if ('repeat' in choice):
            utils.speak(text)
        elif (not choice == ''):
            utils.speak("I'm sorry, please speak again.")
        choice = utils.recognize( rec, mic )

    utils.log(id, "Choice: " + choice)
    if choice == '1':
        print("Choice 1")
        utils.speak("Okay, playing music titled Scenery by Yiruma.")
        utils.play( 'music-files/2_Multiple_00_Practice_Scenery.mp3', 0, 30 )
    elif choice == '2':
        print("Choice 2")
        utils.speak("Okay, playing music titled Scenery by Yiruma.")
        utils.play( 'music-files/2_Multiple_00_Practice_Scenery.mp3', 0, 30 )
    elif choice == '3':
        print("Choice 3")
        utils.speak("Okay, playing music titled Scenery by Yiruma.")
        utils.play( 'music-files/2_Multiple_00_Practice_Scenery.mp3', 0, 30 )

    # Check
    text = 'Do you want to continue this music?'
    utils.speak( text )
    command = utils.recognize( rec, mic )

    while not ('yes' in command or 'no' in command):
        if ('repeat' in command):
            utils.speak("Do you want to continue this music?")
        elif (not command == ''):
            utils.speak( "I'm sorry, please speak again.")
        command = utils.recognize( rec, mic )

    utils.log(id, "Continue?: " + command)
    if command == 'yes':
        print('Yes')
        if choice == '1':
            utils.play( 'music-files/2_Multiple_00_Practice_Scenery.mp3', 30, 60 )
        elif choice == '2':
            utils.play( 'music-files/2_Multiple_00_Practice_Scenery.mp3', 30, 60 )
        elif choice == '3':
            utils.play( 'music-files/2_Multiple_00_Practice_Scenery.mp3', 30, 60 )

    # Satisfaction
    text = 'Please rate your overall satisfaction with your experience on this music recommendation. From one, completely dissatisfied. To seven, completely satisfied.' 
    utils.speak( text )
    sat = utils.recognize( rec, mic )
    
    while sat not in ['1', '2', '3', '4', '5', '6', '7']:
        if ('repeat' in sat): 
            text = 'Please rate your overall satisfaction with your experience on this music recommendation. From one, completely dissatisfied. To seven, completely satisfied.' 
            utils.speak( text )
        elif (not sat == ''):
            utils.speak("I'm sorry, please speak again.")
        sat = utils.recognize( rec, mic )
    print('Satisfaction: ' + sat)
    utils.log(id, "Satisfaction: " + sat)

    # End instructions
    text = 'Thank you for the feedback. This is the end of the practice round. Please click the next button on the computer.'
    utils.speak( text )
    utils.speak('This is the end of the practice round.')

    command = utils.recognize( rec, mic )
    while not ("ready" in command):
        if ("repeat" in command):
            text = 'Thank you for the feedback. This is the end of the practice round. Please click the next button on the computer.'
            utils.speak( text )
        elif (not command == ""):
            utils.speak( "I'm sorry, please speak again." )
        command = utils.recognize( rec, mic)
