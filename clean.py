import json
import re

# Function to clean text by removing <s></s> tags, unwanted characters, and occurrences of @xmath<anynumber> within 0 to 2912
def clean_text(text):
    if isinstance(text, list):
        text = ' '.join(text)
    text = re.sub(r'<S>|</S>', '', text)  
    text = re.sub(r'\n', ' ', text)  
    text = re.sub(r'@xmath(?:[0-9]|[1-9][0-9]|[1-9][0-9]{2}|[12][0-8][0-9][0-9]|291[0-2])', '', text)  #
    text = re.sub(r'@xcite', '', text)
    text = re.sub(r'\s+', ' ', text).strip()  
    text = re.sub(r'[^a-zA-Z0-9\s,.]', '', text)
    text = re.sub(r'\s+', ' ', text).strip() 
    return text

# Path to the input JSONL file
input_file_path = "TRAIN/VALIDATION FILE TO BE CLEANED PATH"
# Path to the output JSONL file
output_file_path = "CLEANED FILE PATH"

# Read the input JSONL file and extract, clean, and save the data
with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    for line in infile:
        json_data = json.loads(line)
        
        # Extract article_text and abstract_text
        article_text = json_data.get('article_text', [])
        abstract_text = json_data.get('abstract_text', "")
        
        # Clean article_text and abstract_text
        cleaned_article_text = clean_text(article_text)
        cleaned_abstract_text = clean_text(abstract_text)
        
        # Ensure that cleaned article_text and abstract_text are not empty
        if cleaned_article_text and cleaned_abstract_text:
            cleaned_entry = {
                'article_text': cleaned_article_text,
                'abstract_text': cleaned_abstract_text
            }
            # Write the cleaned entry to the output JSONL file
            outfile.write(json.dumps(cleaned_entry) + '\n')

print(f"Cleaned data has been saved to {output_file_path}")
