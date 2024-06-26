'''
Created on Jun 18, 2024

@author: immanueltrummer
'''
import argparse
import google.generativeai as genai


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('api_key', type=str, help='Google API key')
    parser.add_argument('question', type=str, help='Question to answer')
    args = parser.parse_args()
    
    genai.configure(api_key=args.api_key)
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    reply = model.generate_content(args.question)
    
    print(reply.text)