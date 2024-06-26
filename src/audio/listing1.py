'''
Created on Nov 10, 2023

@author: immanueltrummer
'''
import argparse
import openai

client = openai.OpenAI()


def transcribe(audio_path):
    """ Transcribe audio file to text.
    
    Args:
        audio_path: path to audio file.
    
    Returns:
        transcribed text.
    """
    with open(audio_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file, model='whisper-1')
        return transcription.text


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('audiopath', type=str, help='Path to audio file')
    args = parser.parse_args()

    transcript = transcribe(args.audiopath)
    print(transcript)