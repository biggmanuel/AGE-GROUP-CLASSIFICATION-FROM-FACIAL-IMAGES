import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Secure Access Portal", page_icon="🔒", layout="centered")

# --- 2. SESSION STATE (Memory) ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- 3. LOAD THE AI MODEL ---
@st.cache_resource
def load_cnn_model():
    model_path = "model.h5"
    if os.path.exists(model_path):
        return tf.keras.models.load_model(model_path)
    else:
        return None

model = load_cnn_model()
# Make sure this matches the alphabetical order of your dataset folders!
CATEGORIES = ["Adult", "Child", "Teenager"] 

# ==========================================
# SCREEN 1: THE LOGIN GATEWAY
# ==========================================
if not st.session_state['logged_in']:
    st.title("System Login")
    st.write("Please enter your credentials to access the portal.")
    
    # Hardcoded offline credentials for defense day
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Log In"):
        if username == "admin" and password == "unical2026":
            st.session_state['logged_in'] = True
            st.rerun() 
        else:
            st.error("⚠️ Invalid username or password.")

# ==========================================
# SCREEN 2: THE AGE VERIFICATION DASHBOARD
# ==========================================
else:
    st.title("Age Verification Check")
    st.info("✅ Login Successful. However, to access restricted content, biometric verification is required.")
    st.markdown("---")
    
    st.write("### STEP 1: Biometric Scan")
    uploaded_file = st.file_uploader("Upload Facial Image (.JPG, .PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", width=300)
        st.markdown("---")
        
        if model is None:
            st.error("⚠️ AI Model missing. Make sure your 'model.h5' file is in this folder.")
        else:
            with st.spinner("Analyzing biometric features..."):
                
                # Resize and normalize image for the AI
                img_resized = image.resize((224, 224))
                img_array = np.array(img_resized) / 255.0
                img_array = np.expand_dims(img_array, axis=0)
                
                # The AI makes its prediction
                predictions = model.predict(img_array)
                predicted_index = np.argmax(predictions)
                predicted_category = CATEGORIES[predicted_index]
                confidence_score = np.max(predictions) * 100
                
                st.write("### SYSTEM OUTPUT")
                st.write(f"**PREDICTED DEMOGRAPHIC:** {predicted_category} (Confidence: {confidence_score:.2f}%)")
                
                # --- THE FINAL ACCESS DECISION ---
                if predicted_category == "Adult":
                    st.success("🟢 ACCESS GRANTED: User verified as Adult. Welcome to the secure dashboard.")
                else:
                    st.error("🔴 ACCESS DENIED: System has detected an underage user. Connection terminated.")
    
    st.markdown("---")
    if st.button("Log Out"):
        st.session_state['logged_in'] = False
        st.rerun()