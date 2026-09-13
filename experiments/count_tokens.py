import tiktoken

def count_tokens(text: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))

customer_message = "I ordered a wireless keyboard last week. It has not arrived, and I need it before Friday for work. Can you tell me what to do?"

prompt_a = """Classify this support message and write a reply.
Return exactly this JSON:
{
"category": "...",
"urgency": "...",
"reply": "..."
}

Customer message: """ + customer_message

prompt_b = """You are a customer-support assistant for an online electronics store.
Task:
1. Classify the message into one category: delivery_delay, damaged_item, return_request, billing_issue, or other.
2. Identify urgency as low, medium, or high.
3. Draft a helpful reply of 80 words or fewer.
Rules:
- Do not invent an order status, delivery date, refund, or policy.
- Acknowledge the customer's Friday deadline.
- Ask for the order number if needed.
- Use calm, professional language.
Return exactly this JSON:
{
"category": "...",
"urgency": "...",
"reply": "..."
}

Customer message: """ + customer_message

print("Prompt A input tokens:", count_tokens(prompt_a))
print("Prompt B input tokens:", count_tokens(prompt_b))

output_a = """{
"category": "Shipping Delay",
"urgency": "High",
"reply": "I'm sorry to hear your keyboard hasn't arrived yet, especially with your Friday deadline. Let me look into this for you right away. Could you share your order number so I can check the current shipping status? Once I have that, I'll let you know the best way to get this resolved before Friday."
}"""

output_b = """{
"category": "delivery_delay",
"urgency": "high",
"reply": "Thank you for reaching out, and I'm sorry your keyboard hasn't arrived yet. I understand you need it before Friday, and I want to help you meet that deadline. I don't have your current shipping status on hand, so could you please share your order number? Once I have it, I'll check the tracking details and let you know the best next steps."
}"""

print("Prompt A output tokens:", count_tokens(output_a))
print("Prompt B output tokens:", count_tokens(output_b))