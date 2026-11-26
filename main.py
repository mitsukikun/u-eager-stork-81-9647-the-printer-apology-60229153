import os

# one-line printer apology, at most 120 characters
line = ("Sorry I printed your browser history to the whole office. "
        "You clicked Print All — I obey, I don't judge.")
assert len(line) <= 120

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
