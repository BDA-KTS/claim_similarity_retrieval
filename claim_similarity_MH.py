import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load your dataset (Assumed to be a TSV file with a 'claimReview_claimReviewed' column)
df = pd.read_csv(r'C:\Users\gangopsa\Documents\claimskg\claimskg-generator-tsv\sebastian_topics\latest_output_topic classification\paper new\claim_similarity_dataset.tsv', sep='\t')

# Extract the sentences from the DataFrame
sentences = df['claimReview_claimReviewed'].tolist()

# Step 2: Load the pre-trained Sentence Transformer model
# This model will be used to generate sentence embeddings
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Step 3: Generate embeddings for all sentences in the DataFrame
# Apply the model to the 'claimReview_claimReviewed' column and generate embeddings for each sentence
df['embeddings'] = df['claimReview_claimReviewed'].apply(lambda sentence: model.encode(sentence))

# Step 4: Take user input (a sentence) to compare with the dataset
user_input = input("Enter a sentence: ")

# Step 5: Generate the embedding for the user input sentence
# This creates a vector representation (embedding) of the input sentence
user_embedding = model.encode(user_input)

# Step 6: Calculate the cosine similarity between the user input embedding and the embeddings in the DataFrame
# Cosine similarity compares how similar two vectors (embeddings) are; a value closer to 1 indicates higher similarity
df['similarity'] = df['embeddings'].apply(lambda x: cosine_similarity([x], [user_embedding])[0][0])

# Step 7: Filter sentences that have a cosine similarity greater than a certain threshold (e.g., 0.85 in this case)
# You can adjust the threshold based on how strict you want the similarity comparison to be
similar_sentences = df[df['similarity'] > 0.85]

# Step 8: Display the sentences with high similarity
# You can choose which columns to display, such as the original claim, its source, and the similarity score
print("Sentences with more than 0.85 cosine similarity:")
print(similar_sentences[['claimReview_source', 'claimReview_claimReviewed', 'similarity']])
