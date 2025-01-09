import pyttsx3

def tts(text):

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    for voice in voices:
        if "de" in voice.languages:
            engine.setProperty('voice', voice.id)
            break

    engine.setProperty('rate', 150)  # Geschwindigkeit in Wörtern pro Minute
    engine.setProperty('volume', 0.9)  # Lautstärke (0.0 bis 1.0)

    engine.say(text)
    engine.runAndWait()