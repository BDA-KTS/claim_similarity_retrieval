# claim_similarity_retrieval

# Description
This method finds claims in a dataset that are similar to a user-provided sentence by comparing their meanings using advanced language embeddings and returning those with a high similarity score.  

### Keywords
claim similarity, claim retrieval, embeddings

### Social Science Usecase

James is a researcher focused on studying misinformation in public discourse, particularly during political events. He has gathered a vast dataset of claims made across various media sources, including news articles and social media posts. To effectively analyze these claims, he wants to identify similar assertions that may spread false narratives. Using the claim similarity method, James inputs a specific claim related to healthcare reform into the system. The method quickly retrieves a list of similar claims from his dataset, allowing him to compare how different sources present the same information. 



### Repository Structure


mdetox.py - The main file to run the project

### Environment Setup
This program requires Python 3.x to run.



  

### How to Use
1. Run the method using python claim_similarity_MH.py
2. Method should ask for user input.
    a) input the sentence similar to which u want to search a claim
   

    b)Output should be the relevant claim/claims
   



### Digital Behavioral data

### Sample Input 
1. List of claims stored in a dataframe
2. User input
   ![image](https://github.com/user-attachments/assets/b24d3fc8-733b-4c8c-9ad3-3541580b3c0a)

### Sample Output
Claim/claims similar to the user inputed claim
![image](https://github.com/user-attachments/assets/d7cb13fb-c04d-4bb0-a3d0-8fe4ecc536d1)

### mdetox pipeline

Embedding Generation: Each sentence in the dataset is encoded into a vector representation using a pre-trained SentenceTransformer model.

User Input: The user provides a sentence, which is also encoded into an embedding.

Cosine Similarity Calculation: The method calculates the cosine similarity between the user input embedding and the embeddings of all sentences in the dataset.

Filtering Results: Sentences with similarity scores above a specified threshold (e.g., 0.85) are filtered out.

Output: The filtered sentences are returned as similar sentences to the user input.



### Limitation

This method may struggle with nuanced meanings and can be computationally intensive for large datasets.



## Contact
Susmita.Gangopadhyay@gesis.org


