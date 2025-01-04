import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval
import pickle
import os

# Step 1: Load your dataset (Assumed to be a TSV file with a 'claimReview_claimReviewed' column)
df = pd.read_csv(r'claim_similarity_dataset.tsv', sep='\t')

# Clean any null bytes from text data
df['claimReview_claimReviewed'] = df['claimReview_claimReviewed'].str.replace('\x00', '', regex=True)

# Step 2: Load the pre-trained Sentence Transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Step 3: Generate and store embeddings for claims (only if not already saved)
if 'embeddings' not in df.columns:
    print("Generating embeddings for all claims...")
    df['embeddings'] = df['claimReview_claimReviewed'].apply(lambda sentence: model.encode(sentence).tolist())
    df.to_pickle('claims_with_embeddings.pkl')  # Save with embeddings

# Step 4: Load the dataset with embeddings safely
df = pd.read_pickle('claims_with_embeddings.pkl')

# Step 5: Get a single input sentence from the user or use a sample sentence
user_input = input("Enter a sentence for similarity check (or press Enter to use a sample sentence): ").strip()

if not user_input:
    user_sentence = "The daughter of U.S. Vice President Dick Cheney went to Iraq to become a human shield"
    print(f"No input provided. Using the sample sentence: '{user_sentence}'")
else:
    user_sentence = user_input

# Step 6: Process the input sentence, calculate similarity, and store results
results = []

# Encode the user's sentence
user_embedding = model.encode(user_sentence)

# Calculate cosine similarity between user input and each claim in the dataset
df['similarity'] = df['embeddings'].apply(lambda x: cosine_similarity([x], [user_embedding])[0][0])

# Sort claims by similarity and get top results
top_x = 3
top_similar_claims = df.sort_values(by='similarity', ascending=False).head(top_x)

# Check if the highest similarity is above 0.7 and prepare the results
if top_similar_claims.iloc[0]['similarity'] < 0.7:
    message = "No claims are found to be very similar (above 0.7), however, the most similar ones are displayed."
else:
    message = ""

# Collect the results for the input sentence
for _, claim_row in top_similar_claims.iterrows():
    results.append({
        'input_sentence': user_sentence,
        'claimReview_source': claim_row['claimReview_source'],
        'claimReview_claimReviewed': claim_row['claimReview_claimReviewed'],
        'normalised_rating': claim_row['normalised_rating'],
        'similarity': claim_row['similarity'],
        'message': message
    })

# Step 7: Output results to a CSV file
output_df = pd.DataFrame(results)
output_file = 'similarity_results.csv'
output_df.to_csv(output_file, index=False)

print(f"Results have been saved to {output_file}")
