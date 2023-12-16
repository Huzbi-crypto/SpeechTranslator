import googletrans as gt
import speech_recognition as sr
import gtts
import playsound

source_lang = input("Enter the source language you're going to speak. Follow this format: https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages: ")
target_lang = input("Enter the target language to translate into ('ja', 'en', etc.): ")

# record the voice 
speech_to_txt = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Speech Recognition Ready: Speak Now")
        voice = speech_to_txt.listen(source)
        txt = speech_to_txt.recognize_google(voice, language=source_lang) # Save the captured audio into its textual format
        print(txt) 
except:
    pass

# Translate the audio which is stored in textual format
translator = gt.Translator()
result = translator.translate(txt, dest=target_lang)
print(result.text)

# Convert the translated text into speech
converted_audio = gtts.gTTS(result.text, lang=target_lang)
converted_audio.save('audio.mp3')

# Play the translated audio
playsound.playsound('audio.mp3')
