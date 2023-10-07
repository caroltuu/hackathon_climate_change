import torch
from tokenization import tokenize_text
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from torch.utils.data import DataLoader, TensorDataset, random_split
from sklearn.metrics.pairwise import cosine_similarity
import database


#all mentions of "user input" must be replaced
#encoded_user_input = tokenizer(user_input, return_tensors='pt', padding=True, truncation = True)
#encoded_course_descriptions = [tokenizer(desc[1], reutrn_tensors='pt', padding = True, truncation = True) for desc in course_descriptions]
#encoded_course_descrptions = [tokenizer(desc[1], return_tensor='pt', padding=True)]

similarities = [cosine_similarity()]



courses = database.create_course_table()
database.insert_course('FNCE101', 'This is a finance class.', 'Lecture 1')
course_descriptions = database.get_courses()
print(course_descriptions)