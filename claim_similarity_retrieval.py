import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval
import pickle
import os
import json


# Step 1: Read method parameters
with open('config.json', 'r') as file:
    config = json.load(file)



# Step 2: Load embeddings of the ClaimsKG dataset
model = SentenceTransformer(config["embedding_model"])

df = []
if os.path.exists(config["claims_dataset_embeddings"]):
    print("Loading pre-computed embeddings for the claimsKG dataset")
    df = pd.read_pickle(config["claims_dataset_embeddings"])
else:
    # Load your dataset (Assumed to be a TSV file with a 'claimReview_claimReviewed' column)
    df = pd.read_csv(confg["claims_dataset_path"], sep='\t')

    # Clean any null bytes from text data
    df['claimReview_claimReviewed'] = df['claimReview_claimReviewed'].str.replace('\x00', '', regex=True)


    # Load the pre-trained Sentence Transformer model
   

    # Generate and store embeddings for claims (only if not already saved)
    if 'embeddings' not in df.columns:
        print("Generating embeddings for all claims...")
        df['embeddings'] = df['claimReview_claimReviewed'].apply(lambda sentence: model.encode(sentence).tolist())
        df.to_pickle(config["claims_dataset_embeddings"])  # Save with embeddings
  
# Step 3: Read input queries
with open(config["input_queries_path"]) as f:
    input_queries = f.read().split('\n')

# Step 4: Generate query embeddings
query_embeddings = [model.encode(query) for query in input_queries]
#print(len(user_embedding), len(user_embedding[0]))

# Step 5: Compute cosine similarity for each queries with claims
top_query_claims = []

for i in range(len(query_embeddings)):
    df['similarity'] = df['embeddings'].apply(lambda x: cosine_similarity([x], [query_embeddings[i]]))

    cutoff_by, cutoff_values = config["cutoff_by"], config["cutoff_values"]
    
    try:
        idx = cutoff_values.index(cutoff_by)

        if cutoff_by == "topK":
            topK = config["topK"]
            top_query_claims.append(df.sort_values(by='similarity', ascending=False).head(topK))
        elif cutoff_by == "threshold":
            threshold =config["similarity_thresholds"]
            df = df.sort_values(by='similarity', ascending=False)
            top_query_claims.append(df[df["similarity"] > threshold])
            

    except ValueError:
        print("Incorrect cutoff value, shutting down")
        exit()
        
    
    
    # Sort claims by similarity and get top results

# Collect the results for the input sentence
results = []
for i in range(len(top_query_claims)):
    for _, claim_row in top_query_claims[i].iterrows():
        results.append({
            "query": "query " + str(i+1),
            'query_text': input_queries[i],
            'claim_review_source': claim_row['claimReview_source'],
            'claim_review': claim_row['claimReview_claimReviewed'],
            'claim_veracity': claim_row['normalised_rating'],
            'similarity': claim_row['similarity'][0][0]
    })

# Step 7: Output results to a CSV file
output_df = pd.DataFrame(results)
output_df.to_csv(config["output_path"], sep='\t', index=False)

print("Results have been saved to " + config["output_path"]) 
