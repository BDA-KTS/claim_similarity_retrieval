# Fact-Checked Claim Retrieval

## Description
This method enables retrieval or searching of fact-checked claims or statements (e.g. taken from online discourse and social media posts). It takes advantage of a unique repository of fact-checked claims mined from the web presented through ClaimsKG which is updated on regular intervals.

ClaimsKG is a structured KnowledgeBase which serves as a registry of claims. The KB is updated at regular intervals. Thea latest release of ClaimsKG contains 74000 claims collected from 13 different fact-checking websites from  the year 1996 to 2023. For more details regarding ClaimsKG like the latest release and related papers, please refer to the official webpage https://data.gesis.org/claimskg/ 

The method receives an input claim/sentence , computes similarity with 74000 previously fact-checked claims from ClaimsKG and returns a set of ranked claims from , their relevance scores, veracity ratings and the corresponding fact-check sources.  

### Method Pipeline

The pipeline consists of the following steps:
![image](https://github.com/user-attachments/assets/b7040304-6db7-4099-83ce-2d498a469f45)





**Embedding Generation**: Each sentence in the dataset is encoded into a vector representation using a pre-trained SentenceTransformer model.

**User Input**: The user provides a sentence, which is also encoded into an embedding.

**Cosine Similarity Calculation**: The method calculates the cosine similarity between the user input embedding and the embeddings of all sentences in the dataset.

**Filtering Results**: Sentences with similarity scores above a specified threshold (e.g., 0.85) are filtered out.

**Output**: The filtered sentences are returned as similar sentences to the user input.

## Keywords
verified claims retrieval, semantic similarity, claims ranking

## Social Science Usecase

1. A social scientist focuses on misinformation in the social media discourse during political events and wants to verify the veracity of a fact-checked claim .
2. A social scientist wants to find out if a claim/statement has been fact-checked before.
3. A social scientist wants to find similar statements/claims that have been previously fact-checked


## Repository Structure
The repository is organised as follows: 

* Files
  - claim_similarity_MH.py: The main file to run the project
  - claim_similarity_dataset.tsv: Dataset of claims
  - sample_input.txt - Sample input of a claim that should be entered to the method to compute the similarity
  - similarity_results.csv - Sample output generated for the sample input file
  - requirements.txt - Text file listing mandatory python packages


 

## Environment Setup
 - This method requires Python 3.9 to run.
 - It also requires the following python packages to be installed namely pandas,sentence_transformers,sklearn and pickle.
 - Sample installation through requirements file
    `>pip install -r requirements.txt`


  

## How to Use
To utilize this tutorial effectively, follow these steps
1. Run the method using the following command: 
   
   `python claim_similarity_MH.py`
   
2. Method will ask for user input.
     - Input the text/input sentence similar to which claims should be fetched
     - If the user doesn't input anything, a default sample sentence is used, and the program informs the user. The default input sentence can be found in the [sample_input.txt](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/sample_input.txt) file

   
3. Output is generated as top 3 relevant and similar claims along with their source, veracity level and similarity score in a csv file

## Input Data 
There are two inputs that are expected to be a part of the method
1. Input Dataset: A dataframe containing a list of claims, from which claims similar to the input must be retrieved.
2. User input: The input claim against which similar claims are searched.
   
### Sample Input 
1. Input Dataset: The [claim_similarity_dataset.tsv](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/claim_similarity_dataset.tsv) already present in the **claim_similarity_retrieval** method. 

   
2. User input: The user input can be provided either by entering it when the script prompts for it:
   
    `Enter a sentence for similarity check (or press Enter to use a sample sentence): Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016.`
   
   or through the file [sample_input.txt](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/sample_input.txt)

## Output Data 
* The output is exported to a csv file [similarity_results.csv](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/similarity_results.csv) and contains the input sentence, normalised rating, similarity , claim source, claim reviewed and message if any
  
  `Results have been saved to similarity_results.csv`
### Sample Output

The program generates a CSV file with the following structure:

| **Input Sentence**                                                   | **Claim Source** | **Claim Reviewed**                                                              | **Normalized Rating** | **Similarity**      | **Message** |
|-----------------------------------------------------------------------|------------------|----------------------------------------------------------------------------------|------------------------|---------------------|--------------|
| Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016. | snopes           | Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016.   | false                 | 1.0000000000000007  |              |
| Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016. | snopes           | Singer and actress Cher died in December 2022 or January 2023.                  | false                 | 0.33357966160385355 |              |

The table captures key details of similarity analysis between the input sentence and claims from the dataset.
               




## Limitation

This method may struggle with nuanced meanings and can be computationally intensive for large datasets. 



## Contact
Susmita.Gangopadhyay@gesis.org


