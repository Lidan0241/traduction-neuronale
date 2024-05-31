import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# Load the reference and candidate translations
with open("./data/clean/Europarl_test_500.fr", "r", encoding="utf-8") as ref_file:
    references = ref_file.readlines()

with open(".src/predictions/Europarl_pred_500.fr.txt", "r", encoding="utf-8") as cand_file:
    candidates = cand_file.readlines()

# Function to calculate BLEU score for each sentence
def calculate_bleu_score(reference, candidate):
    reference_tokens = [reference.split()]
    candidate_tokens = candidate.split()
    smoothing_function = SmoothingFunction().method4
    return sentence_bleu(reference_tokens, candidate_tokens, smoothing_function=smoothing_function)

# Calculate BLEU scores for all sentence pairs
bleu_scores = [calculate_bleu_score(ref, cand) for ref, cand in zip(references, candidates)]

# Calculate average BLEU score
average_bleu_score = sum(bleu_scores) / len(bleu_scores)
average_bleu_score