from gtts import gTTS
import os

mytext = 'Bonjour, je suis un synthétiseur vocal. Faites-moi un bisou, tout-de-suite.'
language = 'fr'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("./bienvenue.mp3")

os.system("mpg321 ./bienvenue.mp3")
