# image_gen.py
from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the folder exists
os.makedirs("assets/thumbnails", exist_ok=True)

def generate_poster(summary_text: str, filename: str = "poster.png"):
    """
    Generates a simple poster image with story summary text.
    """
    width, height = 512, 512
    img = Image.new("RGB", (width, height), color=(30, 30, 60))  # dark sci-fi background
    draw = ImageDraw.Draw(img)

    # Simple text in center
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except:
        font = ImageFont.load_default()

    # Use textbbox instead of textsize
    bbox = draw.textbbox((0, 0), summary_text[:200]+"...", font=font)
    text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]

    draw.text(
        ((width - text_w) / 2, (height - text_h) / 2),
        summary_text[:200] + "...",
        font=font,
        fill=(255, 255, 255)
    )

    path = os.path.join("assets/thumbnails", filename)
    img.save(path)
    print(f"Poster saved at {path}")
    return path

if __name__ == "__main__":
    summary = "3-part sci-fi story about a robot learning human emotions"
    generate_poster(summary)
