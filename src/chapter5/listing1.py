'''
Created on Sep 4, 2023

@author: immanueltrummer
'''
import openai
openai.api_key = '...'
models = openai.Model.list()
print(models)