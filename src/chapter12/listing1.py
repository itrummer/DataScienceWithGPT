'''
Created on Mar 25, 2024

@author: immanueltrummer
'''
from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.runnables.passthrough import RunnablePassthrough

import argparse
import pandas as pd


def create_chain(openai_key):
    """ Creates chain for text classification.
    
    Args:
        openai_key: OpenAI access key.
    
    Returns:
        a chain for text classification.
    """
    prompt = ChatPromptTemplate.from_template(
        '{text}\n'
        'Is the sentiment positive or negative?\n'
        'Answer ("Positive"/"Negative")\n')
    llm = ChatOpenAI(
        model='gpt-3.5-turbo', temperature=0, 
        openai_api_key=openai_key, max_tokens=1)
    parser = StrOutputParser()
    chain = ({'text':RunnablePassthrough()} | prompt | llm | parser)
    return chain


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='Path to input .csv file')
    parser.add_argument('openai_key', type=str, help='OpenAI access key')
    args = parser.parse_args()
    
    df = pd.read_csv(args.file_path)
    chain = create_chain(args.openai_key)
    
    results = chain.batch(list(df['text']))
    df['class'] = results
    df.to_csv('result.csv')