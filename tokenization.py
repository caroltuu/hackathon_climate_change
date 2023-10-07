from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def tokenize_text(text):
    encoded_text = tokenizer(text, return_tensors='pt', padding = True, truncation = True)
    return encoded_text