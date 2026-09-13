import tiktoken

def count_tokens(text: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))

short_prompt = "Classify this support message and write a reply."
print("Short prompt tokens:", count_tokens(short_prompt))