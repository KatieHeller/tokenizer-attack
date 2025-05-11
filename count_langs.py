# Counts number of natural languages processed from oscar-mini dataset

from pathlib import Path

output_dir = Path("oscar-mini/processed")

count = 0
for category_dir in output_dir.iterdir():
        if category_dir.is_dir():
            count += 1

print(count)