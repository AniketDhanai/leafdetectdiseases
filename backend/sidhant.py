import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import os
import requests

# Load environment variables from a .env file
load_dotenv()

# Function to generate a response based on a prompt and an image path
def generate_gemini_response(prompt, image_path):
    # Prepare image data
    image_data = open(image_path, "rb").read()
    # Configure Gemini API endpoint
    url = "https://api.gemini.com/gemini/generate_text_from_image"
    headers = {"x-api-key": os.getenv("GEMINI_API_KEY")}
    # Send request to Gemini API
    response = requests.post(url, data=image_data, headers=headers)
    # Return generated response
    if response.status_code == 200:
        return response.json()["content"]
    else:
        return "Error: Failed to generate response from Gemini."

# Streamlit interface setup
st.title("Plant Pathologist Assistant")

# Upload image file
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Display initial prompt
    st.markdown("""
    ## As a highly skilled plant pathologist, your expertise is indispensable in our pursuit of maintaining optimal plant health. You will be provided with information or samples related to plant diseases, and your role involves conducting a detailed analysis to identify the specific issues, propose solutions, and offer recommendations.
    
    **Analysis Guidelines:**
    
    1. **Disease Identification:** Examine the provided information or samples to identify and characterize plant diseases accurately.
    
    2. **Detailed Findings:** Provide in-depth findings on the nature and extent of the identified plant diseases, including affected plant parts, symptoms, and potential causes.
    
    3. **Next Steps:** Outline the recommended course of action for managing and controlling the identified plant diseases. This may involve treatment options, preventive measures, or further investigations.
    
    4. **Recommendations:** Offer informed recommendations for maintaining plant health, preventing disease spread, and optimizing overall plant well-being.
    
    5. **Important Note:** As a plant pathologist, your insights are vital for informed decision-making in agriculture and plant management. Your response should be thorough, concise, and focused on plant health.
    
    **Disclaimer:**
    *"Please note that the information provided is based on plant pathology analysis and should not replace professional agricultural advice. Consult with qualified agricultural experts before implementing any strategies or treatments."*
    
    Your role is pivotal in ensuring the health and productivity of plants. Proceed to analyze the provided information or samples, adhering to the structured.
    """)

    # Generate response button
    if st.button("Generate Response"):
        response = generate_gemini_response("Input prompt for the plant pathologist", uploaded_file.name)
        st.markdown(f"**Generated Response:**\n{response}")
