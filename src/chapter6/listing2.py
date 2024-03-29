'''
Created on Sep 7, 2023

@author: immanueltrummer
'''
import argparse
import openai
import pandas as pd
import time


def create_prompt(text, attributes):
    """ Generates prompt for information extraction.
    
    Args:
        text: extract information from this text.
        attributes: list of attributes.
    
    Returns:
        input for LLM.
    """
    task = 'Extract the following properties:'
    header = '| ' + ' | '.join(attributes) + ' |'
    nr_attributes = len(attributes)
    separator = '| ' + ' | '.join(['---'] * nr_attributes) + ' |'
    return f'{text}\n{task}\n{header}\n{separator}'


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


def post_process(raw_answer):
    """ Extract fields from raw text answer.
    
    Args:
        raw_answer: raw text generated by LLM.
    
    Returns:
        list of result rows.
    """
    results = []
    for raw_row in raw_answer.split('\n'):
        row = raw_row.split('|')
        row = [field.strip() for field in row]
        row = [field for field in row if field]
        results.append(row)
    return results


def extract_rows(text, attributes):
    """ Extract values for attributes from text.
    
    Args:
        text: extract information from this text.
        attributes: list of attributes to extract.
    
    Returns:
        list of rows with attribute values.
    """
    prompt = create_prompt(text, attributes)
    print(prompt)
    result_text = call_llm(prompt)
    print(result_text)
    result_rows = post_process(result_text)
    return result_rows


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='Path to input file')
    parser.add_argument('attributes', type=str, help='Attribute list')
    parser.add_argument('openai_key', type=str, help='OpenAI access key')
    args = parser.parse_args()
    
    openai.api_key = args.openai_key
    input_df = pd.read_csv(args.file_path)
    attributes = args.attributes.split('|')
    
    extractions = []
    for text in input_df['text'].values:
        extractions += extract_rows(text, attributes)
    
    result_df = pd.DataFrame(extractions)
    result_df.columns = attributes
    result_df.to_csv('result.csv')