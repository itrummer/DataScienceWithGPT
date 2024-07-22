'''
Created on Jul 14, 2024

@author: immanueltrummer
'''
import argparse
import openai

client = openai.OpenAI()


def transcribe_audio(audiopath):
    """ Transcribes audio files and returns text.
    
    Args:
        audiopath: path to file to transcribe.
    
    Returns:
        transcription.
    """
    with open(audiopath, 'rb') as audio_file:
        reply = client.audio.transcriptions.create(
            model='whisper-1', file=audio_file
            )
        return reply.text


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('audiopath', type=str, help='Path to audio file')
    args = parser.parse_args()
    
    reply = transcribe_audio(args.audiopath)
    print(reply)