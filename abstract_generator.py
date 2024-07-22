import gradio as gr
from PyPDF2 import PdfFileReader
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re

#load trained model
tokenizer = AutoTokenizer.from_pretrained("vardhan-rawat/autotrain-BART-ARXIV")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = AutoModelForSeq2SeqLM.from_pretrained("vardhan-rawat/autotrain-BART-ARXIV").to(device)

# Function to generate abstract
def generate_abstract(pdf_file):
    try:
        text = ""
        with open(pdf_file.name, "rb") as f:
            reader = PdfFileReader(f)
            for page in range(reader.numPages):
                text += reader.getPage(page).extractText()

        text = " ".join(text.split())
        print(text)
        # Summary Generation
        inputs = tokenizer.encode(text, max_length=1024, return_tensors='pt', truncation=True).to(device)
        summary_ids = model.generate(inputs, num_beams=4, min_length=250, max_length=300, early_stopping=True)
        abstract = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        # Clean the summary
        cleaned_abstract = re.sub(r'\s+', ' ', abstract).strip()  # Remove extra whitespace

        return cleaned_abstract
    except Exception as e:
        return f"Error: {str(e)} \nPlease check file size and type!"

# Gradio Interface
input_component = gr.File(label="Upload PDF file")
output_component = gr.Textbox(label="Summarized Text")

title = "Abstract Generator (BART)"
description = "<h2>Upload a PDF file to generate abstract.</h2>"

Interface = gr.Interface(fn=generate_abstract, inputs=input_component, outputs=output_component, title=title, description=description)
Interface.launch(share=True)
