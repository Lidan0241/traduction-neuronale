
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu, SmoothingFunction

# Load the data from the uploaded files
with open('./src/predictions/combined_pred_500.fr', 'r', encoding='utf-8') as f:
    predictions = f.readlines()

with open('./data/clean/combined_test.fr', 'r', encoding='utf-8') as f:
    references = f.readlines()

# Process data to remove leading/trailing whitespaces and split into list of lists
predictions = [line.strip() for line in predictions]
references = [[line.strip()] for line in references]  # BLEU expects list of references per hypothesis

#print(len(predictions))
#print(len(references))

# Calculate BLEU score
smoothing_function = SmoothingFunction().method1
bleu_score = corpus_bleu(references, predictions, smoothing_function=smoothing_function)

print("BLEU score pour la prédiction de Europarl+Emea après le prétraitement  et true-caser:")
print(bleu_score)
