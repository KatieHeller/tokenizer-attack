# Remove unshuffled_original_ languages - we only use unshuffled_deduplicated_ for natural languages

experiment_dir="experiments/llm_tokenizers/qwen3"
backup_dir="experiments/llm_tokenizers/original_langs_qwen3"

mkdir -p "$backup_dir"

for dir in "$experiment_dir"/unshuffled_original_*; do
    if [ -d "$dir" ]; then
        echo "Moving $dir to $backup_dir"
        mv "$dir" "$backup_dir/"
    fi
done
