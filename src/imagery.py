import speech_recognition as sr
from record import RecordAudio
import speech
import utils

def simpleImagery(rec, mic):
    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not (command == 'recommend some music'):
        utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)
    
    # Recommend music
    text = "Here is comfortable and cozy piano music."
    utils.speak( text )
    utils.play( 'music-files/1_Simple_03_May\ Be.mp3', 0, 30 )

    # Check
    text = 'Do you want to continue this music?'
    utils.speak( text )
    command = utils.recognize( rec, mic )

    while not (command == 'yes' or command == 'no'):
        utils.speak( "I'm sorry, I did not catch that.")
        command = utils.recognize( rec, mic )

    if command == 'yes':
        print('Yes')
        utils.play( 'music-files/1_Simple_03_May\ Be.mp3', 0, 30 )

    # Satisfaction
    text = 'How much were you satisfied with the music? Please rate \
        your overall satisfaction with your experience on this music \
        recommendation. From one, completely dissatisfied. To seven, completely satisfied.'
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
    
    command = utils.recognize( rec, mic )
    while not ("ready" in command):
        if (not command == ""):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)

def multiImagery(rec, mic):
    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not (command == 'recommend some music'):
        utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)

    # Recommend music, give choices
    text = "Here are 3 music recommendations for you. The first one is front porch piano music. The second is cozy coffee piano music. And the last one is sweater weather music content."
    utils.speak( text )
    text = "Which music do you wish to listen to? 1, 2, or 3?"
    utils.speak( text )

    choice = utils.recognize( rec, mic )
    while choice not in ['1', '2', '3']:
        utils.speak("I'm sorry, I did not catch that. Please speak again.")
        choice = utils.recognize( rec, mic )

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

    while not (command == 'yes' or command == 'no'):
        utils.speak( "I'm sorry, I did not catch that. Please speak again.")
        command = utils.recognize( rec, mic )

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
        utils.speak("I'm sorry, I did not catch that. Please speak again.")
        sat = utils.recognize( rec, mic )
    print('Satisfaction: ' + sat)

    # End instructions
    text = 'Thank you for the feedback. Please fill out the survey on the laptop, and \
            say you are ready when you want to move to the next part.'
    utils.speak( text )

    command = utils.recognize( rec, mic )
    while not ("ready" in command):

        utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)
