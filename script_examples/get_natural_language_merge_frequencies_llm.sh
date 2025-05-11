# Gets merge frequencies for all natural languages from oscar-mini corpus

model_name=qwen3
experiment_dir=experiments/llm_tokenizers/$model_name
natural_languages_corpus_dir=/scratch/network/kh3329/tokenizer-attack/oscar-mini/processed

for subdir in "$natural_languages_corpus_dir"/*/; do
    lang_code=$(basename "$subdir")
    output_dir="$experiment_dir/$lang_code"
    lock_dir="$output_dir.lock"

    # Use lock directories to prevent concurrent execution while running multiple instances
    if mkdir "$lock_dir" 2>/dev/null; then
        # Ensure the lock directory is removed upon script exit
        trap 'rm -rf "$lock_dir"' EXIT

        if [ -d "$output_dir" ]; then
            echo "Skipping $lang_code: output already exists at $output_dir"
        else
            echo "Processing $lang_code..."
            python -m dump_frequencies \
                --experiment_dir "$experiment_dir" \
                --lang_code "$lang_code" \
                --corpus_dir "$natural_languages_corpus_dir" \
                --model_name "$model_name"
        fi

        rm -rf "$lock_dir"
        trap - EXIT
    else
        echo "Another process is handling $lang_code. Skipping..."
    fi
done
