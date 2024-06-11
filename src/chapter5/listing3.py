'''
Created on Sep 4, 2023

@author: immanueltrummer
'''
import openai
openai.api_key = '...'
result = openai.Completion.create(
    model='text-davinci-003', 
    prompt='Tell me a story!' +\
        '\n\nOnce upon a time, there was a kingdom ruled by a wise and',
        max_tokens=512, stop='happily ever after', 
        temperature=1, best_of=2, 
        presence_penalty=0.5,
        logit_bias={14844:-100})
print(result['choices'][0]['text'])