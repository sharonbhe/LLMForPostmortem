import json # Imports the json module for working with JSON data.
import os # Imports the os module for interacting with the operating system, like accessing environment variables.
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Initializes the OpenAI client with an API key retrieved from environment variables.

def load_logs(filename):
    with open(filename, 'r') as f:
        logs = json.load(f)
    return sorted(logs, key=lambda x: x['timestamp']) # Sorts the logs by timestamp and returns them.

def format_logs(logs):    
    # Formats each log entry to show time and message, then joins them with newlines.    
    return '\n'.join([f"- {log['timestamp'][11:16]}: {log['message']}" for log in logs])

def build_prompt(timeline):
    return f"""You are an SRE helping document a production incident.

Here is the incident timeline:
{timeline}

Please generate a structured postmortem with:
- Summary
- Timeline
- Root cause
- Affected systems
- Action items
"""

def call_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o", # Specifies the OpenAI model to use.
        messages=[{"role": "user", "content": prompt}], # Sets the user message for the API call.
        temperature=0.3 # Sets the creativity/randomness of the response.
    )
    return response.choices[0].message.content

def main():
    logs = load_logs("logs.json") # Loads logs from 'logs.json'.
    timeline = format_logs(logs) # Formats the loaded logs into a timeline string.
    prompt = build_prompt(timeline) # Builds the prompt for OpenAI using the timeline.
    postmortem = call_openai(prompt) # Calls OpenAI to generate the postmortem.

    with open("output.md", "w") as f: # Opens 'output.md' in write mode.
        f.write(postmortem)

    print("Postmortem written to output.md")

if __name__ == "__main__":
    # Ensures that main() is called only when the script is executed directly,
    # not when imported as a module.
    main()
