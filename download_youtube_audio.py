# Script for downloading audio from YouTube videos, converting it to .wav format, and saving with a timestamped filename

from pytube import YouTube  # For downloading YouTube videos
from pydub import AudioSegment  # To convert audio to .wav
import os  # For operating system functionalities

def download_youtube_audio(youtube_url):
    try:
        # Download YouTube video
        yt = YouTube(youtube_url)  # Create pytube YouTube object
        stream = yt.streams.filter(only_audio=True).first()  # Filter for and select 1st available audio-only stream
        stream.download(filename='audio.mp4')  # Download audio stream & save it as 'audio.mp4'

        audio = AudioSegment.from_file('audio.mp4', format="mp4")  # Load the audio file into a pydub AudioSegment object

        timestamped_filename = 'audio_' + str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + '.wav'  # Generate audio filename w/ timestamp
        audio.export(timestamped_filename, format='wav')  # Export audio file to WAV format

        os.remove('audio.mp4')  # Remove the temporary MP4 file after conversion

        return timestamped_filename  # Return filename of the converted WAV file

    except Exception as e:
        raise Exception("Error downloading YouTube audio: " + str(e))  # Handle exceptions and raise custom error message

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
