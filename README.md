# Student Tutor Chatbot

This is a FastAPI-based chatbot that acts as an educational tutor for students from Class 1 to Class 12. It uses free OpenRouter LLMs to provide helpful and accurate responses.

## Features

-   **FastAPI Backend**: A robust and modern web framework for building APIs.
-   **OpenRouter Integration**: Leverages free, instruction-following LLMs like `mistralai/mistral-7b-instruct:free`.
-   **In-Memory Chat History**: Supports session-based chat history without needing a database.
-   **Swagger UI**: Interactive API documentation for easy testing.
-   **Deployable on Render**: Ready for deployment with a `render.yaml` configuration.

## Deployment

This application is deployed on Render.

**Deployment Link**: [To be added after deployment]

## API Usage

The API has a single endpoint for interacting with the chatbot.

### Endpoint: `/chat`

-   **Method**: `POST`
-   **Description**: Sends a message to the chatbot and receives a response. Maintains a conversation history using a `session_id`.
-   **Request Body**:
    ```json
    {
      "session_id": "string",
      "message": "string"
    }
    ```
-   **Response Body**:
    ```json
    {
      "response": "string",
      "history": [
        {
          "role": "string",
          "content": "string"
        }
      ]
    }
    ```

### Example `curl` Request

```bash
curl -X POST "YOUR_DEPLOYMENT_URL/chat" \
-H "Content-Type: application/json" \
-d '{"session_id": "test-session-123", "message": "What is photosynthesis?"}'
```
Replace `YOUR_DEPLOYMENT_URL` with the actual deployment link from Render.

## Environment Variables

To run this application, you need to set up the following environment variable.

-   `OPENROUTER_API_KEY`: Your API key from [OpenRouter](https://openrouter.ai/).

Create a `.env` file in the root directory and add your key:

```
OPENROUTER_API_KEY=your_open_router_api_key
```

When deploying to Render, set this environment variable in the Render dashboard.

## Local Setup Guide

Follow these steps to run the application locally.

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/asshejan/Student-Chatbot.git
    cd Student-Chatbot
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables**:
    Create a `.env` file in the root directory and add your `OPENROUTER_API_KEY`. See [Environment Variables](#environment-variables) for details.

5.  **Run the application**:
    ```bash
    uvicorn app.main:app --reload
    ```

6.  **Access the API**:
    The API will be available at `http://127.0.0.1:8000`.
    -   **Swagger UI (for testing)**: `http://127.0.0.1:8000/docs`
    -   **API Endpoint**: `http://127.0.0.1:8000/chat` 