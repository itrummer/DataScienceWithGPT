'''
Created on Sep 4, 2023

@author: immanueltrummer
'''
import openai
client = openai.OpenAI()

result = client.chat.completions.create(
    model='gpt-4o', 
    messages=[{
        'role':'user', 
        'content':'Tell me a story!'
        }])
print(result)