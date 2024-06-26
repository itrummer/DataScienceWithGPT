'''
Created on Sep 4, 2023

@author: immanueltrummer
'''
import openai
client = openai.OpenAI()

models = client.models.list()
for model in models.data:
    print(model)