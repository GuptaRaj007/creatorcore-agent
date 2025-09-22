# demo.py
from feedback_loop import feedback_cycle
from image_gen import generate_poster
from viz import create_story_arc
import os

# Ensure output folders exist
os.makedirs("outputs", exist_ok=True)
os.makedirs("assets/thumbnails", exist_ok=True)

# 1️⃣ Define story goal and feedback
goal = "Write a 3-part sci-fi story series outline"
feedbacks = [
    "Make it more emotional",
    "Add a cliffhanger at the end of each part",
    "Include a humorous side character"
]

# 2️⃣ Generate story with feedback
print("=== Generating story with feedback loop ===")
final_content = feedback_cycle(goal, feedbacks)

# Save final story to file
final_story_path = os.path.join("outputs", "story_final.md")
with open(final_story_path, "w", encoding="utf-8") as f:
    f.write(final_content)
print(f"Final story saved at {final_story_path}\n")

# 3️⃣ Generate poster
print("=== Generating poster ===")
poster_path = generate_poster(final_content)
print(f"Poster saved at {poster_path}\n")

# 4️⃣ Generate story arc
print("=== Generating story arc ===")
story_parts = ["Part 1: Beginning", "Part 2: Conflict", "Part 3: Resolution"]
arc_path = create_story_arc(story_parts)
print(f"Story arc saved at {arc_path}\n")

print("=== Demo Complete! ===")
print(f"Check outputs in 'outputs/' and poster in 'assets/thumbnails/'")
