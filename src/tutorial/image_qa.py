'''
Created on Jul 12, 2024

@author: immanueltrummer
'''
import argparse
import openai

client = openai.OpenAI()


def analyze_image(image_url_1, image_url_2, question):
    """ Answer question about two input images.
    
    Args:
        image_url_1: URL of first image to analyze.
        image_url_2: URL of second image to analyze.
        question: obtain answer to this question.
    
    Returns:
        Answer to input question.
    """
    message = {'role':'user', 'content':[
        {'type':'text', 'text':question},
        {'type':'image_url', 'image_url':{'url':image_url_1}},
        {'type':'image_url', 'image_url':{'url':image_url_2}}
        ]}
    messages = [message]
    reply = client.chat.completions.create(
        model='gpt-4o',
        messages=messages
        )
    return reply.choices[0].message.content


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('image_url_1', type=str, help='First image URL')
    parser.add_argument('image_url_2', type=str, help='Second image URL')
    parser.add_argument('question', type=str, help='Question about images')
    args = parser.parse_args()
    
    answer = analyze_image(
        args.image_url_1, args.image_url_2, 
        args.question)
    print(answer)