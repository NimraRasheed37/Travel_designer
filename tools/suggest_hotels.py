from agents import function_tool
from typing_extensions import TypedDict

class HotelData(TypedDict):
    city: str
    budget: str

@function_tool
async def suggest_hotels(input: HotelData) -> dict:
    city = input["city"]
    budget = input["budget"].lower().strip()
    
    budget_ranges = {
        "low": "3000 - 5000 PKR per night",
        "medium": "6000 - 9000 PKR per night",
        "high": "10000 - 15000 PKR per night",
    }
    
    mock_hotels = {
        "low": [
            {"name": "Safa Inn", "price_per_night": "PKR 11,200", "rating": "3.5"},
            {"name": "Lahore Backpackers Hostel", "price_per_night": "PKR 9,800", "rating": "4.0"}
        ],
        "medium": [
            {"name": "Comfort Residency", "price_per_night": "PKR 22,400", "rating": "4.2"},
            {"name": "Urban Suites Islamabad", "price_per_night": "PKR 26,600", "rating": "4.3"}
        ],
        "high": [
            {"name": "Serena Hotel Islamabad", "price_per_night": "PKR 56,000", "rating": "4.8"},
            {"name": "Pearl Continental Karachi", "price_per_night": "PKR 70,000", "rating": "4.9"}
        ]
    }
    
    if budget not in mock_hotels:
        return {
            "message": (
                f"💬 Please choose a hotel budget range:\n"
                f"- `low` ({budget_ranges['low']})\n"
                f"- `medium` ({budget_ranges['medium']})\n"
                f"- `high` ({budget_ranges['high']})"
            )
        }
    
    return {
        "city": city,
        "budget_range": budget_ranges[budget],
        "hotels": mock_hotels[budget]
    }
    