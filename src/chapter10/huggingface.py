'''
Created on Jan 15, 2024

@author: immanueltrummer
'''
import argparse
import transformers


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('review', type=str, help='Text of a review')
    args = parser.parse_args()
    
    sentiment_task = transformers.pipeline(
        model='cardiffnlp/twitter-roberta-base-sentiment-latest')
    result = sentiment_task(args.review)
    print(result)