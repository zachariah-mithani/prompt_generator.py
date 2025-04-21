# Text-to-Image Prompt Generator

A Python application that generates detailed, creative prompts for text-to-image AI models (e.g., Stable Diffusion, DALL·E) using a pre-trained language model (GPT-2). Users input a basic idea (e.g., "a futuristic city"), and the app creates a vivid prompt for image generation.

## Features
- Generates descriptive prompts with a command-line interface (CLI).
- Saves prompts to a file (`generated_prompts.txt`).
- Uses Hugging Face's `transformers` library with GPT-2.

## Requirements
- Python 3.8+
- Dependencies: `transformers`, `torch`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-to-image-prompt-generator.git
   cd text-to-image-prompt-generator


Create a virtual environment (optional but recommended):python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate


Install dependencies:pip install -r requirements.txt



Usage

Run the script:python prompt_generator.py


Enter a basic idea (e.g., "a magical forest") when prompted.
View the generated prompt and find it saved in generated_prompts.txt.
Type quit to exit.

Example
Enter your idea: a futuristic city

Generated Prompt:
A sprawling futuristic city at twilight, with towering neon-lit skyscrapers, holographic billboards, and sleek flying cars weaving through the air. The mood is vibrant yet mysterious, with deep blues and purples dominating the sky, accented by warm orange lights. The style is hyper-detailed, cyberpunk-inspired, with a cinematic, slightly gritty aesthetic.

Prompt saved to generated_prompts.txt

Future Improvements

Add a web interface using Flask or Streamlit.
Support larger models (e.g., LLaMA) for better prompts.
Integrate with image generation APIs.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contributing
Contributions are welcome! Please open an issue or submit a pull request.```
