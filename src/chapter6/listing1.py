'''
Created on Sep 6, 2023

@author: immanueltrummer
'''
import argparse
import openai
import pandas as pd
import time

client = openai.OpenAI()


def create_prompt(text):
    """ Generates prompt for sentiment classification.
    
    Args:
        text: classify this text.
    
    Returns:
        input for LLM.
    """
    task = 'Is the sentiment positive or negative?'
    answer_format = 'Answer ("Positive"/"Negative")'
    return f'{text}\n{task}\n{answer_format}:'


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


def classify(text):
    """ Classify input text.
    
    Args:
        text: assign this text to a class label.
    
    Returns:
        name of class.
    """
    prompt = create_prompt(text)
    print(prompt)
    label = call_llm(prompt)
    print(label)
    return label


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='Path to input .csv file')
    args = parser.parse_args()
    
    df = pd.read_csv(args.file_path)
    
    df['class'] = df['text'].apply(classify)
    statistics = df['class'].value_counts()
    print(statistics)
    
    df.to_csv('result.csv')