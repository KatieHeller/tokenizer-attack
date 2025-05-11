# python version of clean_merge_list.ipynb

from utils import read_tokenizer_json, ensure_dir
from pathlib import Path
from tqdm import tqdm
from collections import defaultdict, Counter
from tokenizers import Tokenizer
import seaborn as sns
import numpy as np

tokenizer_dir = Path('tokenizer_json/llm_tokenizers')

model_name = 'qwen3'
tokenizer_json = read_tokenizer_json(tokenizer_dir / f'{model_name}_tokenizer.json')

# check if merges are unique
rhs = []
for m in tokenizer_json['merges']:
    rhs.append(''.join(m.split(' ')))
print(f'All merges unique: {len(rhs) == len(set(rhs))}')
print(f'Fraction of non-redundant merges: {len(set(rhs))/len(rhs)}')