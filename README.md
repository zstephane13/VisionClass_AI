# VisionClass AI

A male/female gender prediction application that uses a camera or gallery image based on a deep learning model; with some datasets for testing.

## Technologies

- **Streamlit** : interface web
- **TensorFlow/Keras** : modèle de classification
- **PIL** : traitement d'images

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

1. Depuis le dossier du projet :
   ```bash
   cd "code&dataset"
   streamlit run app.py
   ```

## Structure du projet

- `app.py` : application Streamlit
- `code.ipynb` : notebook d'entraînement du modèle
- `modele_homme_femme.h5` : modèle pré-entraîné
