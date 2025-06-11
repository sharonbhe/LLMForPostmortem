# LLM-Generated Postmortems from Incident Logs

This is a simple Python tool that uses OpenAI’s GPT-4 to generate structured, readable postmortem reports from incident logs. The goal is to help engineering teams save time and create higher-quality documentation after on-call incidents or service disruptions.

# What It Does

- Takes a structured JSON log file with simulated incident events
- Extracts a timeline of what happened
- Uses an LLM to generate a postmortem summary with:
  - Summary
  - Timeline
  - Root cause
  - Affected systems
  - Action items
- Outputs a clean `output.md` file you can copy into a different tool
---

# How to Run
git clone https://github.com/sharonbhe/LLMForPostmortem
cd LLMForPostmortem
python3 -m venv .venv
source .venv/bin/activate
pip install openai
export OPENAI_API_KEY=your_key_here
python postmortem_generator.py
