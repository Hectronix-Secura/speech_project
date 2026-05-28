# Speech Project

Projet Python de :

- Speech To Text
- Text To Speech

Compatible :
- mp3
- wav
- ogg
- m4a
- flac

## Installation

```bash
sudo apt install ffmpeg python3-venv -y
```

Créer un environnement :

```bash
python3 -m venv venv
source venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Lancement

```bash
python3 speech.py
```

## Technologies

- Python
- Whisper AI
- gTTS
- FFmpeg
