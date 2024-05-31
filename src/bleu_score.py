from nltk.translate.bleu_score import sentence_bleu, corpus_bleu, SmoothingFunction

with open('./predictions/combined_lemme_pred.fr', 'r', encoding='utf-8') as f:
    predictions = f.readlines()

with open('../data/clean/combined_test_lemme.fr', 'r', encoding='utf-8') as f:
    references = f.readlines()


predictions = [line.strip() for line in predictions]
references = [[line.strip()] for line in references]  # BLEU expects list of references per hypothesis

#print(len(predictions))
#print(len(references))

# calculer BLEU score
smoothing_function = SmoothingFunction().method1
bleu_score = corpus_bleu(references, predictions, smoothing_function=smoothing_function)

print("BLEU score pour la prédiction de Europarl+Emea après le lemmatization:")
print(bleu_score)
