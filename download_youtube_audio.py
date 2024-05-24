from flask import Flask, request, jsonify, render_template
from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_audio(youtube_url):
    try:
        # Download YouTube video
        yt = YouTube(youtube_url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(filename='audio.mp4')

        # Convert audio to WAV format
        audio = AudioSegment.from_file('audio.mp4', format="mp4")
        audio.export('audio.wav', format='wav')

        # Clean up temporary MP4 file
        os.remove('audio.mp4')

        return 'audio.wav'
    except Exception as e:
        raise Exception("Error downloading YouTube audio: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
