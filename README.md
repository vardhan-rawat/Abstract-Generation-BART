
# Research Paper Abstract Generator

This project focuses on generating abstracts for research paper PDFs using a fine-tuned BART (Bidirectional and Auto-Regressive Transformers) model. The BART model was specifically trained on the ArXiv dataset to produce concise and coherent abstracts from lengthy research articles.

## Project Description

The Research Paper Abstract Generator leverages state-of-the-art natural language processing techniques to automate the creation of abstracts for research papers. By fine-tuning the BART model, this tool aims to provide researchers and academicians with a way to swiftly generate abstracts, thus saving time and effort.

## Tools and Technologies

- **Model:** BART (Bidirectional and Auto-Regressive Transformers)
- **Training Framework:** Hugging Face AutoTrain
- **Dataset:** ArXiv Dataset
- **User Interface:** Gradio
- **Hosted Model:** [vardhan-rawat/autotrain-BART-ARXIV](https://huggingface.co/vardhan-rawat/autotrain-BART-ARXIV)

## Training Process

### Dataset Preparation

The ArXiv dataset was processed with the following steps:

1. **Dataset Reduction:** 
   - The dataset size was reduced for efficient processing using the script `reduce_dataset.py`.
2. **Dataset Cleaning:** 
   - The dataset was cleaned and structured with the following features:
     - **Feature:** `article_text` (The main text of the research paper)
     - **Label:** `abstract_text` (The corresponding abstract of the paper)
   - Cleaning was performed using the script `clean.py`.

### Model Training

The cleaned dataset, consisting of 419 research papers for training and 92 for validation, was used to fine-tune the BART model using Hugging Face AutoTrain. The training involved adjusting the model parameters to optimize the generation of abstracts from the provided article texts.

## Model Hyperparameters

The following hyperparameters were used during the model training:

- **Learning rate:** 5e-5
- **Epochs:** 5
- **Max sequence length:** 512
- **Max target length:** 256
- **Batch size:** 2
- **Gradient accumulation:** 4
- **Optimizer:** AdamW
- **Scheduler:** Linear
- **PEFT:** False
- **Mixed precision:** FP16
- **Training task:** Seq2Seq

## Model Validation Metrics

The model's performance was evaluated using the following metrics:

- **Loss:** 3.3053
- **ROUGE-1:** 40.9946
- **ROUGE-2:** 12.5208
- **ROUGE-L:** 22.015
- **ROUGE-Lsum:** 36.2757

To know more about ROUGE scores, refer to the [link in the References](#references).

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/research-paper-abstract-generator.git
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have your Hugging Face token ready. You can get it from your [Hugging Face account](https://huggingface.co/settings/tokens).

4. Run the abstract generator:
   ```bash
   python abstract_generator.py --hf_token YOUR_HUGGING_FACE_TOKEN
   ```

## User Interface

A user-friendly interface has been implemented using Gradio. Users can upload a PDF file of a research paper without an abstract, and the tool will generate an abstract for it.

## References

- [ArXiv Dataset](https://www.kaggle.com/Cornell-University/arxiv)
- [BART Research Paper](https://arxiv.org/abs/1910.13461)
- [Article Explaining ROUGE Scores](https://medium.com/@eren9677/text-summarization-387836c9e178)
- [Hugging Face AutoTrain Documentation](https://huggingface.co/docs/autotrain/en/index)
