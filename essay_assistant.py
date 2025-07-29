import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# Load API key
load_dotenv()
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError("Please set BASE_URL, API_KEY, and MODEL_NAME.")

set_tracing_disabled(disabled=True)

# Create OpenAI client
client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

#Create agent
agent = Agent(
    name="Essay",
    instructions="You are a helpful essay assistant, your job is to write a beautiful essay in simple and fluent language, highlighting the main points of the topic you will be given. Always try to keep some points, such as : Introduction, Necessity, Advantages, Disadvantages, Conclusion etc. The essay should be a minimum of five to ten paragraphs",
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
)

#async function
async def generate_essay(prompt: str) -> str:
    result = await Runner.run(agent, prompt)
    return result.final_output
