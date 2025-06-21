import os
from typing import Dict
from openai import OpenAI
from dotenv import load_dotenv
from app.models import ChatRequest, ChatResponse, Message

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# In-memory session chat history: {session_id: [messages]}
session_histories: Dict[str, list] = {}

SYSTEM_PROMPT = "You are a helpful, accurate medical tutor."


def get_chat_response(request: ChatRequest) -> ChatResponse:
    # Get or create session history
    history = session_histories.setdefault(request.session_id, [
        {"role": "system", "content": SYSTEM_PROMPT}
    ])

    # Add user message
    history.append({"role": "user", "content": request.message})

    # Call OpenRouter LLM
    completion = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct:free",
        messages=history,
    )

    if completion.choices:
        response = completion.choices[0].message.content
        history.append({"role": "assistant", "content": response})
    else:
        response = "Sorry, I didn't get a response. Please try again."
        history.append({"role": "assistant", "content": response})

    # Prepare history for response (excluding system prompt)
    response_history = [
        Message(role=msg["role"], content=msg["content"])
        for msg in history if msg["role"] != "system"
    ]

    return ChatResponse(
        response=response,
        history=response_history
    ) 