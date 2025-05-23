
import importlib.metadata  # To check the version of installed packages
import tiktoken  # Tokenizer library from OpenAI

# Optional: Check and print the version of the tiktoken package
print("tiktoken version:", importlib.metadata.version("tiktoken"))

# Load the GPT-4 tokenizer (same used in GPT-3.5)
tokenizer = tiktoken.get_encoding("cl100k_base")

# ✅ Simple text example with a special token
text = "Hello, do you like tea? <|endoftext|> In the sunlit terraces of the palace."

# Tokenize the input text
tokens = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print("Token IDs:", tokens)

# Decode the tokens back into a string
decoded_text = tokenizer.decode(tokens)
print("Decoded Text:", decoded_text)

  
