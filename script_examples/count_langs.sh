# Count number of natural and programming languages processed in experiment directory

model_name=qwen3
experiment_dir=/scratch/network/kh3329/tokenizer-attack/experiments/llm_tokenizers/$model_name

natural_count=0
programming_count=0

for subdir in "$experiment_dir"/*/; do
    dir_name=$(basename "$subdir")
    if [[ "$dir_name" == unshuffled_deduplicated_* ]]; then
        ((natural_count++))
    else
        ((programming_count++))
    fi
done

echo "Natural count: $natural_count"
echo "Programming count: $programming_count"