import os
from flask import Flask, request, render_template
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

app = Flask(__name__)

# Set up YouTube Data API client with API key from environment variable
api_key = os.environ.get('google_api')
print("Google API Key:", api_key)
if not api_key:
    raise ValueError("Please set the 'google_api' environment variable with your API key.")

youtube = build('youtube', 'v3', developerKey=api_key)

@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = ""
    error = ""
    if request.method == 'POST':
        url = request.form['url']
        video_id = extract_video_id(url)
        try:
            transcript = get_video_transcript(video_id)
        except HttpError as e:
            error = str(e)
    return render_template('index.html', transcript=transcript, error=error)

def extract_video_id(url):
    video_id = None
    if 'youtu.be' in url:
        video_id = url.split('/')[-1]
    elif 'watch' in url:
        video_id = url.split('v=')[-1]
    return video_id

def get_video_transcript(video_id):
    caption_response = youtube.captions().list(
        part='snippet',
        videoId=video_id
    ).execute()

    captions = caption_response.get('items', [])
    auto_generated_captions_available = False
    for caption in captions:
        if caption['snippet']['trackKind'] == 'ASR':
            auto_generated_captions_available = True
            break
    
    if auto_generated_captions_available:
        # Auto-generated captions available
        caption_id = captions[0]['id']
        caption_response = youtube.captions().download(
            id=caption_id,
            tfmt='vtt'
        ).execute()
        transcript = parse_vtt(caption_response)
        return transcript
    else:
        return "No auto-generated captions available for this video."

def parse_vtt(vtt_content):
    lines = vtt_content.split('\n')
    transcript = ''
    for line in lines:
        if line.strip() and not line.startswith('WEBVTT') and not line.startswith('NOTE'):
            transcript += line.strip() + ' '
    return transcript

if __name__ == '__main__':
    app.run(debug=True)
