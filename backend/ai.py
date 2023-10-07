import torch
from tokenization import tokenize_text
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from torch.utils.data import DataLoader, TensorDataset, random_split
from sklearn.metrics.pairwise import cosine_similarity
import database
import app
from flask import session

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

course_descriptions = database.get_descriptions()
user_input = #need

#all mentions of "user input" must be replaced
encoded_user_input = tokenizer(user_input, return_tensors='pt', padding=True, truncation = True)
encoded_course_descriptions = [tokenizer(desc[1], reutrn_tensors='pt', padding = True, truncation = True) for desc in course_descriptions]

similarities = [cosine_similarity(encoded_user_input['input_ids'], desc_embedding['input_ids'])[0][0] for desc_embedding in encoded_course_descriptions]
filtered_courses = [course_descriptions[i][0] for i, score in enumerate(similarites) if score > 0.9]

if user_course_description:
    user_course_description = database.get_description(session.get('emailAddress'))
    encoded_user_course_description = tokenizer(user_course_description, return_tensors='pt', padding=True, truncation = True) 
    specific_similarity_scores = [
        cosine_similarity(encoded_user_course_description['input_ids'], desc_embedding['input_ids'][0][0]
        for desc_embedding in [tokenizer(desc[1], return_tensors='pt', padding=True, truncation=True) for desc in filtered_courses])
    ]
    recommendations=[filtered_courses[i] for i, score in enumerate(specific_similarity_scores) if score > refined_threshold]

else: 
    final_recommendations = filtered_courses

