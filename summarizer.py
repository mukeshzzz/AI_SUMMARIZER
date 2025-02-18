from transformers import pipeline
from multiprocessing import Pool

def chunk_text(text, chunk_size=300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def summarize_chunk(chunk):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
    return summary[0]["summary_text"]

def summarize_text(text):
    chunks = chunk_text(text)
    with Pool(processes=4) as pool:
        summaries = pool.map(summarize_chunk, chunks)
    return " ".join(summaries)