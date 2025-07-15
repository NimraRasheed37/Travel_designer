import chainlit as cl
from agents import Runner
from agents.run import RunConfig
from config import model, external_client, gemini_config
from traveler.destination_agent import destination_agent
from traveler.explore_agent import explore_agent
from traveler.booking_agent import booking_agent

@cl.on_chat_start
async def start():
    # Initialize session state
    cl.user_session.set("history", [])
    await cl.Message("✨ Welcome! I’m your Travel Assistant ✈️ — here to help you discover, explore, and plan your perfect trip.🌍").send()

@cl.on_message
async def handle(msg: cl.Message):
    history = cl.user_session.get("history") or []
    history.append({"role": "user", "content": msg.content})

    thinking = await cl.Message("✈️ Exploring...").send()

    try:
        result = await Runner.run(
            destination_agent,
            history,
            run_config=gemini_config
            )
        output = result.final_output

        thinking.content = output
        await thinking.update()

        history = result.to_input_list()
        cl.user_session.set("history", history)

    except Exception as e:
            thinking.content = f"❌ Error: {e}"
            await thinking.update()
