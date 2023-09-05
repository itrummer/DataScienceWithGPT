'''
Created on Sep 4, 2023

@author: immanueltrummer
'''
import openai
openai.api_key = '...'
result = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role':'user', 'content':'Tell me a story!'}
        ]
    )
print(result)