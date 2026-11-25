import csv, json, os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()
MODEL = os.getenv("LLM_MODEL")

def check_stock(item: str, strength: str = "") -> list[dict]:
    with open("data/pharmacy_stock.csv", newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if item.lower() in r["item"].lower()]
    if strength:
        rows = [r for r in rows if strength.lower() in r["strength"].lower()]
    return rows

TOOLS = {"check_stock": check_stock}
tool_schemas = [{
    "type": "function",
    "function": {
        "name": "check_stock",
        "description": "Look up pharmacy stock by medicine name and optional strength (e.g., '500mg').",
        "parameters": {
            "type": "object",
            "properties": {
                "item": {"type": "string", "description": "Name of the medication"},
                "strength": {"type": "string", "description": "Dosage strength, e.g., 500mg"}
            },
            "required": ["item"]
        }
    }
}]

messages = [{"role": "user", "content": "Do we have amoxicillin 500mg?"}]
resp = completion(model=MODEL, messages=messages, tools=tool_schemas, temperature=0)

msg = resp.choices[0].message
messages.append(msg.model_dump())

for tc in msg.tool_calls or []:
    args = json.loads(tc.function.arguments)
    result = TOOLS[tc.function.name](**args)
    messages.append({
        "role": "tool",
        "tool_call_id": tc.id,
        "content": json.dumps(result)
    })

final_resp = completion(model=MODEL, messages=messages, tools=tool_schemas, temperature=0)
print(final_resp.choices[0].message.content)