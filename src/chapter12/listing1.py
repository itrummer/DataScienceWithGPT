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


def create_chain():
    """ Creates chain for text classification.
    
    Returns:
        a chain for text classification.
    """
    prompt = ChatPromptTemplate.from_template(
        '{text}\n'
        'Is the sentiment positive or negative?\n'
        'Answer ("Positive"/"Negative")\n')
    llm = ChatOpenAI(
        model='gpt-4o', temperature=0, 
        max_tokens=1)
    parser = StrOutputParser()
    chain = ({'text':RunnablePassthrough()} | prompt | llm | parser)
    return chain


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='Path to input .csv file')
    args = parser.parse_args()
    
    df = pd.read_csv(args.file_path)
    chain = create_chain()
    
    results = chain.batch(list(df['text']))
    df['class'] = results
    df.to_csv('result.csv')