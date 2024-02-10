'''
Created on Feb 6, 2024

@author: immanueltrummer
'''
import argparse
import openai
import time


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('in_path', type=str, help='Path to input file')
    parser.add_argument('ai_key', type=str, help='OpenAI access key')
    args = parser.parse_args()
    
    openai.api_key = args.ai_key
    reply = openai.File.create(
        file=open(args.in_path), purpose='fine-tune')
    file_id = reply['id']
    
    reply = openai.FineTuningJob.create(
        training_file=file_id, model='gpt-3.5-turbo')
    job_id = reply['id']
    print(f'Job ID: {job_id}')
    
    status = None
    start_s = time.time()
    
    while not (status == 'succeeded'):
        
        time.sleep(5)
        total_s = time.time() - start_s
        print(f'Fine-tuning since {total_s} seconds.')
        
        reply = openai.FineTuningJob.retrieve(id=job_id)
        status = reply['status']
        print(f'Status: {status}')
    
    print(f'Fine-tuning is finished!')
    model_id = reply['fine_tuned_model']
    print(f'Model ID: {model_id}')