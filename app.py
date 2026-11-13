import streamlit as st
import json
import random

st.set_page_config(page_title="Company-Smart Mock Interview Coach", page_icon="🎯", layout="centered")
st.title("🎯 Company-Smart Mock Interview Coach")
st.write("Practice company-style interviews, answer questions, and receive simple keyword-based feedback.")

QUESTION_BANK = {
    "Software Engineer": [
        {"question": "Explain the difference between a list and a tuple in Python.", "keywords": ["mutable", "immutable", "list", "tuple"]},
        {"question": "What is time complexity? Explain with an example.", "keywords": ["time", "input", "complexity", "big o"]},
        {"question": "What is object-oriented programming?", "keywords": ["class", "object", "encapsulation", "inheritance"]},
    ],
    "AI/ML Engineer": [
        {"question": "What is the difference between supervised and unsupervised learning?", "keywords": ["label", "data", "supervised", "unsupervised", "pattern"]},
        {"question": "What is overfitting and how can you reduce it?", "keywords": ["training", "test", "generalization", "regularization"]},
        {"question": "Explain the purpose of train-test split.", "keywords": ["training", "testing", "evaluate", "unseen"]},
    ],
    "Data Analyst": [
        {"question": "What is the difference between SQL WHERE and HAVING?", "keywords": ["where", "having", "group", "aggregate"]},
        {"question": "How would you handle missing data?", "keywords": ["missing", "remove", "impute", "mean", "median"]},
        {"question": "What is a KPI? Give an example.", "keywords": ["key performance", "indicator", "metric", "measure"]},
    ],
    "Python Developer": [
        {"question": "What are Python functions and why do we use them?", "keywords": ["function", "reuse", "parameter", "return"]},
        {"question": "Explain exception handling in Python.", "keywords": ["try", "except", "error", "finally"]},
        {"question": "What is a dictionary in Python?", "keywords": ["key", "value", "mapping", "mutable"]},
    ],
}

company = st.selectbox("Choose a company style", ["General", "Google-style", "Microsoft-style", "Amazon-style", "Infosys-style"])
role = st.selectbox("Choose job role", list(QUESTION_BANK.keys()))
if "questions" not in st.session_state or st.session_state.get("role") != role:
    st.session_state.questions = random.sample(QUESTION_BANK[role], k=len(QUESTION_BANK[role]))
    st.session_state.role = role
    st.session_state.answers = [""] * len(st.session_state.questions)

st.caption(f"Company style: {company} • Role: {role} • Demo question bank")
with st.form("interview_form"):
    for i, item in enumerate(st.session_state.questions):
        st.subheader(f"Question {i + 1}")
        st.write(item["question"])
        st.session_state.answers[i] = st.text_area("Your answer", value=st.session_state.answers[i], key=f"answer_{role}_{i}", height=110)
    submitted = st.form_submit_button("Submit interview")

if submitted:
    total_score = 0
    feedback = []
    for i, item in enumerate(st.session_state.questions):
        answer = st.session_state.answers[i].lower()
        matched = [word for word in item["keywords"] if word in answer]
        score = round((len(matched) / len(item["keywords"])) * 10) if item["keywords"] else 0
        total_score += score
        feedback.append({"question": item["question"], "score": score, "matched_keywords": matched, "suggestion": "Add more relevant concepts and explain with an example." if score < 7 else "Good coverage. Make your answer clearer with a concise example."})
    average = round(total_score / len(feedback), 1)
    st.success(f"Interview completed! Average demo score: {average}/10")
    for i, item in enumerate(feedback):
        st.markdown(f"**Q{i + 1} score: {item['score']}/10**")
        st.write("Matched keywords:", ", ".join(item["matched_keywords"]) or "None detected")
        st.write(item["suggestion"])
    report = {"company_style": company, "role": role, "average_score": average, "feedback": feedback}
    st.download_button("Download feedback report (JSON)", data=json.dumps(report, indent=2), file_name="interview_report.json", mime="application/json")

st.info("This is an academic demo prototype. Scores are based on keyword matching, not an AI evaluator. An institution's historical interview archive can be integrated when the data is provided.")
