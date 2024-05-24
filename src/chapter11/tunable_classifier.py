'''
Created on Feb 6, 2024

@author: immanueltrummer
'''
import argparse
import openai
import pandas as pd
import time

client = openai.OpenAI()


def create_single_text_prompt(text, label):
    """ Create prompt for classifying one single text.
    
    Args:
        text: text to classify.
        label: correct class label (empty if unavailable).
    
    Returns:
        Prompt for text classification.
    """
    task = 'Is the sentiment positive or negative?'
    answer_format = 'Answer ("pos"/"neg")'
    return f'{text}\n{task}\n{answer_format}:{label}'


def create_prompt(text, samples):
    """ Generates prompt for sentiment classification.
    
    Args:
        text: classify this text.
        samples: integrate these samples into prompt.
    
    Returns:
        Input for LLM.
    """
    parts = []
    for _, row in samples.iterrows():
        sample_text = row['text']
        sample_label = row['sentiment']
        prompt = create_single_text_prompt(sample_text, sample_label)
        parts += [prompt]
    
    prompt = create_single_text_prompt(text, '')
    parts += [prompt]
    return '\n'.join(parts)


def call_llm(prompt, model, max_tokens, out_tokens):
    """ Query large language model and return answer.
    
    Args:
        prompt: input prompt for language model.
        model: name of OpenAI model to choose.
        max_tokens: maximal output length in tokens.
        out_tokens: prioritize these token IDs in output.
    
    Returns:
        Answer by language model and total number of tokens.
    """
    optional_parameters = {}
    if max_tokens:
        optional_parameters['max_tokens'] = max_tokens
    if out_tokens:
        logit_bias = {int(tid):100 for tid in out_tokens.split(',')}
        optional_parameters['logit_bias'] = logit_bias
    
    for nr_retries in range(1, 4):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {'role':'user', 'content':prompt}
                    ],
                **optional_parameters, temperature=0
                )
            
            answer = response.choices[0].message.content
            nr_tokens = response.usage.total_tokens
            return answer, nr_tokens
        
        except Exception as e:
            print(f'Exception: {e}')
            time.sleep(nr_retries * 2)
    
    raise Exception('Cannot query OpenAI model!')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='Path to input file')
    parser.add_argument('model', type=str, help='Name of OpenAI model')
    parser.add_argument('max_tokens', type=int, help='Maximal output size')
    parser.add_argument('out_tokens', type=str, help='Tokens to prioritize')
    parser.add_argument('nr_samples', type=int, help='Number of samples')
    parser.add_argument('sample_path', type=str, help='Path to samples')
    args = parser.parse_args()
    
    df = pd.read_csv(args.file_path)
    
    samples = pd.DataFrame()
    if args.nr_samples:
        samples = pd.read_csv(args.sample_path)
        samples = samples[:args.nr_samples]
    
    nr_correct = 0
    nr_tokens = 0
    
    for _, row in df.iterrows():
        
        text = row['text']
        prompt = create_prompt(text, samples)
        label, current_tokens = call_llm(
            prompt, args.model, 
            args.max_tokens, 
            args.out_tokens)
        
        ground_truth = row['sentiment']
        if label == ground_truth:
            nr_correct += 1
        nr_tokens += current_tokens
        
        print(f'Label: {label}; Ground truth: {ground_truth}')

    print(f'Number of correct labels:\t{nr_correct}')
    print(f'Number of tokens used   :\t{nr_tokens}')