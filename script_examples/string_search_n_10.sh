# Search for each token *as a string* in the given corpus. 
# This is for the baseline based on token categorization (TC).

corpus_dir=/scratch/network/kh3329/tokenizer-attack/oscar-mini/processed

for test_id in $(seq 0 14); do

    experiment_dir=experiments/mixed_languages/n_10/$test_id

    for subdir in "$experiment_dir"/*/; do

        lang_code=$(basename "$subdir")

        python -m search_string \
        --output_dir $experiment_dir \
        --corpus_dir $corpus_dir \
        --lang $lang_code
    
    done

done
