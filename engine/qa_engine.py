from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad", framework="tf")

def answer_question(context, question):
    result = qa_pipeline(question=question, context=context)
    answer = result['answer']
    start = context.find(answer)
    justification = "Answer found in context" if start != -1 else "Answer inferred from overall document"
    return answer, justification
