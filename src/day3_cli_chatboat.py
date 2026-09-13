import os
from collections import deque
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
MODEL = "gpt-4.1-mini"
MAX_HISTORY_MESSAGES = 5
SYSTEM_INSTRUCTIONS = """
You are LearningBot, a helpful AI tutor for someone learning AI agents and automation.
- Be clear, practical, and concise.
- If you are uncertain, say so instead of inventing facts.
- Use short examples when they help.
"""


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing. Add it to your .env file.")
    return OpenAI(api_key=api_key)


def main() -> None:
    client = get_client()
    history: deque[dict[str, str]] = deque(maxlen=MAX_HISTORY_MESSAGES)
    print("LearningBot is ready. Type exit or quit to stop.")
    print("The bot keeps the last 5 messages of conversation history.\n")

    while True:
        user_text = input("You: ").strip()

        if user_text.lower() in {"exit", "quit"}:
            print("LearningBot: Goodbye. Keep building!")
            break

        if not user_text:
            print("LearningBot: Please type a question.")
            continue

        history.append({"role": "user", "content": user_text})

        try:
            response = client.responses.create(
                model=MODEL,
                instructions=SYSTEM_INSTRUCTIONS,
                input=list(history),
            )
            assistant_text = response.output_text
        except Exception as error:
            history.pop()
            print(f"LearningBot: Request failed: {error}")
            continue

        history.append({"role": "assistant", "content": assistant_text})
        print(f"LearningBot: {assistant_text}\n")
        print(f"[History currently stores {len(history)}/{MAX_HISTORY_MESSAGES} messages]\n")


if __name__ == "__main__":
    main()