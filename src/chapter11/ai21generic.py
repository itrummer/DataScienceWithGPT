'''
Created on Jan 14, 2024

@author: immanueltrummer
'''
import ai21
import argparse


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('ai_key', type=str, help='AI21 access key')
    parser.add_argument('question', type=str, help='Question to Jurassic')
    args = parser.parse_args()
    
    ai21.api_key = args.ai_key
    
    result = ai21.Completion.execute(
        model='j2-mid', prompt=args.question)
    answer = result['completions'][0]['data']['text']
    
    print(answer)