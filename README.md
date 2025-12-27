# 📧 AI-Powered Angry Email Fixer

![Python](https://img.shields.io/badge/Language-Python_3.10%2B-blue)
![AI Model](https://img.shields.io/badge/AI_Model-Llama_3.3_(Groq)-orange)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)

## 📋 Project Overview
The **Angry Email Fixer** is a corporate communication tool designed to save your career.

We've all been there: You are angry at a client or boss, and you write a rude email. This tool acts as a "filter" between your brain and the send button. It uses **Generative AI (Llama 3 via Groq)** to rewrite aggressive text into professional, polite, and corporate-standard language instantly.

> **Key Highlight:** This system uses the **Groq LPU Engine**, meaning it rewrites emails in milliseconds (near real-time) and costs $0 to run.

---

## 🚀 Key Features
* **🎛️ Tone Slider:** Adjust the output severity from "Friendly & Warm" (0) to "Strict & Formal" (10).
* **⚡ Instant Inference:** Powered by Groq, providing results faster than you can blink.
* **🔒 Secure Architecture:** API keys are managed via Streamlit Secrets, keeping credentials safe from GitHub bots.
* **📱 Responsive UI:** Clean, simple interface that works on desktop and mobile browsers.

---

## 🛠️ Tech Stack
| Component | Technology Used | Why? |
| :--- | :--- | :--- |
| **Core Logic** | Python | Easy to read, dominant language for AI. |
| **AI Engine** | Groq (Llama-3.3-70b) | Fastest inference on the market & Free tier available. |
| **Interface** | Streamlit | Turns Python scripts into web apps instantly. |
| **Security** | TOML Secrets | Industry standard for hiding API keys. |

---

## ⚙️ How It Works (Logic Flow)

1.  **Input:** User types: *"This report is garbage, fix it now!"*
2.  **Tone Analysis:** User selects **Severity Level 2** (Friendly).
3.  **Prompt Engineering:** The app wraps the text in a system prompt:
    > *"Act as a corporate expert. Rewrite this text to be warm and casual..."*
4.  **AI Processing:** Groq processes the request in <0.5 seconds.
5.  **Output:** *"Hey! Thanks for the report. I think we need to tweak a few things..."*

---

## 📦 How to Run This Project

### Prerequisites
1.  **Python** installed.
2.  A free **Groq API Key** (Get it [here](https://console.groq.com/keys)).

### Installation Steps
1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Subhaga2000/email-fixer.git](https://github.com/Subhaga2000/email-fixer.git)
    cd email-fixer
    ```

2.  **Install Dependencies**
    *(This installs Streamlit and Groq automatically)*
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Security** (Crucial!)
    * Create a folder named `.streamlit` in the main folder.
    * Inside it, create a file named `secrets.toml`.
    * Paste your key:
    ```toml
    GROQ_API_KEY = "gsk_YourActualKeyHere..."
    ```

4.  **Run the App**
    ```bash
    streamlit run main.py
    ```

---

## 🔮 Future Enhancements
* [ ] Add a "Copy to Clipboard" button for one-click sending.
* [ ] Add "Email Type" selector (Slack message vs. Official Letter).
* [ ] Integrate Outlook/Gmail API to send directly from the app.

---

## 👨‍💻 Author
Built by **Subhaga Hansamana**