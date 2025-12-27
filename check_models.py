import google.generativeai as genai

# PASTE YOUR KEY HERE
genai.configure(api_key="AIzaSyDIwNmn7D9tWBEGcZe75ZaqtvncIUKGzfw")

print("Checking available models...")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)