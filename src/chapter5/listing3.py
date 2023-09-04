'''
Created on Sep 4, 2023

@author: immanueltrummer
'''
import openai
openai.api_key = '...'
result = openai.Completion.create(
    model='text-davinci-003', 
    prompt='Tell me a story!')
print(result)