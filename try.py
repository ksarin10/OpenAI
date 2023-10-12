from gtts import gTTS
import playsound

text = "This is a test."
speech = gTTS(text=text, lang='en', slow=False, tld="com.au")
file_name = "test.mp3"
speech.save(file_name)
playsound.playsound(file_name)
