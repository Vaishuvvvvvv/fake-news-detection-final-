import streamlit as st
import pickle
import numpy as np

# Load the trained SVM model & vectorizer
with open("fake_new_svm.pkl", "rb") as model_file:
    svm_model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

# Streamlit UI
st.title("📰 Fake News Detection with SVM")
st.subheader("Enter a news article to check if it's **Real** or **Fake**")

# User input
user_input = st.text_area("Enter News Text Here:")

if st.button("Check News"):
    if user_input:
        # Preprocess input
        transformed_input = vectorizer.transform([user_input])
        prediction = svm_model.predict(transformed_input)[0]

        # Display result
        if prediction == 1:
            st.success("✅ This news is **Real**!")
        else:
            st.error("🚨 This news is **Fake**!")
    else:
        st.warning("⚠️ Please enter some text to analyze.")
