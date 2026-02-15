import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Chargeons le modèle
model = load_model('modele_homme_femme.h5')

# Définissons la fonction de prédiction
def predict_image(img):
    img = img.resize((128, 128))  # Redimensionner l'image
    img_array = img_to_array(img) / 255.0  # Normaliser
    img_array = np.expand_dims(img_array, axis=0)  # Ajouter une dimension batch
    prediction = model.predict(img_array)
    return prediction

# --- Interface Streamlit ---

st.title('Prédiction Homme / Femme 👤')

# Option : Uploader ou Prendre une photo
option = st.radio(
    "Choisissez une méthode :",
    ("Uploader une image", "Prendre une photo 📷")
)

# Variable pour stocker l'image
img = None

if option == "Uploader une image":
    uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)

elif option == "Prendre une photo 📷":
    camera_photo = st.camera_input("Prenez une photo")
    if camera_photo is not None:
        img = Image.open(camera_photo)

# S'il y a une image (uploadée ou prise avec la caméra)
if img is not None:
    # Afficher l'image
    st.image(img, caption='Image sélectionnée', use_container_width=True)

    # Faire la prédiction
    prediction = predict_image(img)

    # Afficher le résultat
    if prediction[0][0] < 0.5:
        st.success("Résultat : **Homme** 👨")
    else:
        st.success("Résultat : **Femme** 👩")

    # Afficher aussi le score de certitude
    st.write(f"Score de certitude : {prediction[0][0]:.4f}")
