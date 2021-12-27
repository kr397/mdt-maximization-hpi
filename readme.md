#  Explainable AI Speaker in Music Recommendation Contexts
> **_Design for Personalized Conversational User Interfaces to Support User’s Daily Decision-Making Experiences_**
### Code Appendix
In recent years, the research area of Conversational User Interfaces (CUIs) has attracted considerable recognition with the advancement of Artificial Intelligence (AI) technologies. This growing area of study is expected to make significant contributions to more human-centered speech and text-based interfaces. However, existing research on CUIs has been criticized regarding a lack of guidance to improve User eXperience (UX) in a daily context. To address this challenge, this project investigates a new way of creating more personalized CUIs. We specify our research scope at the intersection between voice assistants of CUIs and music recommendation systems. We investigate inter-relationship between two core aspects of CUI interactions: CUIs’ personalized explanation types and users’ decision-making styles. These two factors are examined in an experimental study in the context of interacting with a voice-controlled music recommendation CUI. The voice assistant CUI is designed to recommend music with three personalized explanation types: descriptive type, comparative type, and imagery type. Users’ decision-making styles are also measured and categorized within two types, maximizer and satisficer, for comparison between two groups with reference to recent research within decision science. We found that users’ positive aspects of decision-making experiences increased when the CUI personalized explanation types with music recommendation according to users’ different decision-making styles. We expect these findings will serve to further research and development of more human-centered CUIs.

This repository serves as the code appendix for the project, housing the Python scripts and supporting classes used for the research experiment. The system was developed on a Raspberry Pi 3B+, running the Raspberry Pi OS. This document describes the Raspberry Pi setup, and the structure of files in the `src` directory.

#### File structure
The structure of the `src` directory is as follows. 
```
-- src
    |-- comparative.py
    |-- control.py
    |-- descriptive.py
    |-- imagery.py
    |-- main.py
    |-- practice.py
    |-- record.py
    |-- speech.py
    |-- utils.py
    |-- google-tts.sh
    |-- tts.sh
    |-- music-files
```
* The `main.py` is the primary Python script that needs to be run to execute the system. It iteratively goes over each of the experiment cases (simple choice or multiple choice, comparative, descriptive, or imagery type), with a scheduled time delay between each situation. The script also takes some optional arguments to run a partial experiment (explained later). The flow also includes some practice rounds at the beginning of each phase. The order of situations in each phase are randomized. 
* The `comparative.py`, `descriptive.py`, `imagery.py`, `control.py`, `practice.py` are similar files that contain the functions to execute the experiment cases for each situation. Each file contains one function for simple choice and one for multiple choice, which are called in the flow by `main.py`. 
* `record.py` contains a supplementary `RecordAudio` class used to record voice commands for recognition. `speech.py` contains a function for speech recognition used to convert voice commands to text. The `utils.py` file contains miscellaneous functions for generating speech, playing music, voice recognition, and logging.
* The directory `music-files` contains local copies of music files that are played by the system in each situation. 
#### Setup 
The system on the Raspberry Pi requires two sets of installations of libraries and software. 
1. The first is the Speech Recognition module, which can be setup with the following steps on the terminal.
```
> sudo apt-get install libasound-dev portaudio19-dev python3-pyaudio flac
> sudo pip3 install SpeechRecognition
```
2. In order to play audio from the Raspberry Pi, we also need to install the `mplayer` software as follows. 
```
> sudo apt-get update
> sudo apt-get install mplayer
```
#### Usage
1. In order to run the experiment, the Raspberry Pi first needs to be boot up, and connected to a USB microphone + an AUX speaker. Once set up, the following steps can be executed on the terminal from the src directory to start the system. 
```
> cd src
> python3 main.py
```
2. The terminal would prompt to enter a `Participant ID`, which is used to identify each participant. Input an ID (e.g. `p1`) and press enter. The experiment will get going, with a text log on the terminal, and audio feedback from the speaker. 
3. The system will automatically execute both phases (simple and multiple choice), with the 5 situations in each, and terminate by itself at the end. In case it needs to be interrupted, one can press `Ctrl+C` on the terminal. 

The `main.py` script accepts optional arguments of `S1`, `S2`, `S3`, `S4`, `M1`, `M2`, `M3`, and `M4`, which can be used to run a partial experiment by specifying the cases that have already executed. This method is designed to recover from an interrupted run, so that the entire experiment does not have to be repeated again. The codes `S1-S4` and `M1-M4` represent the four cases as follows: `1. Control`, `2. Descriptive`, `3. Comparative`, and `4. Imagery`. 
For example, if the experiment was interrupted after running the simple choice imagery type and descriptive type, and we need to re-run for the rest of the situations, the command would be:
```
> python3 main.py S4 S2
```
After each run, the logs are stored for reference in the `logs` folder, named according to the `Participant ID` specified in the beginning of the experiment. 
