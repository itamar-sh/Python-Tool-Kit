from transformers import pipeline

def summarize_hebrew(text):
    summarizer = pipeline("summarization", model="ibm/mt5-small-summarizer-hebrew")
    summary = summarizer(text, max_length=100, min_length=20, do_sample=False)
    return summary[0]["summary_text"]

# Example usage
with open("transcript_first14.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

summary = summarize_hebrew(transcript)
print("Summary:", summary)
