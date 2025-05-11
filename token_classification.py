# Our implementation of the token classification baseline

import json
from collections import defaultdict, Counter
from pathlib import Path

n = 10  # Number of languages
data_type = "languages" # either languages or code

# 15 trials
for test_id in range(15):

    # Path to the directory containing output subdirectories for each category
    output_dir = Path(f"experiments/mixed_{data_type}/n_{n}/{test_id}")

    category_token_counts = {}

    for category_dir in output_dir.iterdir():
        if category_dir.is_dir():
            lang = category_dir.name
            counts_file = category_dir / "token_string_counts.json"
            if counts_file.exists():
                with open(counts_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    category_token_counts[lang] = data["counts"]
            else:
                print(f"File not found: {counts_file}")

    token_assignments = {}

    # Set of all unique tokens across categories
    all_tokens = set()
    for counts in category_token_counts.values():
        all_tokens.update(counts.keys())

    # Assign each token to the category with the highest count
    for token in all_tokens:
        max_count = 0
        assigned_category = None
        for category, counts in category_token_counts.items():
            count = counts.get(token, 0)
            if count > max_count:
                max_count = count
                assigned_category = category
        if assigned_category:
            token_assignments[token] = assigned_category

    category_assignment_counts = Counter(token_assignments.values())
    total_assigned_tokens = sum(category_assignment_counts.values())

    category_proportions = {
        category: count / total_assigned_tokens
        for category, count in category_assignment_counts.items()
    }

    solution = {"lang_vals": category_proportions}

    output_path = Path(f"experiments/mixed_{data_type}/n_{n}/{test_id}/tc_solution.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(solution, f, indent=4)