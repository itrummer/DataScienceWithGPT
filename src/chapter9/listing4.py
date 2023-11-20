'''
Created on Nov 12, 2023

@author: immanueltrummer
'''
import argparse
import openai
import scipy.io.wavfile
import sounddevice
import sqlite3
import time


def get_structure(data_path):
    """ Extract structure from SQLite database.
    
    Args:
        data_path: path to SQLite data file.
    
    Returns:
        text description of database structure.
    """
    with sqlite3.connect(data_path) as connection:
        cursor = connection.cursor()
        cursor.execute("select sql from sqlite_master where type = 'table';")
        table_rows = cursor.fetchall()
        table_ddls = [r[0] for r in table_rows]
        return '\n'.join(table_ddls)


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


def create_prompt(description, question):
    """ Generate prompt to translate question into SQL query.
    
    Args:
        description: text description of database structure.
        question: question about data in natural language.
    
    Returns:
        prompt for question translation.
    """
    parts = []
    parts += ['Database:']
    parts += [description]
    parts += ['Translate this question into SQL query:']
    parts += [question]
    parts += ['SQL Query:']
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


def process_query(data_path, query):
    """ Processes SQL query and returns result.
    
    Args:
        data_path: path to SQLite data file.
        query: process this query on database.
    
    Returns:
        query result.
    """
    with sqlite3.connect(data_path) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        table_rows = cursor.fetchall()
        table_strings = [str(r) for r in table_rows]
        return '\n'.join(table_strings)


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('dbpath', type=str, help='Path to SQLite data')
    parser.add_argument('openaikey', type=str, help='OpenAI access key')
    args = parser.parse_args()

    openai.api_key = args.openaikey
    data_structure = get_structure(args.dbpath)
    
    while True:
        
        user_input = input('Press enter to record (type quit to quit).')
        if user_input == 'quit':
            break
        
        audio_path = 'question.wav'
        record(audio_path)
        question = transcribe(audio_path)
        print(f'Question: {question}')
        
        prompt = create_prompt(data_structure, question)
        query = call_llm(prompt)
        print(f'SQL: {query}')

        try:    
            answer = process_query(args.dbpath, query)
            print(f'Answer: {answer}')
        except:
            print('Error processing query! Try to reformulate.')