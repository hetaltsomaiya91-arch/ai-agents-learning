# Day 2 — Prompt Comparison Experiment

**Model/Provider used:** Claude (Anthropic), Claude Sonnet 5
**Task:** Run the same customer message through a short prompt and a detailed prompt, without changing the task between tests.

## Test task — customer message (identical for both tests)

> I ordered a wireless keyboard last week. It has not arrived, and I need it before Friday for work. Can you tell me what to do?

---

## Prompt A — short

**Prompt text:**
```
Classify this support message and write a reply.
Return exactly this JSON:
{
"category": "...",
"urgency": "...",
"reply": "..."
}
```

**Output:**
```json
{
"category": "Shipping Delay",
"urgency": "High",
"reply": "I'm sorry to hear your keyboard hasn't arrived yet, especially with your Friday deadline. Let me look into this for you right away. Could you share your order number so I can check the current shipping status? Once I have that, I'll let you know the best way to get this resolved before Friday."
}
```

---

## Prompt B — detailed

**Prompt text:**
```
You are a customer-support assistant for an online electronics store.
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
```

**Output:**
```json
{
"category": "delivery_delay",
"urgency": "high",
"reply": "Thank you for reaching out, and I'm sorry your keyboard hasn't arrived yet. I understand you need it before Friday, and I want to help you meet that deadline. I don't have your current shipping status on hand, so could you please share your order number? Once I have it, I'll check the tracking details and let you know the best next steps."
}
```

---

## Record your observations

| Dimension | Prompt A — short | Prompt B — detailed |
|---|---|---|
| Follows task correctly | Partial — returns valid JSON but invents its own category label instead of using a fixed taxonomy | Yes — follows all 3 numbered steps and matches the exact JSON format |
| Correct category | No — "Shipping Delay" isn't part of any defined category set | Yes — "delivery_delay" matches the required enum |
| Recognizes urgency | Yes, but inconsistent casing/scale ("High" with no defined levels) | Yes — "high", matches the defined low/medium/high scale |
| Avoids invented facts | Mostly — doesn't state a false delivery date, but implies a resolution path isn't guaranteed | Yes — explicitly states it doesn't have the shipping status, no invented details |
| Output format predictable | Lower — category wording/casing will vary between runs | Higher — enum-constrained and structurally consistent every run |
| Useful to a business workflow | Low — can't be reliably routed/logged without a fixed taxonomy | High — category and urgency map directly to ticket routing and priority queues |
| Input tokens | *(run `count_tokens.py` for exact number)* | *(run `count_tokens.py` for exact number)* |
| Output tokens | *(run `count_tokens.py` for exact number)* | *(run `count_tokens.py` for exact number)* |
| Overall rating (1–5) | 2 | 5 |

---

## Expected lesson

The detailed prompt (Prompt B) produces a more constrained, repeatable output because it defines the exact category taxonomy, an explicit urgency scale, a word limit, and guardrails against inventing information. It costs more input tokens upfront, but that cost buys consistency — which matters most when the output feeds into an automated workflow rather than being read once by a human. Better prompting isn't "always write more" — it's choosing the smallest amount of context and instruction that reliably produces the result the task actually needs.