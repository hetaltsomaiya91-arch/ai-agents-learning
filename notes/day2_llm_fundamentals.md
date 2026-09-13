# Day 2 — LLM Fundamentals
## Tokens
Tokens are the small pieces of text an LLM processes. They matter because model limits and API costs are
measured in tokens, not words.
## Context windows
A context window is the amount of information a model can use in one request. It includes instructions,
conversation history, tool definitions/results, documents, and the output being generated. It is temporary
working memory, not the model’s training data.
## Embeddings
Embeddings are numeric vectors that represent semantic meaning. They are useful for finding related text,
such as retrieving relevant document chunks for a RAG application.
## Model limits
Important limits include context size, output size, rate limits, cost, and imperfect reliability. A model can
still hallucinate or make poor decisions, so applications need grounding, validation, tests, and human
approval for high-impact actions.
## What I learned from my prompt experiment
[Write 3–5 sentences comparing the short and detailed prompts. Include token counts and one example of an
output-quality difference.]
## Practical rule
Send the model only the instructions and context needed for the task. For large knowledge bases, retrieve
relevant information instead of placing everything in every prompt.