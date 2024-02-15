from openai import OpenAI
from config import openai_key
import json
import os

client = OpenAI(api_key = openai_key)

# Load the JSON data
with open('data.json', 'r') as f:
    data = json.load(f)

# def qna(text):
    # prmopt = text

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
{"role": "system", "content": "You are a softBuildersassistant."},
{"role": "user", "content": "What is SoftBuilders?"},
{"role": "assistant", "content": "SoftBuilders is asoftware Company. It provides various servicesincluding web development, app development, UI/UXdesign, machine learning and Block chain and locatedin dubai."},
{"role": "user", "content": "what is the address of company"}
])


content = response.choices[0].message.content
print(content)

    
    # try:
    #     with open('data.json', 'r') as f:
    #         data = json.loads(f)
    # except(json.JSONDecodeError, IndexError):
    #     pass

# if __name__ == "__main__":
#     prompt = "What is softbuilders?"
#     df = qna(prompt)
#     print(df.to_string())