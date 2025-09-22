# generator.py
from dotenv import load_dotenv
import os
from groq import Groq



load_dotenv()  # this will load variables from .env file


# Make sure you set your API key in environment variable:
#   setx GROQ_API_KEY "your_api_key_here"   (Windows PowerShell)
#   export GROQ_API_KEY="your_api_key_here" (Linux/Mac)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"


def generate_content(goal: str, feedback: str = None):
    """
    Generate content (story, ad, or podcast) based on goal.
    Optionally refine it with feedback.
    """
    base_prompt = f"You are CreatorCore Agent. Generate content for the goal: {goal}.\n"

    if feedback:
        base_prompt += f"Refine it based on this feedback: {feedback}\n"

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a creative content generation agent."},
            {"role": "user", "content": base_prompt}
        ],
        max_tokens=800,   # adjust if you need longer scripts
        temperature=0.8,  # creativity
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    # Example run
    goal = "Write a 3-part sci-fi story series outline"
    feedback = "Make it more emotional with a cliffhanger ending"
    content = generate_content(goal, feedback)
    print("Generated Content:\n")
    print(content)
