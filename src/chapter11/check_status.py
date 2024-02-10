'''
Created on Feb 6, 2024

@author: immanueltrummer
'''
import argparse
import openai


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('ai_key', type=str, help='OpenAI access key')
    parser.add_argument('job_id', type=str, help='ID of fine-tuning job')
    args = parser.parse_args()
    
    openai.api_key = args.ai_key
    job_info = openai.FineTuningJob.retrieve(id=args.job_id)
    print(job_info)