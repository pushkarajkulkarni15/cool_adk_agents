from google.adk.agents import Agent

def get_distance(src: str, dest: str) -> dict:
    """
    Return distance between source city and destination city along with weather information.
    """
    if src.lower() == "pune" and dest.lower() == "mumbai":
        return {
            "status": "success",
            "response": ("The distance between Pune and Mumbai is 100 km and the weather is sunny."),
        }
    else:
        return {
            "status": "error",
            "response": ("Sorry, do not have the information for this route."),
        }

def get_restaurants(city: str) -> dict:
    """
    Return list of restaurants in the city.
    """
    if city.lower() == "pune":
        return {
            "status": "success",
            "response": "The list of restaurants in Pune is: Jogeshwari Misal,Camp Burger, Durvankur.",
        }
    else:
        return {
            "status": "error",
            "response": "Sorry, do not have the information for this city.",
        }

root_agent = Agent(
    name="travel_advisor",
    model="gemini-2.5-flash",
    description=("A travel advisor agent that can help you plan your trip between the entered cities with weather information and restraurant suggestions."),
    instruction=("You are a travel advisor agent that can help you plan your trip between the entered cities with weather information and restraurant suggestions."),
    tools=[get_distance, get_restaurants]
)