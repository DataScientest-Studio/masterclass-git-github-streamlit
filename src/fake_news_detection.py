### Import des librairies
# Manipulation des données
import pandas as pd
import numpy as np
# Creation de features
from sklearn.feature_extraction.text import TfidfVectorizer
# Split des données
from sklearn.model_selection import train_test_split
# Modèles
from sklearn.linear_model import PassiveAggressiveClassifier
# Evaluation des modèles
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

### Definition de la fonction principale
def main(path_):
    """ Definition de la fonction de prédiction"""
    
    ### Lecture
    news_data= pd.read_csv(path_)

    ### Séparation en jeux de test et d'entrainement
    x_train, x_test, y_train, y_test= train_test_split(news_data["text"], 
                                                        news_data['label'], 
                                                        test_size= 0.4, 
                                                        random_state= 7) # Reproductibilité des résultats

    ### Creation des features (variables indicatrices)
    vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)
    tfidf_train=vectorizer.fit_transform(x_train) 
    tfidf_test=vectorizer.transform(x_test)

    ### Création modèle de classification avec un modèle PassiveAggressiveClassifier
    passive=PassiveAggressiveClassifier(max_iter=50)
    passive.fit(tfidf_train,y_train)

    ### Prédiction
    y_pred=passive.predict(tfidf_test)

    ### Calcul de l'accuracy (Taux de bonnes prédictions)
    acc = passive.score(tfidf_test, y_test)

    return y_pred, acc

### Appel de la fonction
if __name__ == "__main__":
    # Chemein vers les données
    chemin = "../data/raw/news.csv"

    # Appel de fonction main: Calcul de l'accuracy
    _ , acc = main(chemin)

    # Affichage de l'accuracy
    print(acc)