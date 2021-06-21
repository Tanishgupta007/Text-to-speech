from gtts import gTTS
import os
print("Enter the text you want to convert:\n")
a = input("")
mytext = a
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("1.mp3")
os.system("1.mp3")
