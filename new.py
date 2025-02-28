import streamlit as st
import pickle
import os

# ✅ Apply Custom CSS for Styling
st.markdown("""
    <style>
        /* Colorful Background */
        .stApp {
            background: linear-gradient(135deg, #FFDEE9 10%, #B5FFFC 100%);
        }
        
        /* Centered Title with Glow Effect */
        .title {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            color: #fff;
            text-shadow: 0 0 15px rgba(255,255,255,1), 0 0 30px rgba(255,255,255,0.8);
        }

        /* Section Headings with Lighting Effect */
        h3 {
            color: #fff;
            text-shadow: 0 0 10px rgba(255, 255, 255, 1), 0 0 20px rgba(255, 255, 255, 0.8);
        }

        /* Left-Aligned About Section with Dim Borders */
        .about-container {
            text-align: left;
            font-size: 18px;
            background: rgba(255, 255, 255, 0.85);
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(255,255,255,0.5);
            border: 2px solid rgba(255,255,255,0.3);
        }

        /* Fade-in Effect */
        .fade-in {
            animation: fadeIn 1.5s;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Model Path
model_path = r"C:\Users\VAISHNAVI DANDUMENU\Desktop\hello\fake_news_model.pkl"

# ✅ Check Model File
if not os.path.exists(model_path):
    st.error("❌ Model file not found. Please check the path: " + model_path)
else:
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # ✅ Streamlit UI with Centered Title
    st.markdown("<h1 class='title fade-in'>FAKE NEWS DETECTION</h1>", unsafe_allow_html=True)

    # ✅ Sidebar for About & Suggestions
    with st.sidebar:
        st.markdown("<h3 class='fade-in'>ℹ️ About</h3>", unsafe_allow_html=True)
        if st.button("Show About"):
            st.markdown("""
            <div class='about-container fade-in'>
                This Fake News Detector uses a machine learning model to classify news articles as either **True** or **Fake**.
                Enter a news headline or article and click 'Check' to verify its credibility.
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<h3 class='fade-in'>💡 Suggestions & Reviews</h3>", unsafe_allow_html=True)
        review = st.text_area("Leave your feedback here:")
        if st.button("Submit Review"):
            if review.strip():
                st.success("✅ Thank you for your feedback!")
            else:
                st.warning("⚠️ Please enter some text before submitting.")

    # ✅ User Input
    user_input = st.text_area("Enter a news headline or article:", key="news_input")

    if st.button("Check", key="check_button"):
        if user_input.strip():
            # ✅ Predict
            prediction = model.predict([user_input])[0]
            result = "✅ TRUE NEWS" if prediction == 1 else "🚨 FAKE NEWS"

            # ✅ Display result with fade-in effect and lighting effect
            st.markdown(f"<h2 class='fade-in' style='text-shadow: 0 0 12px rgba(255, 255, 255, 1), 0 0 25px rgba(255, 255, 255, 0.8);'>{result}</h2>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter some text.")
