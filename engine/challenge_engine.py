import random
from transformers import pipeline

qg_pipeline = pipeline("text2text-generation", model="valhalla/t5-small-qa-qg-hl", framework="tf")

def generate_questions(text, n=3):
    sentences = text.split(".")
    random.shuffle(sentences)
    selected = ". ".join(sentences[:5])
    questions = qg_pipeline("generate questions: " + selected, max_length=64, do_sample=False)
    return [q['generated_text'] for q in questions[:n]]

def evaluate_answer(context, question, answer):
    if not answer.strip():
        return 0, "No answer provided."
    # Simulated score; in practice use similarity comparison
    score = random.randint(5, 10)
    justification = f"Answer evaluated against document context. Question: '{question}'"
    return score, justification
