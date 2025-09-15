# 🧠 Skill Extractor — Resume Analyzer

A Streamlit web app that parses resumes, extracts skills, and ranks them against predefined job roles.

---

## ✨ Features
- Upload resumes in **PDF / DOCX / TXT** formats  
- Extract text using [PyResparser](https://github.com/OmkarPathak/pyresparser) (or fallback to PDF/DOCX reader)  
- Tokenize and detect skills with **NLTK**  
- Compare against job roles defined in `data/roles.json`  
- Show missing and recommended skills  
- Download results as CSV  
- *(Optional)* Save results to a MySQL database (local only)

---

## 📂 Project Structure
```

skill-extractor-starter/
│
├─ app.py                # Main Streamlit app
├─ requirements.txt      # Python dependencies
├─ data/
│   ├─ skills\_master.csv
│   └─ roles.json
├─ assets/
│   └─ sample\_resume.txt
├─ utils/
│   ├─ db.py             # MySQL helper (optional)
│   ├─ nlp.py            # Tokenization & skill detection
│   ├─ matching.py       # Role scoring logic
│   └─ parsing.py        # Resume text extraction
└─ .streamlit/
└─ secrets.toml      # Local DB secrets (ignored by git)

````

---

## 🚀 Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/<your-username>/skill-extractor.git
cd skill-extractor
````

### 2️⃣ Create & activate a virtual environment

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# or Command Prompt
.\.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt punkt_tab
```

### 4️⃣ Run locally

```bash
streamlit run app.py
```

---

## 🌐 Deployment (Streamlit Cloud)

1. Push this repo to GitHub.
2. Log in to [Streamlit Cloud](https://share.streamlit.io).
3. Click **New app**, pick your repo, and set `app.py` as the entrypoint.
4. If you don’t use a database online, keep the `save_result()` line commented out.

> If you want DB support online, use a public MySQL provider (e.g. PlanetScale) and add credentials in the app’s **Secrets**.

---

## 📸 Screenshots

<img src="https://github.com/user-attachments/assets/538fbc9c-8f69-4fb0-b56b-74808351f329" alt="Resume Analysis" width="800">

<img src="https://github.com/user-attachments/assets/74806b64-b245-4e25-83a1-a54cd793a1e8" alt="Role Fit Results" width="800">

<img src="https://github.com/user-attachments/assets/37a276dd-cd8a-42ee-beba-b2fc4103546f" alt="Keyword Coverage" width="800">


---

## 🌐 Live Demo

👉 [Open the App](https://skill-extractor-e6xucufw7jq9t8yktuysrf.streamlit.app/)

---

## 📝 License

MIT License © 2025 Your Name

```

---

### How to use this

1. Create a folder in your repo (for example `images`) and upload your three screenshots there.  
2. Edit the `![]()` paths above to match the names of the images (or paste the GitHub `?raw=true` link).  
3. Save and commit your README.

When you refresh your repo’s main page, the screenshots will appear under “📸 Screenshots”.
```
