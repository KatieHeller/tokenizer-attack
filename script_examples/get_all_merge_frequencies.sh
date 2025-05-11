# Run given get_merge_frequencies.sh for all languages in languages.txt

n=10
test_id=5
experiment_dir=experiments/mixed_languages/n_${n}/$test_id
languages_file=experiments/mixed_languages/n_${n}/$test_id/languages.txt
corpus_dir=/scratch/network/kh3329/tokenizer-attack/oscar-small-corpus/processed

while read -r lang_code; do

    python -m dump_frequencies \
    --experiment_dir $experiment_dir \
    --lang_code $lang_code \
    --corpus_dir $corpus_dir

done < $languages_file