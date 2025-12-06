from google.adk.agents import LlmAgent
from google.genai import types

def generate_niche_ideas(channel_type: str, no_of_ideas: int) -> list:
    """
    Generate tailored ideas for youtube videos based on the channel niche provided.

    Args:
        channel_niche: str - The primary topic of the channel for which the ideas are to be generated.
        no_of_ideas: int - The number of ideas to be generated.

    Returns:
        list - A list of ideas for youtube videos.

    """

    ideas = []

    if "technology" in channel_type.lower():
        ideas =  [
            "Idea 1",
            "Idea 2",
            "Idea 3",
        ]
    elif "entertainment" in channel_type.lower():
        ideas = [
            "Idea 1",
            "Idea 2",
            "Idea 3",
        ]
    else:
        ideas = []

    return ideas[:no_of_ideas]

def get_channel_optimization_tips(channel_type: str) -> dict:
    """
    Based on the channel type provided, return tips for increasing engagement on the channel, also suggest SEO reccomnedations and adivses to improve content discovery. 
    
    Args:
        channel_type: str - The type of the channel for which the optimization tips are to be generated.

    Returns:
        dict - A dictionary containing the optimization tips for the channel.

    """
    
    if "technology" in channel_type.lower():
        return {
            "status": "success",
            "response": "technology recommondations",
        }
    elif "entertainment" in channel_type.lower():
        return {
            "status": "success",
            "response": "entertainment recommondations",
        }
    
    else:
        return {
            "status": "error",
            "response": "Sorry, do not have the information for this channel type.",
        }

root_agent = LlmAgent(
    name="youtube_creator_assistant",
    model="gemini-2.5-flash",
    description=("An AI assistant that can help creators generate best ideas for their youtube videos and also help opitmize thier channels."),
    instruction=("You are most creative assistant with expertise in youtube content creation and optimization. Generate idea based on channel niche and also help optimize the channel. Advise should include SEO, engagement and content strategy."),
    tools=[generate_niche_ideas, get_channel_optimization_tips],
    generate_content_config=types.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=400
    )
)


