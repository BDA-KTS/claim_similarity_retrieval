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

# Step 5: Load the file with input sentences by filename only
input_filename = input("Enter the name of the input file (CSV or TSV) located in the current directory: ")
input_file_path = os.path.join(os.getcwd(), input_filename)

input_df = pd.read_csv(input_file_path, sep=',' if input_filename.endswith('.csv') else '\t')
input_df['input_sentence'] = input_df['input_sentence'].str.replace('\x00', '', regex=True)

# Step 6: Process each input sentence, calculate similarity, and store results
results = []

# Set the default number of top claims to display
top_x = 3

for _, row in input_df.iterrows():
    user_sentence = row['input_sentence']
    user_embedding = model.encode(user_sentence)
    
    # Calculate cosine similarity between user input and each claim in the dataset
    df['similarity'] = df['embeddings'].apply(lambda x: cosine_similarity([x], [user_embedding])[0][0])
    
    # Sort claims by similarity and get top results
    top_similar_claims = df.sort_values(by='similarity', ascending=False).head(top_x)
    
    # Check if the highest similarity is above 0.7 and prepare the results
    if top_similar_claims.iloc[0]['similarity'] < 0.7:
        message = "No claims are found to be very similar (above 0.7), however, the most similar ones are displayed."
    else:
        message = ""
    
    # Collect the results for each input sentence
    for _, claim_row in top_similar_claims.iterrows():
        results.append({
            'input_sentence': user_sentence,
            'claimReview_source': claim_row['claimReview_source'],
            'claimReview_claimReviewed': claim_row['claimReview_claimReviewed'],
            'similarity': claim_row['similarity'],
            'message': message
        })

# Step 7: Output results to a CSV file
output_df = pd.DataFrame(results)
output_file = 'similarity_results.csv'
output_df.to_csv(output_file, index=False)

print(f"Results have been saved to {output_file}")
