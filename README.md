
# 🧠 Skill Extractor — Resume Analyzer

A Streamlit web app that parses resumes, extracts skills, and ranks them against predefined job roles.
---
## ✨ Features
- Upload resumes in *PDF / DOCX / TXT* formats  
- Extract text using [PyResparser](https://github.com/OmkarPathak/pyresparser) (or fallback to PDF/DOCX reader)  
- Tokenize and detect skills with *NLTK*  
- Compare against job roles defined in data/roles.json  
- Show missing and recommended skills  
- Download results as CSV  
- (Optional) Save results to a MySQL database (local only)

---

## 📂 Project Structure

skill-extractor-starter/ │ ├─ app.py                # Main Streamlit app ├─ requirements.txt      # Python dependencies ├─ data/ │   ├─ skills_master.csv │   └─ roles.json ├─ assets/ │   └─ sample_resume.txt ├─ utils/ │   ├─ db.py             # MySQL helper (optional) │   ├─ nlp.py            # Tokenization & skill detection │   ├─ matching.py       # Role scoring logic │   └─ parsing.py        # Resume text extraction └─ .streamlit/ └─ secrets.toml      # Local DB secrets (ignored by git)

---
## 🚀 Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/<your-username>/skill-extractor.git
cd skill-extractor

2️⃣ Create & activate a virtual environment

python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# or Command Prompt
.\.venv\Scripts\activate

3️⃣ Install dependencies

pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt punkt_tab

4️⃣ Run locally

streamlit run app.py
---
🌐 Deployment (Streamlit Cloud)
1. Push this repo to GitHub.
2. Log in to Streamlit Cloud.
3. Click New app, pick your repo, and set app.py as the entrypoint.
4. If you don’t use a database online, keep the save_result() line commented out.
> If you want DB support online, use a public MySQL provider (e.g. PlanetScale) and add credentials in the app’s Secrets.




---

📸 Screenshots

(Add screenshots of your app analysing a resume and the results table here)

<img width="1259" height="761" alt="Screenshot 2025-09-14 130610" src="https://github.com/user-attachments/assets/c03d7c55-714f-4471-8f06-40679310c48b" />

<img width="1160" height="749" alt="Screenshot 2025-09-14 130725" src="https://github.com/user-attachments/assets/2e6119ae-123b-4a13-a70f-b862c8f7fd43" />


<img width="1005" height="800" alt="Screenshot 2025-09-14 130755" src="https://github.com/user-attachments/assets/39ed567d-60a2-4cc6-be50-614f5720346e" />


## 🌐 Live Demo
👉 [Open the App](https://skill-extractor-e6xucufw7jq9t8yktuysrf.streamlit.app/)
---

