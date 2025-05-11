# Fix format of merges from qwen3 tokenizer.json file

import json

with open('qwen3_tokenizer.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

if 'model' in data and 'merges' in data['model']:
    data['model']['merges'] = [' '.join(pair) for pair in data['model']['merges']]

    with open('qwen3_tokenizer.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
