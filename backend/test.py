from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import database
import pandas as pd

# 1. Load pre-trained BERT model and tokenizer
model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model.eval()

# Function to get embedding of a sentence
def get_embedding(sentence):
    tokens = tokenizer(sentence, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**tokens)
    return outputs['last_hidden_state'][0, 0].numpy()  # [CLS] token embedding

# 2. Tokenize descriptions
courses_data = [
        {"course_name": "Python Basics",
         "description": "A beginner's guide to Python. Learn about variables, loops, and functions."},
        {"course_name": "Advanced Python",
         "description": "Delve deeper into Python. Explore OOP, decorators, and generators."},
        {"course_name": "JavaScript Essentials",
         "description": "Discover the world of JavaScript and its dynamic capabilities."},
        {"course_name": "Deep Dive into Deep Learning",
         "description": "Explore neural networks, CNNs, RNNs, and other advanced ML techniques."},
        {"course_name": "Web Development with Flask",
         "description": "Learn how to create web applications using Flask, a micro web framework."},
        {"course_name": "React for Frontend",
         "description": "Master the React framework for building interactive UIs."},
        {"course_name": "Databases with SQL",
         "description": "Learn how to structure, query, and manage data with SQL."},
        {"course_name": "Game Development with Unity", "description": "Build interactive games using Unity and C#."},
        {"course_name": "Mobile Apps with Flutter",
         "description": "Design and develop mobile applications using Flutter and Dart."},
        {"course_name": "Cloud Computing with AWS",
         "description": "Discover the tools and services offered by AWS for cloud solutions."}
    ]

df = pd.read_csv('courses.csv')


# Extract course descriptions
course_descriptions = df['description']
input_description = "Learn the foundations of the Python language, including variables, loops, and functions."
input_embedding = get_embedding(input_description)
database_embeddings = [get_embedding(desc) for desc in course_descriptions]

# 3. & 4. Calculate similarities
similarities = [cosine_similarity([input_embedding], [db_emb]) for db_emb in database_embeddings]
print(similarities)
# 5. Rank and retrieve
top_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)[:10]
top_descriptions = [course_descriptions[i] for i in top_indices]
print(top_descriptions)