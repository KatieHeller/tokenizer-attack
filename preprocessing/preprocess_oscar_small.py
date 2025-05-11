# Script for preprocessing OSCAR-small dataset

import os
# Ensure everything goes to scratch directory to avoid running out of space on home directory
os.environ["HF_HOME"] = "/scratch/network/kh3329/hf_cache"
os.environ["HF_DATASETS_CACHE"] = "/scratch/network/kh3329/hf_cache/datasets"
os.environ["HUGGINGFACE_HUB_CACHE"] = "/scratch/network/kh3329/hf_cache/hub"
from pathlib import Path
from datasets import get_dataset_config_names, load_dataset
import sys
sys.path.append('/scratch/network/kh3329/tokenizer-attack')
from utils import ensure_dir

corpus_dir = Path('/scratch/network/kh3329/tokenizer-attack/oscar-small-corpus')
clean_dir = corpus_dir / 'processed'

os.environ["HF_DATASETS_CACHE"] = str(corpus_dir / 'hf_cache')

language_codes = get_dataset_config_names('nthngdy/oscar-small')

for language_code in language_codes:
    try:
        print(f'Processing language: {language_code}', flush=True)

        dataset = load_dataset(
            'nthngdy/oscar-small',
            language_code,
            split='train',
            cache_dir=os.environ["HF_DATASETS_CACHE"]
        )

        output_dir = clean_dir / language_code
        ensure_dir(output_dir)

        output_file = output_dir / f'{language_code}_oscar_small.txt'

        with open(output_file, 'w', encoding='utf-8') as f:
            for example in dataset:
                f.write(example['text'] + '\n\n')

        print(f'Saved to {output_file}', flush=True)

    except Exception as e:
        print(f'Failed to process language {language_code}: {e}', flush=True)

