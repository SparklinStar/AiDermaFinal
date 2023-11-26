import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.efficientnet import preprocess_input
import style
from googleapiclient.discovery import build

# Set your OpenAI API key and YouTube API key



page_bg_img = style.stylespy()  # used for styling the page

# Appname
st.set_page_config(page_title="AI DERMATOLOGIST", layout="wide")

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #fff;'>AI DERMATOLOGIST</h1>", unsafe_allow_html=True)
st.sidebar.title("AI DERMATOLOGIST")

# Load your model and its weights
model = tf.keras.models.load_model('EfficientNetB2-Skin-87.h5')
class_names = ['Eczema', 'Warts Molluscum and other Viral Infections', 'Melanoma', 'Atopic Dermatitis',
    'Basal Cell Carcinoma (BCC)', 'Melanocytic Nevi (NV)', 'Benign Keratosis-like Lesions (BKL)',
    'Psoriasis pictures Lichen Planus and related diseases', 'Seborrheic Keratoses and other Benign Tumors',
    'Tinea Ringworm Candidiasis and other Fungal Infections']  # List of your class names

# Define the Streamlit app

user_input=0
st.write("Upload an image for classification")
    
uploaded_file = 0
col1,col2=st.columns(2)
    
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    save_path = "uploaded_image.png"
    image.save(save_path)

    st.image(image, caption='Uploaded Image.', use_column_width=True)

    st.write("")
    st.write("Classifying...")

        # Preprocess the image
    image = image.resize((224, 224))
    image = np.array(image)
    image = preprocess_input(image)

        # Make predictions
    predictions = model.predict(np.expand_dims(image, axis=0))

    if np.isnan(predictions).any():
            st.write("Prediction result is NaN. Please try with another image")
    else:
        predicted_class = np.argmax(predictions)
            
        confidence = predictions[0][predicted_class]
        if(confidence>=0.9):
            st.write(f"Predicted class: {class_names[predicted_class]}")
            st.write(f"Confidence: {confidence:.2f}")
        else:
            st.write("No disease Predicted")
        #user_input = st.text_input("Describe the patient's condition and symptoms:")
        user_input=class_names[predicted_class]
        st.session_state["disease"] = user_input