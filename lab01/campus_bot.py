import os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()
MODEL = os.getenv("LLM_MODEL")

with open("lab01/facts.md", "r", encoding="utf-8") as f:
    facts = f.read()

system_prompt = f"""You are the Campus Info Bot for the Department of Computer Science.

FACTS (Your only source of knowledge):
{facts}

RULES (Performance Measure & Actuator Limits):
1. Answer questions ONLY using the FACTS provided above.
2. If the answer is not in the FACTS, say "I don't have that information" and direct the student to the General Office (Room 101) or cs-admin@ug.edu.gh. Do NOT guess.
3. You can ONLY provide text information. You cannot register students for courses, book appointments, or modify records. If asked to perform an action, explain that you cannot do it and tell them which office to visit.
4. Keep answers short, clear, and polite.
"""

messages = [{"role": "system", "content": system_prompt}]

print("Campus Info Bot ready! Type 'quit' to exit.\n")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "quit":
        break
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})
    resp = completion(model=MODEL, messages=messages, temperature=0)
    reply = resp.choices[0].message.content
    print(f"Bot: {reply}\n")
    messages.append({"role": "assistant", "content": reply})