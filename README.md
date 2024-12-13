# 3D Audio Project

This project demonstrates how to generate and play 3D audio using Deepgram TTS, pydub, and OpenAL. The audio files are generated using Deepgram's Text-to-Speech (TTS) API, converted to WAV format, and played in a 3D space using OpenAL.

## Prerequisites

- Python 3.10 or higher
- Deepgram API key
- Virtual environment (optional but recommended)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/3dAudio.git
    cd 3dAudio
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your Deepgram API key:
    ```sh
    echo "API=your_deepgram_api_key" > .env
    ```

## Usage

1. Run the script:
    ```sh
    python audio.py
    ```

2. The script will generate TTS audio files for the objects, convert them to WAV format, and play them in a 3D space.

## Cleanup

The script will automatically delete the generated audio files after playing them.

## Notes

- Ensure that your Deepgram API key is valid and has the necessary permissions for TTS.
- You can add more objects to the `objects` list in `audio.py` to generate and play audio for additional items.
- Adjust the positions of the objects in the `objects` list to change their locations in the 3D space.
- The `.gitignore` file is configured to ignore environment files and generated audio files.
- The project uses `pydub` for audio format conversion and `PyOpenAL` for 3D audio playback.
- The `dotenv` package is used to load environment variables from the `.env` file.
- The `asyncio` package is used to handle asynchronous operations for generating audio files.

## License

This project is licensed under the MIT License.