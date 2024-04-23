from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime
import os

def hablar(texto, idioma):
    tts = gTTS(text=texto, lang=idioma, slow=False)
    archivo = 'hora.mp3'
    tts.save(archivo)
    audio = AudioSegment.from_mp3(archivo)
    play(audio)
    os.remove(archivo)

def anunciar_hora(idioma='es'):
    ahora = datetime.now()
    hora = ahora.strftime('%H:%M')

    if idioma == 'es':
        texto = f"Son las {hora}"
    else:
        texto = f"It is {hora}"

    hablar(texto, idioma)

anunciar_hora('es')
