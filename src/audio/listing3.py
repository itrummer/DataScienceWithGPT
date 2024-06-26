'''
Created on Nov 20, 2023

@author: immanueltrummer
'''
import argparse
import openai
import playsound
import scipy.io.wavfile
import sounddevice
import time

client = openai.OpenAI()


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
        transcription = client.audio.transcriptions.create(
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
            response = client.chat.completions.create(
                model='gpt-4o',
                messages=[
                    {'role':'user', 'content':prompt}
                    ]
                )
            return response.choices[0].message.content
        except:
            time.sleep(nr_retries * 2)
    raise Exception('Cannot query OpenAI model!')


def generate_speech(speech_text):
    """ Generates speech for given text.
    
    Args:
        speech_text: generate speech for this text.
    
    Returns:
        query result.
    """
    response = client.audio.speech.create(
        model='tts-1', voice='alloy', 
        input=speech_text)
    return response.content

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('tolanguage', type=str, help='Target language')
    args = parser.parse_args()
    
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
        
        speech = generate_speech(translated)
        with open('translation.mp3', 'wb') as file:
            file.write(speech)
            
        playsound.playsound('translation.mp3')