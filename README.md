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
  - claim_similarity_dataset.tsv: Sample input dataset of claims


 

### Environment Setup
This method requires Python 3.x to run.

  

### How to Use :To utilize this tutorial effectively, follow these steps
1. Run the method using the following command: 
   
   `python claim_similarity_MH.py`
   
2. Method should ask for user input.
     - Input the name of the file that contains text/input sentences similar to which claims should be fetched

   
3. Output is generated as top 3 relevant and similar claims along with their source, veracity level and similarity score

   
### Sample Input 
1. List of claims stored in a dataframe .
    - For example, the claim_similarity_dataset.tsv already present in the **claim_similarity_retrieval** method. 

   
3. User input
   
    `Enter the name of the input file (CSV or TSV) located in the current directory: input.csv`

   The input file should look like

                input_sentence  | 
                  ------------- | 
                Joe Biden Donald Trump  | 
                Ukraine Russia  |  


### Sample Output
* Claim/claims similar to the user inputed claim

input_sentence | claimReview_source | claimReview_claimReviewed|  <div style="width:290px">normalised_rating</div>|<div style="width:290px">similarity</div> | message                                                                                              
---------------|-------------------|---------------------------|------------------|---------------------|--------------------  
Joe Biden Donald trump   | checkyourfact     | A video shared on Facebook purports...                           | false            | 0.3887              | No claims are found to be very similar (above 0.7), however, the top 3 are displayed.               
Joe Biden Donald trump   | politifact        | "Barack Obama supported keeping troops...                        | mixture          | 0.3292              | No claims are found to be very similar (above 0.7), however, the top 3 are displayed.               
Joe Biden Donald trump   | truthorfiction    | "Ivanka Trump quoted Thomas Jefferson to her...                  | other            | 0.2931              | No claims are found to be very similar (above 0.7), however, the top 3 are displayed.               
Ukraine Russia          | checkyourfact     | A video shared on Facebook claims to show...                     | false            | 0.5271              | No claims are found to be very similar (above 0.7), however, the top 3 are displayed.               
Ukraine Russia          | africacheck       | "Marburg virus disease unrelated to Covid-19...                 | false            | 0.2993              | No claims are found to be very similar (above 0.7), however, the top 3 are displayed.               
Ukraine Russia          | checkyourfact     | A video shared on Facebook claims to show a...                  | false            | 0.2972              | No claims are found to be very similar (above 0.7), however, the top 3 are displayed.               



  
* The output is also exported to a csv file
  
  `Results have been saved to similarity_results.csv`




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


