'''
Created on Jan 28, 2024

@author: immanueltrummer
'''
import argparse
import openai
import sqlite3


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
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {'role':'user', 'content':prompt}
            ]
        )
    return response['choices'][0]['message']['content']


def execute_query(db_path, sql):
    """ Executes SQL query and returns result. 
    
    Args:
        db_path: path to SQLite database file.
        sql: process this SQL query.
    
    Returns:
        query result
    """
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        table_rows = cursor.fetchall()
        table_strings = [str(r) for r in table_rows]
        return '\n'.join(table_strings)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('dbpath', type=str, help='Path to SQLite DB file')
    parser.add_argument('openaikey', type=str, help='OpenAI access key')
    parser.add_argument('question', type=str, help='A question about game sales')
    args = parser.parse_args()

    openai.api_key = args.openaikey

    prompt = create_prompt(args.question)
    print(f'Prompt:\n{prompt}')
    
    query = call_llm(prompt)
    print(f'Query:\n{query}')
    
    result = execute_query(args.dbpath, query)
    print(f'Result:\n{result}')