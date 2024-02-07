'''
Created on Jan 14, 2024

@author: immanueltrummer
'''
import ai21
import argparse


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('ai_key', type=str, help='AI21 access key')
    parser.add_argument('text', type=str, help='Text to paraphrase')
    args = parser.parse_args()
    
    ai21.api_key = args.ai_key
    
    result = ai21.Paraphrase.execute(
        text=args.text, style='formal')
    
    answer = result['suggestions'][0]['text']
    print(answer)