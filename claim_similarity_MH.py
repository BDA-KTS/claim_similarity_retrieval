import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval
import pickle

# Step 1: Load your dataset (Assumed to be a TSV file with a 'claimReview_claimReviewed' column)
df = pd.read_csv(r'claim_similarity_dataset.tsv', sep='\t')

# Clean any null bytes from text data
df['claimReview_claimReviewed'] = df['claimReview_claimReviewed'].str.replace('\x00', '', regex=True)

# Step 2: Load the pre-trained Sentence Transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Step 3: Generate and store embeddings (only if not already saved)
if 'embeddings' not in df.columns:
    print("Generating embeddings for all claims...")
    df['embeddings'] = df['claimReview_claimReviewed'].apply(lambda sentence: model.encode(sentence).tolist())
    # Save as Pickle to avoid CSV/TSV serialization issues
    df.to_pickle('claims_with_embeddings.pkl')

# Step 4: Load the dataset with embeddings safely
df = pd.read_pickle('claims_with_embeddings.pkl')

# Step 5: Take user input
user_input = input("Enter a sentence: ")
user_embedding = model.encode(user_input)

# Step 6: Calculate cosine similarity
df['similarity'] = df['embeddings'].apply(lambda x: cosine_similarity([x], [user_embedding])[0][0])

# Step 7: Get the number of top claims to display
top_x = input("Enter the number of top similar claims to display (default 3): ")
top_x = int(top_x) if top_x.isdigit() else 3

# Step 8: Sort claims by similarity
df_sorted = df.sort_values(by='similarity', ascending=False).head(top_x)

# Step 9: Print results or fallback message
if df_sorted.iloc[0]['similarity'] < 0.7:
    print("No claims are found to be very similar (above 0.7), however, the most similar ones are displayed.")

print(f"\nTop {top_x} most similar claims:")
print(df_sorted[['claimReview_source', 'claimReview_claimReviewed', 'similarity']])
