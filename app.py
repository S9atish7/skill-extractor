import json, io
import pandas as pd
import streamlit as st

from utils.parsing import extract_text_from_file
from utils.nlp import tokenize, extract_skills
from utils.matching import score_roles
from utils.db import save_result

# Try to use PyResparser (spaCy) if available
ENABLE_PYRESPARSER = True
try:
    from pyresparser import ResumeParser
except Exception:
    ENABLE_PYRESPARSER = False

# ---------------- Streamlit UI ---------------- #
st.set_page_config(page_title="Skill Extractor", page_icon="🧠")
st.title("🧠 Skill Extractor — Resume Analyzer")
st.caption("Upload a PDF/DOCX/TXT resume to extract skills and see role fit.")

with st.expander("ℹ How it works"):
    st.write(
        "1) Extract text from your resume (PyResparser if available, or a fallback).\n"
        "2) Tokenize and match against a curated skills list (data/skills_master.csv).\n"
        "3) Compare your skills with role templates in data/roles.json and compute a match score."
    )

# Upload or use sample resume
colA, colB = st.columns([3, 1])
uploaded = colA.file_uploader("Upload resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
use_sample = colB.button("Use sample resume")

# Load skills & roles
skills_master = set(pd.read_csv("data/skills_master.csv")["skill"].str.lower().tolist())
roles = json.load(open("data/roles.json", "r"))

if use_sample:
    with open("assets/sample_resume.txt", "rb") as f:
        uploaded = io.BytesIO(f.read())
        uploaded.name = "sample_resume.txt"

# ---------------- Processing ---------------- #
if uploaded:
    st.subheader("📄 Parsed Resume")
    raw_text = ""
    meta = {}

    # Try PyResparser first
    if ENABLE_PYRESPARSER:
        try:
            st.write("Using *PyResparser* for structured extraction…")
            content = uploaded.read()
            uploaded.seek(0)
            tmp = "tmp_resume.bin"
            with open(tmp, "wb") as f:
                f.write(content)
            meta = ResumeParser(tmp).get_extracted_data() or {}
            raw_text = meta.get("text", "") or ""
        except Exception as e:
            st.warning(f"PyResparser failed ({e}). Falling back to plain text extraction.")
            raw_text = extract_text_from_file(uploaded)
    else:
        raw_text = extract_text_from_file(uploaded)

    if not raw_text:
        st.error("Couldn't extract text from the file. Try a different format.")
        st.stop()

    with st.expander("Show raw text"):
        st.text_area("Resume text", raw_text[:5000], height=300)

    # -------- Skills & Roles -------- #
    tokens = tokenize(raw_text)
    found_skills = extract_skills(tokens, skills_master)

    st.subheader("🧩 Detected Skills")
    if found_skills:
        st.write(", ".join(sorted(found_skills)))
    else:
        st.info("No skills matched our list. Consider expanding data/skills_master.csv.")

    # Score roles
    results = score_roles(found_skills, roles)
    st.subheader("🏁 Role Fit Ranking")
    df = pd.DataFrame(results)
    st.dataframe(
        df[["role", "score", "matched_required", "total_required",
            "matched_nice", "total_nice"]],
        use_container_width=True
    )

    # ✅ Save best result to MySQL
    if results:
        best = results[0]
        save_result(uploaded.name, best["role"], best["score"], found_skills)

    # -------- Recommendations -------- #
    st.markdown("---")
    st.subheader("🔍 Recommendations (Top 3)")
    for row in results[:3]:
        st.markdown(f"### {row['role']} — {row['score']}% fit")
        if row["missing_required"]:
            st.write("*Missing required skills:* ", ", ".join(row["missing_required"]))
        if row["suggested_skills"]:
            st.write("*Good to learn next:* ", ", ".join(row["suggested_skills"]))

    # -------- Export -------- #
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇ Download results (CSV)", csv, "role_fit_results.csv", "text/csv")

    # -------- Coverage -------- #
    st.markdown("---")
    st.subheader("📈 Keyword Coverage Signal")
    coverage = round(100 * len(found_skills) / max(len(skills_master), 1), 2)
    st.write(f"Coverage vs. master list: *{coverage}%* (tune via data/skills_master.csv)")
else:
    st.info("Upload a resume or click *Use sample resume* to try it.")