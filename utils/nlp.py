import re
from typing import List, Set
import nltk


for pkg in ["punkt", "punkt_tab"]:
    try:
        nltk.data.find(f"tokenizers/{pkg}")
    except LookupError:
        nltk.download(pkg)

def tokenize(text: str) -> List[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\- ]+", " ", text)
    tokens = nltk.word_tokenize(text)
    return [t for t in tokens if len(t) > 1]

def extract_skills(tokens: List[str], skills_master: Set[str]) -> Set[str]:
    toks = set(tokens)
    found = set()
    joined = " ".join(tokens)
    for skill in skills_master:
        s = skill.lower().strip()
        if " " in s:
            if s in joined:
                found.add(skill)
        else:
            if s in toks:
                found.add(skill)
    return found
