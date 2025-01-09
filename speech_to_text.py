import speech_recognition as sr
from translator import Translate

def speech_to_text_german():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        
        recognizer.adjust_for_ambient_noise(source)
        print("Jetzt sprechen...")
        
        try:
            audio = recognizer.listen(source)
            
            print("Verarbeite die Eingabe...")
            text = recognizer.recognize_google(audio, language="de-DE")
            
            print(f"Erkannter Text: {text}")
            Translate.main(text)
        except sr.UnknownValueError:
            print("Die Sprache konnte nicht erkannt werden.")
        except sr.RequestError as e:
            print(f"Fehler beim Zugriff auf den Google-Service: {e}")

if __name__ == "__main__":
    speech_to_text_german()
