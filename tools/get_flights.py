from agents import function_tool
from typing_extensions import TypedDict  # ✅ Use typing_extensions for Python < 3.12

class FlightData(TypedDict):
    departure: str
    destination: str
    date: str

@function_tool
async def get_flights(input: FlightData) -> dict:
    departure = input["departure"]
    destination = input["destination"]
    date = input["date"]  # ✅ Corrected key

    flights = [
        {"airline": "Air Blue", "departure time": "08:00 AM", "arrival time": "10:00 AM", "price": "30000 PKR"},
        {"airline": "PIA", "departure time": "10:00 AM", "arrival time": "7:00 PM", "price": "80000 PKR"},
        {"airline": "Shaheen Airline", "departure time": "02:00 PM", "arrival time": "5:00 PM", "price": "25000 PKR"}
    ]

    return {
        "flights": flights,  # ✅ Corrected variable name
        "route": f"{departure} -> {destination}",
        "date": date
    }
