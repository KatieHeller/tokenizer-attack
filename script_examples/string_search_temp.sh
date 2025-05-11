# Search for each token *as a string* in the given corpus. 
# This is for the baseline based on token categorization (TC).
test_id=0
experiment_dir=experiments/mixed_code/n_10/$test_id
corpus_dir=/scratch/network/kh3329/tokenizer-attack/github/scrubbed


for subdir in "$experiment_dir"/*/; do

    lang_code=$(basename "$subdir")

    python -m search_string \
    --output_dir $experiment_dir \
    --corpus_dir $corpus_dir \
    --lang $lang_code

done
