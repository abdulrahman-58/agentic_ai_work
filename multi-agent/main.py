from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
import asyncio
import chainlit as cl
load_dotenv()

MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key = GEMINI_API_KEY,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
    )
model = OpenAIChatCompletionsModel(
    model = MODEL_NAME,
    openai_client = external_client
    )

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True
    )

webdev = Agent(
    name = "Web Developer",
    instructions = "You are a professional web developer. Handle only web development queries. If asked something else, politely say you're a web developer only.",
    model = model
    )
mobile_dev = Agent(
    name= "Mobile App Developer",
    instructions = "You are an expert in mobile app development. Handle only mobile-related queries. If asked something else, politely say you're a mobile developer only.",
    model = model
    )

marketing_agent = Agent(
    name="Marketing agent",
    instructions = "Your task is to work as a professional digital marketing expert and solve your field related quiries and say sorry when user ask you other than digital marketing.",
    model = model
    )
    
manager = Agent(
    name = "Manager",
    instructions = """You are the team manager. Your job is to analyze the user request, and forward the task to the right agent:
- Web-related → Web Developer
- Mobile-related → Mobile Developer
- Marketing-related → Marketing Agent
If the task doesn’t belong to any of these, politely respond that the team cannot handle it.""",
    model = model
    )
@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Welcome to Multi-Agent Assistant!").send()
    await cl.Message(content="""
This system includes:
- 🧑‍💻 Web Developer
- 📱 Mobile Developer
- 📢 Marketing Agent

All managed by a 🧠 Manager Agent who delegates tasks accordingly.
Type anything to get started!
""").send()


@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content

    # Manager receives the user input
    await cl.Message(content="🧠 Manager is reviewing your request...").send()

    # Let Manager analyze and decide which agent to use
    task_assignment_prompt = f"""
You are the manager. Read the user's message:
"{user_input}"
Then respond ONLY with one of the following:
- Web Developer
- Mobile Developer
- Marketing Agent
- None
depending on which agent should handle this.
"""
    agent_decision = await Runner.run(manager,task_assignment_prompt, run_config=config)

    agent_name = agent_decision.final_output.strip()

    if agent_name == "Web Developer":
        await cl.Message(content="✅ Assigning to Web Developer...").send()
        result = await Runner.run(webdev, user_input, run_config=config)
    elif agent_name == "Mobile Developer":
        await cl.Message(content="✅ Assigning to Mobile Developer...").send()
        result = await Runner.run(mobile_dev, user_input, run_config=config)
    elif agent_name == "Marketing Agent":
        await cl.Message(content="✅ Assigning to Marketing Agent...").send()
        result = await Runner.run(marketing_agent, user_input, run_config=config)
    else:
        result = "❌ Sorry, our team currently can't handle this type of request."

    # Final output to user
    await cl.Message(content=result if isinstance(result, str) else result.final_output).send()