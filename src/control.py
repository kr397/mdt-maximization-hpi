import speech_recognition as sr
from record import RecordAudio
import speech
import utils

def simpleControl(id, rec, mic):
    utils.log( id, "S1: Control Condition")

    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not (command == 'recommend some music'):
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
    command = utils.recognize( rec, mic )

    while not (command == 'yes' or command == 'no'):
        utils.speak( "I'm sorry, I did not catch that. Please speak again.")
        command = utils.recognize( rec, mic )

    utils.log(id, "Continue?: " + command )
    if command == 'yes':
        print('Yes')
        utils.play( 'music-files/1_Simple_04_Love\ Me.mp3', 30, 60 )

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
    utils.log(id, "Satisfaction: " + sat)

    # End instructions
    text = 'Thank you for the feedback. Please fill out the survey on the laptop, and \
            say you are ready when you want to move to the next part.'
    utils.speak( text )
    
    command = utils.recognize( rec, mic )
    while not ("ready" in command):
        if (not command == ""):
            utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)

def multiControl(id, rec, mic):
    utils.log(id, "M1: Control Condition")

    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not (command == 'recommend some music'):
        utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)
    
    # Recommend music, give choices
    text = "Here are 3 music recommendations for you from Spotify."
    utils.speak( text )
    text = "Which music do you wish to listen to? 1, 2, or 3?"
    utils.speak( text )

    choice = utils.recognize( rec, mic )
    while choice not in ['1', '2', '3']:
        utils.speak("I'm sorry, I did not catch that. Please speak again.")
        choice = utils.recognize( rec, mic )

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
    command = utils.recognize( rec, mic )

    while not (command == 'yes' or command == 'no'):
        utils.speak( "I'm sorry, I did not catch that. Please speak again.")
        command = utils.recognize( rec, mic )

    utils.log(id, "Continue?: " + command)
    if command == 'yes':
        print('Yes')
        if choice == '1':
            utils.play( 'music-files/2_Multiple_04_01_Wait\ There.mp3', 30, 60 )
        elif choice == '2':
            utils.play( 'music-files/2_Multiple_04_02_Indigo.mp3', 30, 30 )
        elif choice == '3':
            utils.play( 'music-files/2_Multiple_04_03_Yellow\ Room.mp3', 30, 30 )

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
    utils.log(id, "Satisfaction: " + sat)

    # End instructions
    text = 'Thank you for the feedback. Please fill out the survey on the laptop, and \
            say you are ready when you want to move to the next part.'
    utils.speak( text )

    command = utils.recognize( rec, mic )
    while not ("ready" in command):

        utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)
