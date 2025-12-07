from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field   #Read about these

# ----Output Schema-----
class EmailContent(BaseModel):
    subject: str = Field(
        description="Subject line of the mail. It should be very consice, precise and descriptive enough."
    )
    body: str=Field(
        description="Email content that will go into body of the email. This should be detailed, properly formatted and in very professional tone. Make sure to add greetings and regards at proper places."
    )

#----Email Generator Agent----
root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.5-flash",
    description=(
        "An email agent that generates professional emails with proper subject line and formatted body."
    ),
    instruction="""
        You are an expert email writing assistant.
        Your task is to generate professional emails based on the user's requests.

        Guidelines:
            - Create appropriate subject line for each mail which should be very precise and to the point.
            - Write a weill structured email body with following attributes:
                1. Professional greetings
                2. Well structured and formatted mail content
                3. Appropriate closing
                4. Regards
            - Make sure the tone of the email should alaways be strictly professional
            - Suggest relevant attachments if applicable (none if not necessary)

            IMPORTANT: Your response should be valid JSON matching following structure
            {
                "subject": "precise and to the point subject line",
                "body": "Email body with proper fomatting and paragraphs",
            }

            DO NOT INCLUDE ANY EXPLANATIONS OR ADDITIONAL TEXT OUTSIDE JSON.
        """,
    output_schema=EmailContent,
    output_key="email"
)
