# claim_similarity_retrieval

## Description
This method enables fact-checking of arbitrary claims or statements (e.g. taken from online discourse and social media posts). It takes advantage of a unique and constantly updated repository of fact-checked claims mined from the web (ClaimsKG). The method receives an input claim/sentence and returns a set of ranked claims, their relevance scores, veracity ratings and the corresponding fact-check sources.   

### Keywords
verified claims retrieval, semantic similarity, claims ranking

### Social Science Usecase

A social scientist focuses on misinformation in the social media discourse during political events and wants to verify the veracity of a claim a post using the latest ClaimsKG release of verified facts. 

### Repository Structure
The repository is organised as follows: 

* Files
  - claim_similarity_MH.py: The main file to run the project
  - claim_similarity_dataset.tsv: Sample input dataset


 

### Environment Setup
This method requires Python 3.x to run.

  

### How to Use :To utilize this tutorial effectively, follow these steps
1. Run the method using the following command: 
   
   `python claim_similarity_MH.py`
   
2. Method should ask for user input.
     - Input the sentence similar to which you want to search a claim

     - Input the number of top similar claims
   
3. Output is generated as relevant claim/claims

   
### Sample Input 
1. List of claims stored in a dataframe .
    - For example, the claim_similarity_dataset.tsv already present in the **claim_similarity_retrieval** method. 

   
3. User input
   
    `Enter a sentence: Joe Biden Donald Trump`

    `Enter the number of top similar claims to display (default 3) :2`
   



### Sample Output
* Claim/claims similar to the user inputed claim
  
   ´Top 2 most similar claims´

   | claimReview_source  | Claim  | Normalised_rating  | Similarity  |
   |---------------|----------------|---------------|---------------|
   |checkyourfact  | A video shared on Facebook purports Iowa Repub...   | false  |  0.410853  |
   | politifact  | Barack Obama supported keeping troops in Iraq,... | mixture  | 0.368890  |


  
* The output is also exported to a csv file
  
  `Output exported successfully as output.csv`




### Method pipeline

The pipeline consists of the following steps:
![image](https://github.com/user-attachments/assets/b7040304-6db7-4099-83ce-2d498a469f45)





**Embedding Generation**: Each sentence in the dataset is encoded into a vector representation using a pre-trained SentenceTransformer model.

**User Input**: The user provides a sentence, which is also encoded into an embedding.

**Cosine Similarity Calculation**: The method calculates the cosine similarity between the user input embedding and the embeddings of all sentences in the dataset.

**Filtering Results**: Sentences with similarity scores above a specified threshold (e.g., 0.85) are filtered out.

**Output**: The filtered sentences are returned as similar sentences to the user input.



### Limitation

This method may struggle with nuanced meanings and can be computationally intensive for large datasets.



## Contact
Susmita.Gangopadhyay@gesis.org


