'''
Created on Feb 6, 2024

@author: immanueltrummer
'''
import argparse
import openai

client = openai.OpenAI()


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('job_id', type=str, help='ID of fine-tuning job')
    args = parser.parse_args()
    
    job_info = client.fine_tuning.jobs.retrieve(args.job_id)
    print(job_info)