# Utilisation des scripts

## Récupération et séparation des corpus

1. Il faut d’abord télécharger les corpus Europarl et Emea sur les deux liens : https://opus.nlpl.eu/Europarl/en&fr/v8/Europarl https://opus.nlpl.eu/EMEA/en&fr/v3/EMEA
2. `train_europarl.ipynb` : ce script est pour extraire les premiers 100 000 rangs sur le corpus Europarl `fr` et `en`.
3. `train_emea.ipynb` : ce script est pour extraire les premiers 10 000 rangs sur le corpus Emea `fr` et `en`.
4. `dev_europarl.ipynb`: ce script est pour extraire la partie `dev` du corpus Europarl.
5. `test_europarl.ipynb`: ce script est pour extraire la partie `test` du corpus Europarl.
6. `test_emea.ipynb`: ce script est pour extraire la partie `test` du corpus Emea.



## Nettoyage des données

Nous nous sommes servis des scripts Perl fourni par le professeur pour la tokenisation, ainsi que l'entraînement de true-case des corpus.


## Entraînement de modèle
`OpenNMT_Train`: ce script construit des vocabulaires pour la langue source et cible, puis entraîne le modèle avec le chemin des données selon la configuration du fichier `toy_en_fr.yaml`, ensuite il traduit en fonction du modèle entraîné

## Lemmatisation des données

#### Lemmatisation des données anglais :
`lemmatisation_en.ipynb`: nous avons utilisé `nltk` et `WordNetLemmatizer` pour lemmatiser les mots dans le corpus en anglais. Le fichier à traiter est fourni en tant qu'un argument, mais il est nécessaire de convertir le code au format `.py`. On peut entrer la commande suivante pour l'exécution du code : 
> python3 lemmatisation_en.py Europarl_test_500.tok.true.clean.en.
#### Lemmatisation des données françaises :
`lemmatisation_fr.ipynb`: nous avons utilisé `spacy` pour substituer `nltk` car le dernier ne fonctionne pas bien pour la langue française en POS.

`lemmatistaion_fr(1).ipynb`: c'est une version en utilisant `nltk` et `FrenchLefffLemmatizer` mais on trouve que les mots ne sont pas bien lemmatisés.

## Potentielle détokenisation de données
`detokenize.sh`: ce script shell sert à détokeniser un corpus pour donner une forme plus naturelle de traduction. Pour exécuter: `./detokenize.sh`
