from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-3-sonnet-20241022")

result = model.invoke("What is your name ")

print(result.content)