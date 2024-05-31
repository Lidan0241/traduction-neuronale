# Utilisation des scripts

## Récupération et séparation des corpus

1. Il faut d’abord télécharger les corpus Europarl et Emea sur les deux liens : https://opus.nlpl.eu/Europarl/en&fr/v8/Europarl https://opus.nlpl.eu/EMEA/en&fr/v3/EMEA
2. `train_europarl.ipynb` : ce script est pour extraire les premiers 100 000 rangs sur le corpus Europarl `fr` et `en`.
3. `train_emea.ipynb` : ce script est pour extraire les premiers 10 000 rangs sur le corpus Emea `fr` et `en`.
4. `dev_europarl.ipynb`: ce script est pour extraire la partie `dev` du corpus Europarl.
5. `test_europarl.ipynb`: ce script est pour extraire la partie `test` du corpus Europarl.
6. `test_emea.ipynb`: ce script est pour extraire la partie `test` du corpus Emea.



## Nettoyage des données







## Lemmatisation des données

#### Lemmatisation des données françaises :

`lemmatisation_fr.ipynb`: nous avons utilisé `spacy` pour substituer `nltk` car le dernier ne supporte pas la langue française en POS.