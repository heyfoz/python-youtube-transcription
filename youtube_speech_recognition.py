# Provides functionality to download audio from YouTube videos for transcription with speech recognition

from flask import Flask, request, render_template, jsonify # Web framework imports
from pytube import YouTube  # To download YouTube video
from pydub import AudioSegment  # For audio manipulation
import speech_recognition as sr  # To transcribe audio
import os  # For file handling

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')  # Render the HTML form template

@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        url = request.json['url']  # Get YouTube URL from AJAX request
        update_status('Downloading audio...') 

        # Download YouTube video
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()  # Get first audio-only stream
        stream.download(filename='audio.mp4')  # Download the audio stream

        update_status('Converting audio...') 

        # Convert audio to WAV format using pydub
        audio = AudioSegment.from_file('audio.mp4', format="mp4")
        audio.export('audio.wav', format='wav')  # Export as WAV format

        update_status('Transcribing audio...') 

        # Transcribe audio to text using speech_recognition
        recognizer = sr.Recognizer()
        audio_file = sr.AudioFile('audio.wav')
        with audio_file as source:
            audio_data = recognizer.record(source)  # Record the audio data
            transcript = recognizer.recognize_google(audio_data)  # Recognize speech in the audio

        # Clean up temporary files
        os.remove('audio.mp4')
        os.remove('audio.wav')

        return jsonify({'transcript': transcript})  # Return the transcript as JSON
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return error message if exception occurs

def update_status(status):
    # Logs the status in console
    print(status)  

if __name__ == '__main__':
    app.run(debug=True) # Run Flask app in debug mode
