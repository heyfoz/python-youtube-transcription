# Python YouTube Transcription

This repository contains Python scripts and a local Flask web application for transcribing YouTube videos using various methods. It includes functionalities to retrieve video transcripts using the YouTube Data API, download audio from YouTube videos, and convert audio to text using speech recognition.

## Features

- **get_youtube_captions.py**: Contains functions to retrieve YouTube video transcripts using the YouTube Data API.
- **youtube_speech_recognition.py**: Provides functionality to download audio from YouTube videos for transcription.
- **download_youtube_audio.py**: Script to download YouTube audio and save it with a timestamp-based filename.
- **index.html**: HTML template for the Flask web application UI to transcribe YouTube videos.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ffm5113/python_youtube_transcription.git
    ```

2. Install the required libraries:

    ```bash
    pip install Flask google-api-python-client pytube pydub SpeechRecognition
    ```

## Usage

1. Ensure you have set up your Google API key and environment variable as specified in `get_youtube_captions.py`.
2. Run the desired Flask application (`get_youtube_captions.py`, or `youtube_speech_recognition.py`).
3. Open your web browser and navigate to `http://localhost:5000` to access the web application.
4. Enter a YouTube video URL and choose the desired transcription option.
5. Optionally, use `get_youtube_captions.py` to download a .wav file to the project directory.

## Documentation

- [YouTube Data API Documentation](https://developers.google.com/youtube/v3/docs)
- [pytube Documentation](https://pytube.io/en/latest/)
- [pydub Documentation](https://github.com/jiaaro/pydub#documentation)

## Note

- The `index.html` file can be used with any of the Flask scripts mentioned above.
- There are some limitations on YouTube regarding audio availability based on intellectual property concerns and user configurations. Some videos may not be accessible for transcription.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
