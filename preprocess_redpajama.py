import pandas as pd
import seaborn as sns
import json
import ujson
import os
from pathlib import Path
from tqdm import tqdm
from utils import ensure_dir
from collections import defaultdict
import random
import numpy as np

data_dir = Path('/scratch/network/kh3329/tokenizer-attack')

for fin in os.listdir(data_dir / 'github'):
     if os.path.isfile(data_dir / 'github' / fin):
        random_str = Path(fin).stem
        sub_df = pd.read_json(data_dir / 'github' / fin, lines=True)
        with open(data_dir / 'github' / f'{random_str}.txt', 'w') as fo:
            fo.write('\n\n'.join(sub_df['text'].astype(str)))

languages_json = json.load(open('preprocessing/languages.json'))
extensions_to_language = {}
for language, data in languages_json.items():
    if 'extensions' in data:
        for ext in data['extensions']:
            extensions_to_language[ext[1:]] = language

scrubbed_data_dir = Path('/scratch/network/kh3329/tokenizer-attack/github')
xlab_data_dir = scrubbed_data_dir / 'scrubbed'

for fin in os.listdir(scrubbed_data_dir):
    if fin.endswith('.txt'):
        continue # Only process github_sample.jsonl.
    if os.path.isfile(scrubbed_data_dir / fin):
        random_str = fin.split('_')[1].split('.')[0]
        df = pd.read_json(scrubbed_data_dir / fin, lines=True)
        languages = []
        for meta in df.meta:
            languages.append(extensions_to_language.get(meta['path'].rsplit('.', 1)[-1].rsplit('/', 1)[-1].lower()))
        df['language'] = languages
        for language, sub_df in tqdm(df.groupby('language'), desc=random_str):
            language = ''.join(language.split(' '))
            ensure_dir(xlab_data_dir / language)
            with open(xlab_data_dir / language / f'{random_str}.txt', 'w') as fin:
                fin.write('\n\n'.join(sub_df['text']))