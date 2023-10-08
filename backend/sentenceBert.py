from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def find_similar_courses(user_input, top_n=10):
    # Initialize the SBERT model
    model = SentenceTransformer('paraphrase-distilroberta-base-v1')

    # Extract course descriptions
    courses = pd.read_csv('courses.csv')
    descriptions = courses['description'].to_list()
    ids = courses['courseID'].to_list()
    names = courses['courseName'].to_list()
    schools = courses['school'].to_list()

    # Compute embeddings
    course_embeddings = model.encode(descriptions)

    # Compute the embedding for the user input
    user_embedding = model.encode([user_input])

    # Compute cosine similarities
    similarities = cosine_similarity(user_embedding, course_embeddings)

    # Get the top_n course indices
    top_courses_indices = np.argsort(similarities[0])[-top_n:]

    # Return the most similar courses
    return [[descriptions[i] for i in reversed(top_courses_indices)], [ids[i] for i in reversed(top_courses_indices)], [names[i] for i in reversed(top_courses_indices)], [schools[i] for i in reversed(top_courses_indices)], len(descriptions)]

