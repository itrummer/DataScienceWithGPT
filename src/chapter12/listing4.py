'''
Created on Mar 31, 2024

@author: immanueltrummer
'''
import argparse
import openai

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('openaikey', type=str, help='OpenAI access key')
    parser.add_argument('datadir', type=str, help='Path to data directory')
    parser.add_argument('question', type=str, help='A question to answer')
    args = parser.parse_args()

    openai.api_key = args.openaikey

    documents = SimpleDirectoryReader(args.datadir).load_data()
    index = VectorStoreIndex.from_documents(documents)
    engine = index.as_query_engine()
    answer = engine.query(args.question)
    print(answer)