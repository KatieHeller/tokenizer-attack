# Record all merge frequencies to apply our attack in controlled experiments.
test_id=0
experiment_dir=experiments/mixed_languages/n_112/$test_id
lang_code=en
corpus_dir=/scratch/network/kh3329/oscar-corpus-small/processed

python -m dump_frequencies \
    --experiment_dir $experiment_dir \
    --lang_code $lang_code \
    --corpus_dir $corpus_dir
