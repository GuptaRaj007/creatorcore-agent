# CreatorCore Agent

## Overview
**CreatorCore Agent** is a Reinforcement Learning-enhanced generative agent that can:
- Generate stories, ads, or podcast outlines based on user-defined content goals.
- Refine generated content using feedback loops (e.g., “make it more emotional”, “add cliffhanger”).
- Generate a poster/thumbnail image and visualize a narrative arc/timeline.
- Export results in Markdown, PNG, and optionally JSON/CSV formats.

This project was developed as part of an internship test task.

---

## Features
1. **Story/Script Generation**
   - Generates 3-part story series, short video ads, or podcast outlines.
   - Uses **LLAMA 3.3 70B Versatile** LLM backend for text generation.

2. **Feedback Loop**
   - Iteratively refines content based on user feedback.
   - Feedback tokens examples:
     - `emotional depth ++`
     - `add cliffhanger`
     - `include humor`

3. **Poster/Thumbnail Generation**
   - Generates a simple poster using PIL (can be upgraded to AI-generated images with Stable Diffusion or DALL·E).

4. **Story Arc / Timeline**
   - Visualizes story progression using Matplotlib.

5. **Demo Script**
   - `demo.py` generates the story, poster, and story arc sequentially for easy demonstration.

---

## Project Structure

```

creatorcore-agent/
├── generator.py          # Generates initial content using LLAMA 3.3
├── feedback\_loop.py      # Iteratively refines content based on feedback
├── image\_gen.py          # Generates poster/thumbnail image
├── viz.py                # Generates story arc/timeline visualization
├── demo.py               # Runs full demo: story + poster + arc
├── outputs/              # Saved story scripts and timeline image
│   ├── story\_initial.md
│   ├── story\_feedback1.md
│   ├── story\_feedback2.md
│   ├── story\_feedback3.md
│   ├── story\_final.md
│   └── story\_arc.png
├── assets/
│   └── thumbnails/
│       └── poster.png
└── README.md

````

---

## How to Run

1. **Generate Story with Feedback Loop**
```bash
python feedback_loop.py
````

2. **Generate Poster / Thumbnail**

```bash
python image_gen.py
```

3. **Generate Story Arc / Timeline**

```bash
python viz.py
```

4. **Run Full Demo**

```bash
python demo.py
```

> All outputs are saved in the `outputs/` and `assets/thumbnails/` folders.

---

## Learning Note (200–300 words)

During this assignment, I developed a generative agent capable of producing stories, ads, and podcast outlines. The project taught me how to combine **LLM-based content generation** with a **feedback-driven refinement loop**, enabling iterative improvement of generated content based on natural language feedback. I learned how to define feedback tokens (e.g., `make it more emotional`, `add cliffhanger`) and apply them programmatically to guide the model’s outputs.

I also implemented a **poster/thumbnail generator** using PIL to visually represent content, along with a **story arc visualizer** using Matplotlib to map narrative progression. While placeholder methods were used for image generation, the architecture supports integration with AI image generators such as Stable Diffusion or DALL·E.

This project reinforced key concepts in **Reinforcement Learning**, **prompt engineering**, and **multi-modal content generation**, while also emphasizing clean project structure and automation of outputs. By saving content, images, and timelines in organized directories, the agent now produces fully exportable deliverables suitable for GitHub demos or further integration into video production pipelines.

Overall, this task provided practical experience in building a **full-stack generative content pipeline**, combining text, image, and visualization, while emphasizing iterative refinement based on human-like feedback.

---

## Notes

* The project currently uses **PIL** for poster generation; it can be upgraded to AI-generated posters later.
* The LLM model used is **LLAMA 3.3 70B Versatile**.
* Video export functionality is optional and can be added in future iterations.

---

## Demo / Bonus

* `demo.py` script demonstrates the full pipeline:

  1. Generates story with feedback
  2. Creates poster/thumbnail
  3. Generates story arc visualization
* This serves as a **mini interactive demo** for your internship submission.

---

## Deliverables

1. **GitHub Repository** with all scripts and README.md
2. **Story Files** (`outputs/`):

   * `story_initial.md`
   * `story_feedback1.md` … `story_feedbackN.md`
   * `story_final.md`
3. **Poster Image** (`assets/thumbnails/poster.png`)
4. **Story Arc Image** (`outputs/story_arc.png`)
5. **Demo Script** (`demo.py`) to show full workflow
6. **Learning Note** (included in README.md)

> To submit: Upload the **entire repository** to GitHub and share the link with your internship supervisor. Ensure all output folders (`outputs/`, `assets/thumbnails/`) contain at least one generated file to demonstrate functionality.

```

---

This README now:

- Matches your **assignment requirements**
- Lists all **deliverables**
- Explains **how to run scripts**
- Includes a **demo script for easy review**
- Includes **learning note**

---

If you want, I can **also prepare a quick checklist of what to include in the GitHub repo** so your submission is perfect.  

Do you want me to do that?
```
