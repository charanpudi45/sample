from gtts import gTTS 
from playsound import playsound
audio="speech.mp3"
language='en'
sp=gTTS(text="this is charan from vishakapatnam",lang=language,slow=False)
sp.save(audio)
playsound(audio)
print("=====audio playing====")
