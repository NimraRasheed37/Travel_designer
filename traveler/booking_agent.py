from agents import Agent
from config import model
from tools.get_flights import get_flights
from tools.suggest_hotels import suggest_hotels

booking_agent = Agent(
    name="BookingAgent",
    instructions="""
You help users book travel.

Responsibilities:
- Ask where and when the user wants to travel.
- Use tools to suggest flights and hotels.
- Let the user pick one and confirm their choices.

Tone: Efficient, helpful, polite.
""",
    model=model,
    tools=[get_flights, suggest_hotels]
)
