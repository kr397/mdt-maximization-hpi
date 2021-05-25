import speech_recognition as sr
from record import RecordAudio
import speech
import utils

def simpleComparative(rec, mic):
    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not (command == 'recommend some music'):
        utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)
    
    # Recommend music
    text = "Here is the piano music played most in your location. The number of \
            today's streams is 7,996,867."
    utils.speak( text )
    utils.play( 'music-files/1_Simple_02_Kiss\ the\ Rain.mp3', 0, 30 )

    # Check
    text = 'Do you want to continue this music?'
    utils.speak( text )
    command = utils.recognize( rec, mic )
    
    while not (command == 'yes' or command == 'no'):
        utils.speak( "I'm sorry, I did not catch that.")
        command = utils.recognize( rec, mic )

    if command == 'yes':
        print('Yes')
        utils.play( 'music-files/1_Simple_02_Kiss\ the\ Rain.mp3', 30, 60 )

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

def multiComparative(rec, mic):
    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not (command == 'recommend some music'):
        utils.speak( "I'm sorry, I did not catch that. Please speak again." )
        command = utils.recognize( rec, mic)
    
    # Recommend music, give choices
    text = "Here are 3 music recommendations for you. The first one is the piano music played the most today in your location. The number of today's streams is 4,453,602. The second is played most by other users in your age group. The number of today's streams is 1,987,055. The last one is the piano music played the most this by other users in the US. The number of streams is 9,865,329."
    utils.speak( text )
    text = "Which music do you wish to listen to? 1, 2, or 3?"
    utils.speak( text )

    choice = utils.recognize( rec, mic )
    while choice not in ['1', '2', '3']:
        utils.speak("I'm sorry, I did not catch that. Please speak again.")
        choice = utils.recognize( rec, mic )

    if choice == '1':
        print("Choice 1: It's Your Day by Yiruma")
        utils.speak("Okay, playing 1.")
        utils.play( 'music-files/2_Multiple_02_01_Its\ Your\ Day.mp3', 0, 30 )
    elif choice == '2':
        print("Choice 2: Passing By by Yiruma")
        utils.speak("Okay, playing 2.")
        utils.play( 'music-files/2_Multiple_02_02_Passing\ By.mp3', 0, 30 )
    elif choice == '3':
        print("Choice 3: Time Forgets by Yiruma")
        utils.speak("Okay, playing 3.")
        utils.play( 'music-files/2_Multiple_02_03_Time\ Forgets.mp3', 0, 30 )

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
            utils.play( 'music-files/2_Multiple_02_01_Its\ Your\ Day.mp3', 30, 60 )
        elif choice == '2':
            utils.play( 'music-files/2_Multiple_02_02_Passing\ By.mp3', 30, 60 )
        elif choice == '3':
            utils.play( 'music-files/2_Multiple_02_03_Time\ Forgets.mp3', 30, 60 )

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
