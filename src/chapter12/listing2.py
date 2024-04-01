'''
Created on Mar 29, 2024

@author: immanueltrummer
'''
import argparse

from langchain.agents.load_tools import load_tools
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_openai import ChatOpenAI


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

    agent = create_sql_agent(
        llm=llm, db=db, verbose=True,
        agent_type='openai-tools',
        extra_tools=extra_tools)
    agent.invoke({'input':args.question})