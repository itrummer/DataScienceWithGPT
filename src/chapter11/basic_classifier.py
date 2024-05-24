'''
Created on Feb 6, 2024

@author: immanueltrummer
'''
import argparse
import openai
import pandas as pd
import time

client = openai.OpenAI()


def create_prompt(text):
    """ Create prompt for sentiment classification.
    
    Args:
        text: text to classify.
    
    Returns:
        Prompt for text classification.
    """
    task = 'Is the sentiment positive or negative?'
    answer_format = 'Answer ("pos"/"neg")'
    return f'{text}\n{task}\n{answer_format}:'


def call_llm(prompt):
    """ Query large language model and return answer.
    
    Args:
        prompt: input prompt for language model.
    
    Returns:
        Answer by language model and total number of tokens.
    """
    for nr_retries in range(1, 4):
        try:
            response = client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role':'user', 'content':prompt}
                    ],
                temperature=0
                )
            
            answer = response.choices[0].message.content
            nr_tokens = response.usage.total_tokens
            return answer, nr_tokens
        
        except Exception as e:
            print(f'Exception: {e}')
            time.sleep(nr_retries * 2)
    
    raise Exception('Cannot query OpenAI model!')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='Path to input file')
    args = parser.parse_args()
    
    df = pd.read_csv(args.file_path)
    
    nr_correct = 0
    nr_tokens = 0
    
    for _, row in df.iterrows():
        
        text = row['text']
        prompt = create_prompt(text)
        label, current_tokens = call_llm(prompt)
        
        ground_truth = row['sentiment']
        if label == ground_truth:
            nr_correct += 1
        nr_tokens += current_tokens
        
        print(f'Label: {label}; Ground truth: {ground_truth}')

    print(f'Number of correct labels:\t{nr_correct}')
    print(f'Number of tokens used   :\t{nr_tokens}')