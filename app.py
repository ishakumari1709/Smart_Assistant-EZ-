import streamlit as st
from engine.file_utils import read_file
from engine.summarizer import generate_summary
from engine.qa_engine import answer_question
from engine.challenge_engine import generate_questions, evaluate_answer

st.set_page_config(page_title="Smart Assistant", layout="wide")

st.title("📄 Smart Assistant for Research Documents")
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    text = read_file(uploaded_file)
    st.subheader("📌 Summary (≤ 150 words)")
    summary = generate_summary(text)
    st.write(summary)

    mode = st.radio("Choose Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        question = st.text_input("Ask a question based on the document:")
        if question:
            answer, justification = answer_question(text, question)
            st.markdown(f"**Answer:** {answer}")
            st.markdown(f"🧾 Justification: {justification}")

    elif mode == "Challenge Me":
        st.info("Generating questions...")
        questions = generate_questions(text, 3)
        user_answers = []

        for i, q in enumerate(questions):
            st.markdown(f"**Q{i + 1}:** {q}")
            user_input = st.text_input(f"Your Answer to Q{i + 1}", key=f"ua_{i}")
            user_answers.append((q, user_input))

        if st.button("Evaluate Answers"):
            for i, (q, ua) in enumerate(user_answers):
                score, feedback = evaluate_answer(text, q, ua)
                st.markdown(f"**Q{i + 1} Score:** {score}/10")
                st.markdown(f"🧾 Feedback: {feedback}")
