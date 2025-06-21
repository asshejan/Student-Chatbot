import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# 1. Get the API key from the environment
# Make sure to create a .env file with your OPENROUTER_API_KEY
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# 2. Set up the OpenAI client to use OpenRouter
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

# 3. Define the chat history with a system prompt
# The prompt is from the task description.
history = [
    {"role": "system", "content": "You are a helpful, accurate medical tutor."},
]

def chat():
    """
    Main function to run the chatbot in the terminal.
    """
    print("Chatbot initialized. Type 'quit' or 'exit' to end the session.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit"]:
                print("Ending chat session. Goodbye!")
                break

            # Add user message to history
            history.append({"role": "user", "content": user_input})

            # 4. Get the chat completion from OpenRouter
            completion = client.chat.completions.create(
                model="mistralai/mistral-7b-instruct:free", # As per requirements
                messages=history,
                # The task requires markdown formatting where needed.
                # The model should handle this based on the prompt.
            )

            # 5. Get the response and add it to history
            if completion.choices:
                response = completion.choices[0].message.content
                history.append({"role": "assistant", "content": response})
                print(f"Chatbot: {response}")
            else:
                print("Chatbot: I didn't get a response. Please try again.")

        except KeyboardInterrupt:
            print("\nEnding chat session. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    chat() 