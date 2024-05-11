import ollama
import time

start_time = time.time()

response = ollama.chat(model='llama3:8b', messages=[
  {
    'role': 'user',
    'content': 'What are the famous foods in Taiwan?',
  },
])

end_time = time.time()

print(response['message']['content'])

elapsed_time = end_time - start_time
print(f"Duration：{elapsed_time} seconds")