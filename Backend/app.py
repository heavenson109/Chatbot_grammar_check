import os
import openai

openai.api_key = "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"

def chatgpt_call(prompt, model="gpt-3.5-turbo"):
   response = openai.ChatCompletion.create(
      model=model,
      messages=[
                  {"role": "system", "content": "You have to provide correct English sentence"},
                  {"role": "user", "content": prompt}
               ]
   )
   return response.choices[0].message["content"]

prompt = "I went go to the school"
response = chatgpt_call(prompt)
print(response)
