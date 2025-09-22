# feedback_loop.py
from generator import generate_content
import os

# Ensure outputs folder exists
os.makedirs("outputs", exist_ok=True)

def feedback_cycle(goal: str, feedback_list: list):
    """
    Generate initial content and refine it iteratively based on feedback.
    
    :param goal: Initial content goal (story, ad, podcast)
    :param feedback_list: List of feedback strings to refine content
    :return: final content after all feedback iterations
    """
    print(f"=== Generating initial content for goal: {goal} ===\n")
    content = generate_content(goal)
    print("Initial Content:\n")
    print(content)
    print("\n" + "="*50 + "\n")

    # Save initial content
    with open("outputs/story_initial.md", "w", encoding="utf-8") as f:
        f.write(content)
    
    # Apply feedback iteratively
    for idx, fb in enumerate(feedback_list, start=1):
        print(f"--- Applying Feedback {idx}: {fb} ---\n")
        content = generate_content(goal, feedback=fb)
        print("Refined Content:\n")
        print(content)
        print("\n" + "="*50 + "\n")

        # Save each refined version
        with open(f"outputs/story_feedback{idx}.md", "w", encoding="utf-8") as f:
            f.write(content)
    
    return content

if __name__ == "__main__":
    # Example usage
    goal = "Write a 3-part sci-fi story series outline"
    feedbacks = [
        "Make it more emotional",
        "Add a cliffhanger at the end of each part",
        "Include a humorous side character"
    ]
    
    final_content = feedback_cycle(goal, feedbacks)
