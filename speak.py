import os
import time
import pyaudio
import speech_recognition as sr
import openai
import uuid
import playsound
from gtts import gTTS

api_key = "hidden"

openai.api_key = api_key


def text_to_speech(text, lang='hi'):
    speech = gTTS(text=text, lang=lang, slow=False)
    file_name = f"response_{str(uuid.uuid4())}.mp3"
    speech.save(file_name)
    playsound.playsound(file_name, block=False)


while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=0) as source:
            print("Listening...")

            while True:
                try:
                    audio = r.listen(source, timeout=5)
                    said = r.recognize_google(audio, language='hi')
                    print("You said:", said)

                    if "श्लोक" in said:
                        new_string = said.replace("श्लोक", "")
                        new_string = new_string.strip()
                        print("Translated input:", new_string)

                        # Use the GPT-3.5 model with the Hindi language code
                        completion = openai.Completion.create(
                            engine="davinci",
                            prompt=new_string,
                            max_tokens=50,
                            temperature=0.7,
                            stop=None,
                            frequency_penalty=0.0,
                            presence_penalty=0.0,
                        )
                        text = completion.choices[0].text

                        if text:
                            # Print and speak the response in Hindi
                            print("चैटजीपीटी से जवाब:", text)
                            text_to_speech(text, lang='hi')

                    elif not said:
                        print("Sorry, please repeat.")

                except sr.WaitTimeoutError:
                    print("Timeout: No speech detected.")
                except Exception as e:
                    print(e)

    get_audio()
