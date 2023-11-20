'''
Created on Nov 20, 2023

@author: immanueltrummer
'''
import argparse
import openai
import requests
import scipy.io.wavfile
import sounddevice
import time


def record(output_path):
    """ Record audio and store in .wav file. 
    
    Args:
        output_path: store audio recording there.
    """
    sample_rate = 44100
    nr_frames = 5 * sample_rate
    recording = sounddevice.rec(nr_frames, samplerate=sample_rate, channels=1)
    sounddevice.wait()
    scipy.io.wavfile.write(output_path, sample_rate, recording)


def transcribe(audio_path):
    """ Transcribe audio file to text.
    
    Args:
        audio_path: path to audio file.
    
    Returns:
        transcribed text.
    """
    with open(audio_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe(
            file=audio_file, model='whisper-1')
        return transcription.text


def create_prompt(to_translate, to_language):
    """ Generate prompt to translate text to target language.
    
    Args:
        to_translate: translate this text.
        to_language: translate text to this language.
    
    Returns:
        Translated text.
    """
    parts = []
    parts += [f'Translate this text to {to_language}:']
    parts += [to_translate]
    parts += ['Translated text:']
    return '\n'.join(parts)


def call_llm(prompt):
    """ Query large language model and return answer.
    
    Args:
        prompt: input prompt for language model.
    
    Returns:
        Answer by language model.
    """
    for nr_retries in range(1, 4):
        try:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role':'user', 'content':prompt}
                    ]
                )
            return response['choices'][0]['message']['content']
        except:
            time.sleep(nr_retries * 2)
    raise Exception('Cannot query OpenAI model!')


def generate_speech(ai_key, speech_text):
    """ Generates speech for given text.
    
    Args:
        ai_key: access key for OpenAI.
        speech_text: generate speech for this text.
    
    Returns:
        query result.
    """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {ai_key}'
    }
    payload = {'model': 'tts-1', 'input':speech_text, 'voice':'alloy'}
    response = requests.post(
        'https://api.openai.com/v1/chat/completions', 
        headers=headers, json=payload)
    return response

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('openaikey', type=str, help='OpenAI access key')
    parser.add_argument('tolanguage', type=str, help='Target language')
    args = parser.parse_args()

    openai.api_key = args.openaikey
    
    while True:
        
        user_input = input('Press enter to record (type quit to quit).')
        if user_input == 'quit':
            break
        
        audio_path = 'to_translate.wav'
        record(audio_path)
        to_translate = transcribe(audio_path)
        print(f'Original text: {to_translate}')
        
        prompt = create_prompt(to_translate, args.tolanguage)
        translated = call_llm(prompt)
        print(f'Translated text: {translated}')
        
        response = generate_speech(args.openaikey, translated)
        print(response)