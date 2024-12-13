import time
from deepgram import DeepgramClient, SpeakOptions
from pydub import AudioSegment
from openal import *
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
# Initialize Deepgram SDK
DEEPGRAM_API_KEY = os.getenv("API")
deepgram = DeepgramClient(DEEPGRAM_API_KEY)

# Sample data: Objects with their positions
objects = [
    {"name": "table", "position": [-10, -20, 0]},
    # {"name": "chair", "position": [10, 0, 0]},
    # {"name": "lamp", "position": [0, 10, 0]},
    # {"name": "sofa", "position": [5, 10, 0]},
]

# Generate TTS audio files and convert them to .wav format
async def generate_audio_files(objects):
    for obj in objects:
        # STEP 1: Create a Deepgram client.
        # By default, the DEEPGRAM_API_KEY environment variable will be used for the API Key

        # STEP 2: Configure the options (such as model choice, audio configuration, etc.)
        options = SpeakOptions(
            model="aura-asteria-en",
        )
        filename=f"{obj['name']}.mp3"
        SPEAK_OPTIONS = {"text": obj["name"]}
        # STEP 3: Call the save method on the speak property
        response = deepgram.speak.rest.v("1").save(filename, SPEAK_OPTIONS, options)
       
       
       
        # Convert MP3 to WAV using pydub
        wav_filename = f"{obj['name']}.wav"
        audio = AudioSegment.from_mp3(filename)
        
        # Export the audio to WAV format without changing the pitch
        audio.export(wav_filename, format="wav")
        
        # Add the .wav filename to the object data
        obj["audio_file"] = wav_filename

        # Clean up the MP3 file after conversion
        os.remove(filename)


def play_audio(objects):
    sources = []
    for obj in objects:
        # Open each WAV audio file and set its position in 3D space
        source = oalOpen(obj["audio_file"])
        source.set_position(obj["position"])  # Set the position of the object in 3D space
        source.set_looping(True)  # Play once
        source.play()  # Start playing the sound
        sources.append(source)

    # Check if any of the sources is still playing
    while True:
        still_playing = False
        for source in sources:
            # Check the state of the source
            state = source.get_state()
            if state == AL_PLAYING:
                still_playing = True
                break
        
        if not still_playing:
            break
        time.sleep(0.1)  # Wait a bit before checking again

# Clean up (close the OpenAL context)
def cleanup():
    oalQuit()
    # Delete audio files after playing
    for obj in objects:
        os.remove(obj["audio_file"])

if __name__ == "__main__":
    # Generate audio files for objects (MP3 -> WAV)
    asyncio.run(generate_audio_files(objects))

    # Play the sounds at the positions of their respective objects
    play_audio(objects)

    # Clean up resources
    cleanup()