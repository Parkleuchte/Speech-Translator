from translate import Translator
from text_to_speech import tts

class Translate():
        def main(text):
            target_language = "de"

            try:
                translator = Translator(to_lang=target_language)
                translation = translator.translate(text)
                print(f"Übersetzter Text ({target_language}): {translation}\n")
                tts(translation)
            except Exception as e:
                print(f"Fehler bei der Übersetzung: {e}\n")
