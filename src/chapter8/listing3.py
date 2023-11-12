'''
Created on Nov 10, 2023

@author: immanueltrummer
'''
import argparse
import openai


def transcribe(audio_path):
    """ Transcribe audio file to text.
    
    Args:
        audio_path: path to audio file.
    
    Returns:
        transcribed text.
    """
    with open(audio_path, 'rb') as audio_file:
        return openai.Audio.transcribe(
            'whisper-1', audio_file)


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('openaikey', type=str, help='OpenAI access key')
    parser.add_argument('audiopath', type=str, help='Path to audio file')
    args = parser.parse_args()

    openai.api_key = args.openaikey

    transcript = transcribe(args.audiopath)
    print(transcript)