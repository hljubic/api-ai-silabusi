from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import time
import pandas as pd

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key and assistant ID
openai.api_key = os.getenv("API_KEY")
assistant_id = os.getenv("ASSISTANT_ID")

def create_thread():
    """Create a thread for conversation."""
    thread = openai.beta.threads.create()
    return thread.id

def submit_message(thread_id, user_message):
    """Submit a message to the thread."""
    openai.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_message
    )

def run_assistant(thread_id):
    """Run the assistant and get a response."""
    run = openai.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )
    return run.id

def check_status(run_id, thread_id):
    """Check the status of the run."""
    run = openai.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
    return run.status

def get_response(thread_id):
    """Retrieve messages from the thread."""
    response = openai.beta.threads.messages.list(thread_id=thread_id, order="asc")
    return response.data[-1].content[0].text.value if response.data else None

@app.route('/ask', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    thread_id = request.json.get("thread_id", "")

    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    # Create a new conversation thread
    if not thread_id:
        thread_id = create_thread()

    # Submit user message to the thread
    submit_message(thread_id, user_input)

    # Run the assistant
    run_id = run_assistant(thread_id)

    # Wait for the response to complete
    status = check_status(run_id, thread_id)
    while status != "completed":
        time.sleep(1)  # Wait before checking again
        status = check_status(run_id, thread_id)

    # Get and return the assistant's response
    response = get_response(thread_id)
    '''
    # Get the client's IP address, considering proxies
    if request.headers.getlist("X-Forwarded-For"):
        ip_address = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip_address = request.remote_addr
    '''

    #df = pd.DataFrame({"user_input": user_input, "response": response, "thread_id": thread_id, "ip_address": 'test'})
    #df.to_csv('data/log.csv', index=False)

    return jsonify({"response": response, "thread_id": thread_id})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
