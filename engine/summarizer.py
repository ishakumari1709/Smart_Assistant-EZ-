from transformers import pipeline

summarizer = pipeline("summarization", model="google/pegasus-xsum", framework="tf")

def generate_summary(text):
    max_input = 1024
    text = text[:max_input]
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return summary
