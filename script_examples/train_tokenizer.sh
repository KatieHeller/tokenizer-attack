# Train tokenizer on a randomly sampled mix of n data categories, saving the output in output_dir.
n=10
test_id=5
output_dir=experiments/mixed_languages/n_${n}/$test_id
# corpus_dir=/scratch/network/kh3329/tokenizer-attack/oscar-small-corpus/processed
corpus_dir=/scratch/network/kh3329/tokenizer-attack/github/

echo "Training tokenizers on mixes of $n languages"
python -m train_mixed_tokenizer \
    --output_dir $output_dir \
    --num_categories $n \
    --corpus_dir $corpus_dir
