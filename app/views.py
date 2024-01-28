from django.shortcuts import render
from django.conf import settings
import requests
from pydub import AudioSegment
import uuid
import io



from openai import OpenAI


OPENAI_KEY=settings.OPENAI_KEY
ELEVENLABS_KEY=settings.ELEVENLABS_KEY

openai_client = OpenAI(

    api_key=OPENAI_KEY
)















def text_to_speech(text, voice_id, output_file):
    print('inside text to speech')
    url = "https://api.elevenlabs.io/v1/text-to-speech/" + voice_id
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": f"{ELEVENLABS_KEY}"  # Replace with your API key
    }
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        print("text to speech res:", response)

        if response.status_code == 200:
            print(f'response is 200')
            # Read the audio content from the API response
            audio_content = response.content
            print('getting content')

            # Convert to AudioSegment
            audio = AudioSegment.from_file(io.BytesIO(audio_content), format="mp3")
            print('past audio segment')

            # Save the audio locally as an MP3 file
            audio.export(output_file, format="mp3")
            print('exporting audio')

            print(f"Saved MP3 file locally: {output_file}")

            # Optionally, you can return the file size or any other information
            return output_file
    except Exception as ex:
        # Handle the API request error
        print("text to speech error:", ex)
        return None




def main(request):
    text = "Hello, the game has started."
    voice_id = "bdiU6KSOeqgviMTZdCIe"
    output_file = "output.mp3"

    txting = text_to_speech(text, voice_id, output_file)
    

    
    return render(request, 'index.html')

