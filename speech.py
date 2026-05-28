import whisper
from gtts import gTTS
import os

MODEL_NAME = "base"

# =========================================
# SPEECH TO TEXT
# =========================================

def speech_to_text(audio_file):

    print("[+] Chargement du modèle...")

    model = whisper.load_model(MODEL_NAME)

    print("[+] Transcription en cours...")

    result = model.transcribe(audio_file)

    text = result["text"]

    print("\n========== TRANSCRIPTION ==========\n")
    print(text)

    with open("transcription.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("\n[+] Sauvegardé dans transcription.txt")

# =========================================
# TEXT TO SPEECH
# =========================================

def text_to_speech(text, output_file="output.mp3", lang="fr"):

    tts = gTTS(text=text, lang=lang)

    tts.save(output_file)

    print(f"[+] Audio généré : {output_file}")

# =========================================
# MENU
# =========================================

while True:

    print("\n1. Speech To Text")
    print("2. Text To Speech")
    print("3. Quitter")

    choix = input("Choix : ")

    if choix == "1":

        audio = input("Chemin audio : ")

        if os.path.exists(audio):
            speech_to_text(audio)
        else:
            print("Fichier introuvable")

    elif choix == "2":

        text = input("Texte : ")

        filename = input("Nom fichier mp3 : ")

        if filename.strip() == "":
            filename = "output.mp3"

        text_to_speech(text, filename)

    elif choix == "3":
        break
