import speech_recognition as sr
from record import RecordAudio
import speech
import utils

def simplePractice(rec, mic):
    # Recommend music
    text = "Here is piano music from Spotify."
    utils.speak( text )
    utils.play( 'music-files/1_Simple_00_Practice_Room\ With\ A\ View.mp3', 0, 30 )

    # Check
    text = 'Do you want to continue this music?'
    utils.speak( text )
    command = utils.recognize( rec, mic )

    while not (command == 'yes' or command == 'no'):
        utils.speak( "I'm sorry, I did not catch that. Please speak again.")
        command = utils.recognize( rec, mic )

    if command == 'yes':
        print('Yes')
        utils.play( 'music-files/1_Simple_00_Practice_Room\ With\ A\ View.mp3', 0, 30 )

def multiPractice(rec, mic):
    # Recommend music, give choices
    text = "Here are 3 music recommendations for you from Spotify."
    utils.speak( text )
    text = "Which music do you wish to listen to? 1, 2, or 3?"
    utils.speak( text )

    choice = utils.recognize( rec, mic )
    while choice not in ['1', '2', '3']:
        utils.speak("I'm sorry, I did not catch that. Please speak again.")
        choice = utils.recognize( rec, mic )

    if choice == '1':
        print("Choice 1: Indigo by Yiruma")
        utils.speak("Okay, playing 1.")
        utils.play( 'music-files/2_Multiple_04_01_Wait\ There.mp3', 0, 30 )
    elif choice == '2':
        print("Choice 2: Wait There by Yiruma")
        utils.speak("Okay, playing 2.")
        utils.play( 'music-files/2_Multiple_04_02_Indigo.mp3', 0, 30 )
    elif choice == '3':
        print("Choice 3: Yellow Room by Yiruma")
        utils.speak("Okay, playing 3.")
        utils.play( 'music-files/2_Multiple_04_03_Yellow\ Room.mp3', 0, 30 )

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
            utils.play( 'music-files/2_Multiple_04_01_Wait\ There.mp3', 30, 60 )
        elif choice == '2':
            utils.play( 'music-files/2_Multiple_04_02_Indigo.mp3', 30, 30 )
        elif choice == '3':
            utils.play( 'music-files/2_Multiple_04_03_Yellow\ Room.mp3', 30, 30 )
