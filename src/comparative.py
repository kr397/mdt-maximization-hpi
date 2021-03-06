import speech_recognition as sr
import time
from record import RecordAudio
import speech
import utils

def simpleComparative(id, rec, mic):
    log = [id, 'Comparative Condition']
    utils.log(id, "S3: Comparative Condition")

    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not ('recommend' in command or 'play' in command):
        if ('repeat' in command):
            utils.speak("Okay, how can I help you?")
        elif (not command == ''):
            utils.speak( "I'm sorry, please speak again." )
        command = utils.recognize( rec, mic)
    
    # Recommend music
    text = "Okay, here is the piano music played most in your location. The number of today's streams is 7 point 9 million."
    utils.speak( text )
    utils.play( 'music-files/1_Simple_02_Kiss\ the\ Rain.mp3', 0, 30 )
    utils.log(id, "Playing: Kiss The Rain")

    # Check
    text = 'Do you want to continue this music?'
    utils.speak( text )
    start_time = time.time()
    command = utils.recognize( rec, mic )
    
    while not ('yes' in command or 'no' in command):
        if ('repeat' in command):
            utils.speak("Do you want to continue this music?")
        elif (not command == ''):
            utils.speak( "I'm sorry, please speak again.")
        command = utils.recognize( rec, mic )

    continued_time = time.time() - start_time
    utils.log(id, "Continue?: " + command )
    log.append(command)
    log.append(str(continued_time))

    if command == 'yes':
        print('Yes')
        utils.play( 'music-files/1_Simple_02_Kiss\ the\ Rain.mp3', 30, 60 )

    # Satisfaction
    text = 'Please rate your overall satisfaction with your experience on this music recommendation. From one, completely dissatisfied. To seven, completely satisfied.' 
    utils.speak( text )
    start_time = time.time()
    sat = utils.recognize( rec, mic )
    
    while sat not in ['1', '2', '3', '4', '5', '6', '7']:
        if ('repeat' in sat): 
            text = 'Please rate your overall satisfaction with your experience on this music recommendation. From one, completely dissatisfied. To seven, completely satisfied.' 
            utils.speak( text )
        elif (not sat == ''):
            utils.speak("I'm sorry, please speak again.")
        sat = utils.recognize( rec, mic )
    sat_time = time.time() - start_time
    print('Satisfaction: ' + sat)
    utils.log(id, "Satisfaction: " + sat)
    log.append(sat)
    log.append(str(sat_time))

    # End instructions
    text = 'Thank you for the feedback. Please fill out the survey on the computer by clicking the next button, and say you are ready when you want to move to the next part.'
    utils.speak( text )

    time.sleep(180)
    
    command = utils.recognize( rec, mic )
    while not ("ready" in command):
        if ("repeat" in command):
            text = 'Thank you for the feedback. Please fill out the survey on the computer by clicking the next button, and say you are ready when you want to move to the next part.'
            utils.speak( text )
        elif (not command == ""):
            utils.speak( "I'm sorry, please speak again." )
        command = utils.recognize( rec, mic)
    
    # Add log to CSV
    utils.csvSimple(log)

