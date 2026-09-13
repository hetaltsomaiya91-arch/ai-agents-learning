from collections import deque
MAX_HISTORY_MESSAGES = 5
history = deque(maxlen=MAX_HISTORY_MESSAGES)
print("History demo. Type exit to stop.")

while True:
    user_text = input("You: ").strip()
    if user_text.lower() == "exit":
        break
    history.append({"role": "user", "content": user_text})
    fake_reply = f"I received: {user_text}"
    history.append({"role": "assistant", "content": fake_reply})
    print(f"Bot: {fake_reply}")
    print("Stored history:")
    for message in history:
        print(message)