from pathlib import Path
import html
import random
import re
import emoji


def clean_text(text):
    # Decode HTML entities
    text = html.unescape(text)

    # Remove URLs
    text = re.sub(r"\b(?:https?://|www\.)[^\s<>]+", " ", text, flags=re.IGNORECASE)

    # Remove known HTML tags
    text = re.sub(r"</?(?:b|i|u|span|pre|html)\s*>", " ", text, flags=re.IGNORECASE)

    # Remove emoji
    text = emoji.replace_emoji(text, replace=" ")

    # Remove noise
    text = re.sub(r"(?<!\S)(?:[@$%]|\^+)(?!\S)", " ", text)
    text = text.replace("+++$+++", " ")

    # Normalize whitespace
    return " ".join(text.split())


# Locate and read the input file
folder = Path(__file__).resolve().parent
input_path = folder / "corrupt_twitter_corpus.txt"
output_path = folder / "cleaned_twitter_corpus.txt"

raw_lines = input_path.read_text(encoding="utf-8").splitlines()

# Save 10 random lines and their cleaned versions
sample = random.Random(42).sample(raw_lines, min(10, len(raw_lines)))

(folder / "twitter_sample_input.txt").write_text(
    "\n".join(sample) + "\n", encoding="utf-8"
)
(folder / "twitter_sample_output.txt").write_text(
    "\n".join(clean_text(line) for line in sample) + "\n", encoding="utf-8"
)

# Clean the full dataset and remove empty lines
cleaned_lines = [clean_text(line) for line in raw_lines]
cleaned_lines = [line for line in cleaned_lines if line]

(folder / "cleaned_twitter_corpus.txt").write_text(
    "\n".join(cleaned_lines) + "\n", encoding="utf-8"
)

print(f"Lines: {len(raw_lines):,} -> {len(cleaned_lines):,}")