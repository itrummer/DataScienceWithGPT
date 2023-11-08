'''
Created on Nov 5, 2023

@author: immanueltrummer
'''
import argparse
import openai
import time


def create_prompt(question):
    """ Generate prompt to translate question into SQL query.
    
    Args:
        question: question about data in natural language.
    
    Returns:
        prompt for question translation.
    """
    parts = []
    parts += ['Database:']
    parts += ['create table games(rank int, name text, platform text,']
    parts += ['year int, genre text, publisher text, americasales numeric,']  
    parts += ['eusales numeric, japansales numeric, othersales numeric,'] 
    parts += ['globalsales numeric);']
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


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('openaikey', type=str, help='OpenAI access key')
    parser.add_argument('question', type=str, help='A question about game sales')
    args = parser.parse_args()

    openai.api_key = args.openaikey

    prompt = create_prompt(args.question)
    print(prompt)
    query = call_llm(prompt)
    
    print(f'SQL: {query}')