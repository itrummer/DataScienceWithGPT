'''
Created on Mar 31, 2024

@author: immanueltrummer
'''
import argparse

from langchain.agents.load_tools import load_tools
from langchain.tools import tool
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_openai import ChatOpenAI
from typing import Union


@tool
def convert_currency(USD_amount: float, currency: str) -> Union[float, str]:
    """ Converts an amount in US dollars to another currency.
    
    Args:
        USD_amount: amount in US dollars.
        currency: name of target currency (e.g., "Yen").
    
    Returns:
        input amount in target currency.
    """
    conversion_factors = {
        'Euro':0.93, 'Yen':151.28, 'Yun':0.14, 
        'Pound':1.26, 'Won':0.00074, 'Rupee':0.012}
    
    if currency not in conversion_factors:
        error_message = (
            f'Unknown currency: {currency}!'
            f'Use one of {conversion_factors.keys()}')
        return error_message
    
    conversion_factor = conversion_factors[currency]
    converted_amount = USD_amount * conversion_factor
    return converted_amount


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('openaikey', type=str, help='OpenAI access key')
    parser.add_argument('serpaikey', type=str, help='SERP API access key')
    parser.add_argument('dbpath', type=str, help='Path to SQLite database')
    parser.add_argument('question', type=str, help='A question to answer')
    args = parser.parse_args()
    
    llm = ChatOpenAI(
        openai_api_key=args.openaikey, 
        temperature=0, model='gpt-4')
    db = SQLDatabase.from_uri(f'sqlite:///{args.dbpath}')
    extra_tools = load_tools(
        ['serpapi'], serpapi_api_key=args.serpaikey, llm=llm)
    extra_tools.append(convert_currency)

    agent = create_sql_agent(
        llm=llm, db=db, verbose=True,
        agent_type='openai-tools',
        extra_tools=extra_tools)
    agent.invoke({'input':args.question})