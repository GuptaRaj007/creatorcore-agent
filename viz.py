# viz.py
import matplotlib.pyplot as plt
import os

# Ensure folder exists
os.makedirs("outputs", exist_ok=True)

def create_story_arc(parts: list, title: str = "Story Arc"):
    """
    Creates a simple story arc visualization.
    :param parts: List of part names or plot points
    """
    points = list(range(1, len(parts) + 1))  # simple Y-axis progression
    plt.figure(figsize=(8, 4))
    plt.plot(parts, points, marker='o', color='cyan', linewidth=2)
    plt.title(title)
    plt.xlabel("Story Part")
    plt.ylabel("Plot Progression")
    plt.grid(True)

    output_path = os.path.join("outputs", "story_arc.png")
    plt.savefig(output_path)
    plt.show()
    print(f"Story arc saved at {output_path}")
    return output_path

if __name__ == "__main__":
    story_parts = ["Part 1: Beginning", "Part 2: Conflict", "Part 3: Resolution"]
    create_story_arc(story_parts)
