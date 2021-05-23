import speech_recognition as sr
from record import RecordAudio
import speech
import utils

def simpleDescriptive(rec, mic):
    # Recommend music
    text = "Here is the music titled River Flows In You by Yiruma"
    utils.speak( text )
    utils.play( 'music-files/1_Simple_01_River\ Flows\ In\ You.mp3', 0, 30 )

    # Check
    text = 'Do you want to continue this music?'
    utils.speak( text )
    command = utils.recognize( rec, mic )

    while not (command == 'yes' or command == 'no'):
        utils.speak( "I'm sorry, I did not catch that.")
        command = utils.recognize( rec, mic )

    if command == 'yes':
        print('Yes')
        utils.play( 'music-files/1_Simple_01_River\ Flows\ In\ You.mp3', 30, 60 )

def multiDescriptive(rec, mic):
    # Recommend music, give choices
    text = "Here are 3 music recommendations for you. The first one is piano music titled When the Love Falls. The second is Because I Love you. And the last one is music titled Fairy Tale."
    utils.speak( text )
    text = "Which music do you wish to listen to? 1, 2, or 3?"
    utils.speak( text )

    choice = utils.recognize( rec, mic )
    while choice not in ['1', '2', '3']:
        utils.speak("I'm sorry, I did not catch that. Please speak again.")
        choice = utils.recognize( rec, mic )

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

    while not (command == 'yes' or command == 'no'):
        utils.speak( "I'm sorry, I did not catch that. Please speak again.")
        command = utils.recognize( rec, mic )

    if command == 'yes':
        print('Yes')
        if choice == '1':
            utils.play( 'music-files/2_Multiple_01_01_When\ The\ Love\ Falls.mp3', 30, 60 )
        elif choice == '2':
            utils.play( 'music-files/2_Multiple_01_02_Because\ I\ Love\ You.mp3', 30, 60 )
        elif choice == '3':
            utils.play( 'music-files/2_Multiple_01_02_Fairy\ Tale.mp3', 30, 60 )
