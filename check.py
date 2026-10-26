from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=500,
    messages=[{
         "role": "user",
        "content": "What is Claude AI? Answer in one sentence."}]
)

print(message.content[0].text)
