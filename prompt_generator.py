```python
from transformers import pipeline
import re

def initialize_model():
    """Initialize the GPT-2 model for text generation."""
    try:
        generator = pipeline("text-generation", model="gpt2", device=-1)  # Use GPU if available
        return generator
    except Exception as e:
        print(f"Error initializing model: {e}")
        return None

def generate_prompt(generator, user_input, max_length=100):
    """Generate a detailed prompt based on user input."""
    if not generator:
        return "Model not initialized."
    
    # Craft a meta-prompt to guide the model
    meta_prompt = (
        f"Create a detailed, creative prompt for a text-to-image AI based on the idea: '{user_input}'. "
        "The prompt should be vivid, descriptive, and include specific details like setting, mood, colors, and style. "
        "Keep it under 100 words."
    )
    
    try:
        # Generate the prompt
        output = generator(
            meta_prompt,
            max_length=max_length,
            num_return_sequences=1,
            temperature=0.9,  # Controls creativity
            top_p=0.95,      # Nucleus sampling for diversity
            do_sample=True
        )[0]["generated_text"]
        
        # Clean up the output
        prompt = output.replace(meta_prompt, "").strip()
        prompt = re.sub(r"\s+", " ", prompt)  # Normalize whitespace
        return prompt[:500]  # Limit length for practicality
    except Exception as e:
        return f"Error generating prompt: {e}"

def save_prompt(prompt, filename="generated_prompts.txt"):
    """Save the generated prompt to a file."""
    try:
        with open(filename, "a") as f:
            f.write(f"{prompt}\n\n")
        print(f"Prompt saved to {filename}")
    except Exception as e:
        print(f"Error saving prompt: {e}")

def main():
    print("Text-to-Image Prompt Generator")
    print("Enter a basic idea (e.g., 'a futuristic city') or 'quit' to exit.")
    
    # Initialize the model
    generator = initialize_model()
    if not generator:
        print("Exiting due to model initialization failure.")
        return
    
    while True:
        user_input = input("\nEnter your idea: ").strip()
        if user_input.lower() == "quit":
            break
        
        if not user_input:
            print("Please enter a valid idea.")
            continue
        
        # Generate and display the prompt
        prompt = generate_prompt(generator, user_input)
        print("\nGenerated Prompt:")
        print(prompt)
        
        # Save the prompt
        save_prompt(prompt)
        
        print("\nEnter another idea or 'quit' to exit.")

if __name__ == "__main__":
    main()
```