from gtts import gTTS
import os

mytext = 'Text to speech test using Python and G T T S'
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("./welcome.mp3")

os.system("mpg321 ./welcome.mp3")
