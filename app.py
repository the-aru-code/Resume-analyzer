import streamlit as st
from utils import extract_text_from_pdf, clean_text, calculate_similarity, skill_match

# Job Role Skills
job_roles = {
    "Python Developer": [
        "python", "django", "flask", "sql", "git", "api", "numpy", "pandas"
    ],
    "Frontend Developer": [
        "html", "css", "javascript", "react", "bootstrap", "git"
    ],
    "Data Analyst": [
        "python", "excel", "sql", "power bi", "tableau", "pandas"
    ]
}

st.title("AI Resume Skill Gap Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
job_role = st.selectbox("Select Job Role", list(job_roles.keys()))

if st.button("Analyze Resume") and uploaded_file:
    raw_text = extract_text_from_pdf(uploaded_file)
    clean_resume = clean_text(raw_text)

    skills = job_roles[job_role]
    score = calculate_similarity(clean_resume, skills)
    matched, missing = skill_match(clean_resume, skills)

    st.subheader("Results")
    st.write(f"🔍 Resume Match Score: *{score}%*")
    st.success(f"✅ Matched Skills: {', '.join(matched)}")
    st.error(f"❌ Missing Skills: {', '.join(missing)}")
