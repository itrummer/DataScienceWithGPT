'''
Created on Feb 6, 2024

@author: immanueltrummer
'''
import argparse
import jsonlines
import pandas


def get_samples(df):
    """ Generate samples from data frame.
    
    Args:
        df: data frame containing samples.
    
    Returns:
        List of samples in OpenAI format for fine-tuning.
    """
    samples = []
    for _, row in df.iterrows():

        text = row['text']
        user_message = {'role':'user', 'content':text}
        
        label = row['sentiment']
        assistant_message = {'role':'assistant', 'content':label}
        
        sample = {'messages':[user_message, assistant_message]}
        samples += [sample]
    
    return samples


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('in_path', type=str, help='Path to input')
    parser.add_argument('out_path', type=str, help='Path to output')
    args = parser.parse_args()
    
    df = pandas.read_csv(args.in_path)
    samples = get_samples(df)
    
    with jsonlines.open(args.out_path, 'w') as file:
        for sample in samples:
            file.write(sample)