from openai import OpenAI

client = OpenAI
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variables name, you can do something like:
client = OpenAI(
  api_key="<Your API Here >",
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content": "This is a virtual assistant Alpha"},
    {"role": "user", "content": "write  about ai"}
  ]
)

print(completion.choices[0].message.content)