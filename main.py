import streamlit as st
from groq import Groq

# --- CONFIGURATION ---
# PASTE YOUR GROQ KEY HERE (starts with gsk_...)
# This looks inside .streamlit/secrets.toml automatically
if "GROQ_API_KEY" in st.secrets:
    api_key = st.secrets["GROQ_API_KEY"]
else:
    # This helps if you forget to set it up later
    st.error("Missing API Key. Please add it to secrets.toml")
    st.stop()

client = Groq(api_key=api_key)

# --- THE APP UI ---
st.title("📧 The Angry Email Fixer")
st.write("Powered by Groq (Llama 3)")

# Input: The angry text
user_text = st.text_area("Paste your angry email here:", height=150)

# Input: The Tone Slider
tone_level = st.slider("Select Tone Severity", 0, 10, 5)

# Tone Logic
tone_description = ""
if tone_level < 3:
    tone_description = "very friendly, warm, and casual"
elif tone_level < 7:
    tone_description = "professional, concise, and corporate"
else:
    tone_description = "strict, firm, and formal"

st.write(f"Target Tone: **{tone_description}**")

# --- THE MAGIC ---
if st.button("Fix My Email"):
    if user_text:
        my_prompt = f"""
        Act as a professional corporate communications expert.
        Rewrite the following text to be {tone_description}.
        
        Rules:
        1. Remove all insults and aggressive language.
        2. Keep the core request or message clear.
        3. Do not add any explanation, just give the rewritten text.
        
        Original Text: "{user_text}"
        """

        try:
            with st.spinner("Polishing your words..."):
                # Call Groq (Llama 3 model)
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "user", "content": my_prompt}
                    ],
                    model="llama-3.3-70b-versatile",  # This is the fast, free model
                )
                
                # Get Result
                result = chat_completion.choices[0].message.content
                
                # Show Result
                st.success("Fixed!")
                st.text_area("Your new email:", result, height=150)
                
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text first.")