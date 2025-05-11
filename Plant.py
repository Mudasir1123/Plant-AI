import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# 🔹 Streamlit Page Config
st.set_page_config(page_title="🌿 AI-Powered Crop Disease Detector", page_icon="🩺")

# 🔹 Configure Gemini AI
API_KEY = os.getenv("GEMINI_API_KEY") or "AIzaSyBBTNFznyQOKaD56pYb-dXxwbp8bGYOXAI"
genai.configure(api_key=API_KEY)
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

# 🔹 Pakistani Language Selection
languages = {
    "English": "English",
    "Urdu": "اردو",
    "Sindhi": "سنڌي",
    "Punjabi (Shahmukhi)": "پنجابی",
    "Pashto": "پښتو",
    "Balochi": "بلوچی",
    "Siraiki": "سرائیکی",
    "Kashmiri": "كشميري",
    "Brahui": "براہوئی",
    "Gujarati": "ગુજરાતી",
    "Gilgiti": "گلگتی",
    "Balti (Skardu)": "بلتی",
    "Khowar (Chitrali)": "کهووار",
    "Shina": "شِنا",
    "Hindko": "ہندکو",
    "Potohari": "پوٹوہاری",
    "Wakhi": "وخی",
    "Torwali": "توروالی",
    "Burushaski": "بروشسکی",
}

# Select Language
selected_language = st.selectbox("🌍 اپنی زبان منتخب کریں | Select your language:", list(languages.keys()))

# 🔹 Streamlit UI
st.title("🌿 AI-Powered Crop Disease Detector")
st.write("📸 ایک پودے کی تصویر اپ لوڈ کریں، اور AI بیماریوں کا پتہ لگائے گا اور علاج کی تجویز دے گا۔")

# Upload Image
uploaded_image = st.file_uploader("📸 تصویر اپ لوڈ کریں (JPG, PNG, JPEG)", type=["jpg", "png", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="📷 اپ لوڈ شدہ تصویر", use_container_width=True)  # Updated to use_container_width

    # 🔹 AI Analysis
    st.info("🔍 پودے کی صحت کا تجزیہ کیا جا رہا ہے...")

    try:
        prompt = f"""
        Identify the disease in the following plant image and suggest treatments. 
        Provide results in {selected_language} ({languages[selected_language]}).

        The image contains a close-up of a plant leaf. Check for any disease symptoms such as spots, discoloration, or mold.
        """
        # Send request to the model
        response = gemini_model.generate_content([prompt, image])

        # Handle response
        if response and hasattr(response, "text") and response.text.strip():
            st.success("✅ AI کا تجزیہ مکمل ہو گیا!")
            st.markdown(f"### 🌱 بیماری اور علاج ({selected_language}):")
            st.write(response.text.strip())
        else:
            st.warning("⚠️ کوئی واضح تشخیص نہیں ملی۔ براہ کرم دوسری تصویر آزمائیں۔")

    except Exception as e:
        st.error(f"⚠️ AI میں خرابی: {str(e)}")

# 🔹 Footer
st.markdown("---")
st.markdown("🚀 **Developed by Muhammad Mudasir** | AI-Powered Crop Disease Detector")