def multiComparative(id, rec, mic):
    utils.log(id, "M3: Comparative Condition")
    log = [id, 'Comparative Condition']

    # Introduction
    text = "Okay, how can I help you?"
    utils.speak( text )

    # Wait for the recommend command
    command = utils.recognize( rec, mic )
    while not ('recommend' in command or 'play' in command):
        if ('repeat' in command):
            utils.speak("Okay, how can I help you?")
        elif (not command == ''):
            utils.speak( "I'm sorry, please speak again." )
        command = utils.recognize( rec, mic)
    
    # Recommend music, give choices
    text = "Okay, here are 3 music recommendations for you. The first one is the piano music played the most today in your location. The number of today's streams is 4 point 4 million."
    utils.speak( text )
    text = "The second is played most by other users in your age group. The number of today's streams is 1 point 9 million."
    utils.speak( text )
    text = "The last one is the piano music played the most by other users in the US. The number of streams is 9 point 2 million. Which music do you wish to listen to? 1, 2, or 3?"
    utils.speak( text )
    start_time = time.time()

    choice = utils.recognize( rec, mic )
    while choice not in ['1', '2', '3']:
        if ('repeat' in choice):
            text = "Okay, here are 3 music recommendations for you. The first one is the piano music played the most today in your location. The number of today's streams is 4,453,602."
            utils.speak( text )
            text = "The second is played most by other users in your age group. The number of today's streams is 1,987,055."
            utils.speak( text )
            text = "The last one is the piano music played the most by other users in the US. The number of streams is 9,865,329. Which music do you wish to listen to? 1, 2, or 3?"
            utils.speak( text )
        elif (not choice == ''):
            utils.speak("I'm sorry, please speak again.")
        choice = utils.recognize( rec, mic )

    choice_time = time.time() - start_time
    log.append(choice)
    log.append(str(choice_time))

    utils.log(id, "Choice: " + choice)
    if choice == '1':
        print("Choice 1: It's Your Day by Yiruma")
        utils.speak("Okay, playing music titled It's Your Day by Yiruma.")
        utils.play( 'music-files/2_Multiple_02_01_Its\ Your\ Day.mp3', 0, 30 )
    elif choice == '2':
        print("Choice 2: Passing By by Yiruma")
        utils.speak("Okay, playing music titled Passing By by Yiruma.")
        utils.play( 'music-files/2_Multiple_02_02_Passing\ By.mp3', 0, 30 )
    elif choice == '3':
        print("Choice 3: Time Forgets by Yiruma")
        utils.speak("Okay, playing music titled Time Forgets by Yiruma.")
        utils.play( 'music-files/2_Multiple_02_03_Time\ Forgets.mp3', 0, 30 )

    # Check
    text = 'Do you want to continue this music?'
    utils.speak( text )
    start_time = time.time()

    command = utils.recognize( rec, mic )
    while not ('yes' in command or 'no' in command):
        if ('repeat' in command):
            utils.speak("Do you want to continue this music?")
        elif (not command == ''):
            utils.speak( "I'm sorry, please speak again.")
        command = utils.recognize( rec, mic )

    continued_time = time.time() - start_time
    log.append(command)
    log.append(str(continued_time))

    utils.log(id, "Continue?: " + command)
    if command == 'yes':
        print('Yes')
        if choice == '1':
            utils.play( 'music-files/2_Multiple_02_01_Its\ Your\ Day.mp3', 30, 60 )
        elif choice == '2':
            utils.play( 'music-files/2_Multiple_02_02_Passing\ By.mp3', 30, 60 )
        elif choice == '3':
            utils.play( 'music-files/2_Multiple_02_03_Time\ Forgets.mp3', 30, 60 )

    # Satisfaction
    text = 'Please rate your overall satisfaction with your experience on this music recommendation. From one, completely dissatisfied. To seven, completely satisfied.' 
    utils.speak( text )
    start_time = time.time()
    sat = utils.recognize( rec, mic )
    
    while sat not in ['1', '2', '3', '4', '5', '6', '7']:
        if ('repeat' in sat): 
                text = 'Please rate your overall satisfaction with your experience on this music recommendation. From one, completely dissatisfied. To seven, completely satisfied.' 
                utils.speak( text )
        elif (not sat == ''):
            utils.speak("I'm sorry, please speak again.")
        sat = utils.recognize( rec, mic )
    print('Satisfaction: ' + sat)
    sat_time = time.time() - start_time
    utils.log(id, "Satisfaction: " + sat)
    log.append(sat)
    log.append(str(sat_time))

    # End instructions
    text = 'Thank you for the feedback. Please fill out the survey on the computer by clicking the next button, and say you are ready when you want to move to the next part.'
    utils.speak( text )

    time.sleep(180)

    command = utils.recognize( rec, mic )
    while not ("ready" in command):
        if ("repeat" in command):
            text = 'Thank you for the feedback. Please fill out the survey on the computer by clicking the next button, and say you are ready when you want to move to the next part.'
            utils.speak( text )
        elif (not command == ""):
            utils.speak( "I'm sorry, please speak again." )
        command = utils.recognize( rec, mic)
    
    # Add log to CSV
    utils.csvMulti(log)
