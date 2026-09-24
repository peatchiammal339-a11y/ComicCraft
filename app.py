import os
from google import genai
from google.genai import types

# Initialize Gemini Client (Uses GEMINI_API_KEY environment variable)
client = genai.Client()

def generate_comic_story(prompt: str) -> str:
    """Generates a panel-by-panel comic story script using Gemini 2.5 Flash."""
    
    system_instruction = (
        "You are 'ComicCraft', an AI comic book writer. "
        "Create a detailed comic story script based on the user prompt. "
        "Structure the output into Panels (Panel 1, Panel 2, etc.) with: "
        "1. Visual Description (Illustration details for the artist) "
        "2. Dialogue (Character speech bubbles) "
        "3. Narrative Box (Story background/caption box)"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.7,
        )
    )
    return response.text

if __name__ == "__main__":
    print("==================================================")
    print("   Welcome to ComicCraft: AI Comic Story Creator  ")
    print("==================================================\n")
    
    user_prompt = input("Enter your comic story idea or theme: ")
    
    if user_prompt.strip():
        print("\nCreating your comic script using Gemini... Please wait.\n")
        try:
            comic_script = generate_comic_story(user_prompt)
            print("---------------- YOUR COMIC SCRIPT ----------------\n")
            print(comic_script)
            print("---------------------------------------------------")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Tip: Make sure you have set the GEMINI_API_KEY environment variable.")
    else:
        print("Story prompt cannot be empty!")
