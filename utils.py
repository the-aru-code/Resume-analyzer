import pdfplumber
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')

# ----- Resume Text Extraction -----
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# ----- Text Preprocessing -----
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return " ".join(words)

# ----- TF-IDF + Cosine Similarity -----
def calculate_similarity(resume_text, skills):
    documents = [resume_text, " ".join(skills)]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(similarity[0][0] * 100, 2)

# ----- Skill Matching -----
def skill_match(resume_text, skills):
    matched = []
    missing = []
    for skill in skills:
        if skill.lower() in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)
    return matched, missing
