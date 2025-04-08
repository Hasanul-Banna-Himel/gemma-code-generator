import os
import google.generativeai as genai
import sys
import textwrap  

# --- Environment Setup ---
API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL_NAME = "gemma-3-27b-it"

# --- Core Generation Function ---
def generate_with_gemma(prompt_text: str):
    """
    Sends a prompt to the specified Gemma model and streams the response.

    Args:
        prompt_text: The input text prompt for the model.

    Returns:
        The full response text as a string, or None if an error occurred.
    """
    if not API_KEY:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please set the environment variable and try again.")
        sys.exit(1)  
    print("\nAttempting to generate code...")
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel(MODEL_NAME)

        generation_config = {
            "temperature": 0.2,
        }

        print(f"\n--- Gemma's Generated Code ({MODEL_NAME}) ---")
        
        response = model.generate_content(
            prompt_text,
            generation_config=generation_config,
            stream=True,
        )
        
        full_response = ""
        for chunk in response:
            if hasattr(chunk, 'text'):
                chunk_text = chunk.text
            elif hasattr(chunk, 'parts') and chunk.parts:
                chunk_text = chunk.parts[0].text
            else:
                chunk_text = str(chunk)
                
            print(chunk_text, end="", flush=True) 
            full_response += chunk_text
            
        print("\n--- End of Generation ---")
        return full_response

    except Exception as e:
        print(f"\nAn error occurred during generation: {e}")
        print("This could be due to API key issues, network problems, or model errors.")
        return None  


# --- Code Generator Specific Logic ---
def build_code_generation_prompt(description: str, language: str = "Python") -> str:
    prompt = f"""\
Generate {language} code based on the following description.
Please only output the code, enclosed in markdown code blocks (e.g., ```{language.lower()} ... ```).
Do not add any explanations before or after the code block unless the description explicitly asks for comments within the code.

Description:
{description}
"""
    return prompt

# --- Main Execution ---
if __name__ == "__main__":
    print("--- Gemma Code Generator ---")
    print("Describe the code you want me to generate (e.g., 'a function to check if a number is prime').")
    print("Press Enter when you are finished.")

    try:
        user_description = input("> ")
    except EOFError:
        print("\nNo input received. Exiting.")
        sys.exit(0)

    if user_description:
        target_language = "Python"  
        generation_prompt = build_code_generation_prompt(user_description, target_language)

        print("\nSending the following request to Gemma:")
        print("-----------------------------------------")
        print(textwrap.indent(generation_prompt, prefix="  "))
        print("-----------------------------------------")

        generated_code = generate_with_gemma(generation_prompt)

        if generated_code:
            print("\nCode generation process complete.")
    else:
        print("No description provided. Exiting.")