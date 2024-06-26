'''
Created on Jan 14, 2024

@author: immanueltrummer
'''
import argparse
from anthropic import Anthropic


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('ai_key', type=str, help='Anthropic access key')
    parser.add_argument('question', type=str, help='A question for Claude')
    args = parser.parse_args()
    
    anthropic = Anthropic(api_key=args.ai_key)
    
    completion = anthropic.messages.create(
        model='claude-3-opus-20240229', 
        max_tokens=100,
        messages=[
            {
                'role':'user', 
                'content':args.question
             }])
    
    print(completion.content)