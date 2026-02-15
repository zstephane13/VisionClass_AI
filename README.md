# VisionClass AI

Application de prédiction **Homme / Femme** à partir d'une image, basée sur un modèle de deep learning.

## Technologies

- **Streamlit** : interface web
- **TensorFlow/Keras** : modèle de classification
- **PIL** : traitement d'images

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

1. Placez le fichier `modele_homme_femme.h5` dans le dossier `code&dataset/`
2. Depuis le dossier du projet :
   ```bash
   cd "code&dataset"
   streamlit run app.py
   ```

## Structure du projet

- `app.py` : application Streamlit
- `code.ipynb` : notebook d'entraînement du modèle
- `modele_homme_femme.h5` : modèle pré-entraîné (à ajouter localement)
