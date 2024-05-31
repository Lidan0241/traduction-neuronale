# -*- coding: utf-8 -*-
"""lemmatisation_en.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16ki63yPzzicuK8LRX6fhiZXpjvbvI5u7
"""

import sys
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Téléchargement des données nécessaires pour NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Initialisation du lemmatiseur
lemmatizer = WordNetLemmatizer()

# Définition d'une fonction pour obtenir la classe de mot WordNet à partir d'une balise Treebank
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ  # Adjectif
    elif treebank_tag.startswith('V'):
        return nltk.corpus.wordnet.VERB  # Verbe
    elif treebank_tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN  # Nom
    elif treebank_tag.startswith('R'):
        return nltk.corpus.wordnet.ADV  # Adverbe
    else:
        # Par défaut, on considère que c'est un nom
        return nltk.corpus.wordnet.NOUN

def lemmatize_english_file(input_file_path):

    # Remplacement de l'extension du fichier pour créer le nom du fichier de sortie
    output_file_path = input_file_path.replace('.tok.true.clean', '_lemme')

    # Ouverture du fichier d'entrée et du fichier de sortie
    with open(input_file_path, 'r', encoding='utf-8') as infile, \
         open(output_file_path, 'w', encoding='utf-8') as outfile:
        # Lecture et traitement du fichier ligne par ligne
        for line in infile:
            # Tokenisation de la ligne
            words = word_tokenize(line)
            # Marquage des parties du discours
            tagged_words = pos_tag(words)
            # Lemmatisation des mots
            lemmas = [
                lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in tagged_words
            ]
            # Réassemblage des mots lemmatizés en une phrase et écriture dans le fichier de sortie, en conservant le caractère de nouvelle ligne
            outfile.write(' '.join(lemmas) + '\n')

# Vérification des arguments de ligne de commande
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        lemmatize_english_file(input_file_path)
    else:
        print("Veuillez fournir le chemin du fichier d'entrée en argument.")