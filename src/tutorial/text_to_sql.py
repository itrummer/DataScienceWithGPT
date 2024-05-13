'''
Created on May 13, 2024

@author: immanueltrummer
'''
import openai
import argparse
import re
import sqlite3


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
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role':'user', 'content':prompt}
            ]
        )
    return response.choices[0].message.content


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
    parser.add_argument('db_path', type=str, help='Path to database')
    args = parser.parse_args()

    client = openai.OpenAI()
    
    description = get_structure(args.db_path)
    
    question = None
    while True:
        question = input('Enter question!')
        
        if question == 'quit':
            break
    
        try:
            prompt = create_prompt(description, question)
            print(prompt)
            
            completion = call_llm(prompt)
            query = re.findall('```sql(.*)```', completion, re.DOTALL)[0]
            print(query)
            
            result = process_query(args.db_path, query)
            print(f'Result:\n{result}')
        
        except Exception as e:
            print(e)