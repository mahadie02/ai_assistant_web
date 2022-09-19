from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summ_txt(txt):
    summar = summarizer(txt, max_length=55, min_length=30, do_sample = False)
    summary = str(summar)
    summary = summary.replace("[","")
    summary = summary.replace("]","")
    summary = summary.replace("{","")
    summary = summary.replace("}","")
    summary = summary.replace("summary_text","")
    summary = summary.replace("'","")
    summary = summary.replace(":","")
    summary = summary.strip()
    return summary