# Introduction

This is a Python program that translates the speech into a user input language and plays the translated result to them.

## How Does It Work

1. The program first asks for source and target language where source is the one you're going to speak and target being the one into which you want to translate it into.

2. Then the program displays the text of what you spoke as well as the translated text.

3. Finally, it plays the audio of the translated text and ends the program afterwards.

### Details for Nerds

This is all possible because of several Python packages; `googletrans`, `speech_recognition`, `playsound`, and `gTTS`.

`speech_recognition` captures the voice almost accurately and then saves the text format of it inside a variable which we will use later on, we also use that text to print out what we spoke, that is, it prints out the text in its source langauge.

`googletrans` translates the given text from `speech_recogntion` and also stores it inside a variable. We also print out the target language output.

`gTTS` then converts the translated text into audio using Google's famous Text-to-Speech capabilities. The audio is stored inside an "audio.mp3" file which will be used later on.

`playsound` then takes that audio.mp3 file and then plays it inside the program and the program ends afterwards.

## Usage

Pre-requisites are on how to make a virtual environment in Python and on how to use the "requirements.txt" file to install the dependencies for the program.

**Make sure to use the packages inside the requirements.txt file since there are some packages with specific versions being used and won't work otherwise.**

Afterwards, just install the requirements.txt file inside a virtual environment and then run the `app.py` file.

There is no restriction to use a virtual environment, but it helps not bog down space by not installing too many unnecessary packages which won't be used from outside a single program.

An executable will be made available when I get the time to make it, but until then, this is the only method.
