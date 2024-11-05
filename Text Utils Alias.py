# main.py

import text_utils as tu

sample_text = "text Utility!"

reversed_text = tu.reverse_string(sample_text)
capitalized_text = tu.capitalize_string(sample_text)
uppercase_text = tu.uppercase_string(sample_text)
lowercase_text = tu.lowercase_string(sample_text)

print(f"Original Text: {sample_text}")
print(f"Reversed Text: {reversed_text}")
print(f"Capitalized Text: {capitalized_text}")
print(f"Uppercase Text: {uppercase_text}")
print(f"Lowercase Text: {lowercase_text}")