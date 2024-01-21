'''
Created on Jan 14, 2024

@author: immanueltrummer
'''
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('ai_key', type=str, help='Anthropic access key')
    parser.add_argument('question', type=str, help='A question for Claude')
    args = parser.parse_args()
    
    anthropic = Anthropic(api_key=args.ai_key)
    
    prompt = f'{HUMAN_PROMPT}{args.question}{AI_PROMPT}'
    completion = anthropic.completions.create(
        model='claude-2.1', max_tokens_to_sample=100,
        prompt=prompt)
    
    print(completion.completion)