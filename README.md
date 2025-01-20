# Fact-Checked Claim Retrieval

## Description


This method enables the retrieval of fact-checked claims or statements, making it particularly useful for analyzing online discourse and social media posts. It leverages ClaimsKG, a structured knowledge base that serves as a registry of fact-checked claims mined from the web. The database is regularly updated, with the latest release containing over 74,000 claims from 13 different fact-checking websites spanning 1996 to 2023. For detailed information about ClaimsKG, including its latest release and related publications, visit the [official webpage](https://data.gesis.org/claimskg/).

The method takes an input claim or sentence from the user, computes its similarity with the fact-checked claims in ClaimsKG, and returns a ranked list of matching claims. The results include relevance scores, veracity ratings, and references to the original fact-check sources.

The similarity between the input sentence and the claims in ClaimsKG is calculated using [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity). This involves comparing the embedding representations of the input and the claims, ensuring accurate and efficient retrieval of relevant fact-checked information.

This tool provides a practical solution for verifying information, combating misinformation, and supporting research in the field of online content validation.

**Reproducibility:** The embedding model used in this method is [SentenceTransformer](https://github.com/UKPLab/sentence-transformers) with the [paraphrase-MiniLM-L6-v2](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html) pre-trained model.
Using the **paraphrase-MiniLM-L6-v2** model ensures reproducibility by providing a standardized, pre-trained, and widely used model that generates consistent sentence embeddings. This version is deterministic, meaning the same input will always produce the same output, regardless of the environment, as long as the model version remains the same. It is publicly available, easy to load from Github, and documented for clarity, making it straightforward for others to replicate experiments and results with the same setup.


## Social Science Use Case(s)

1. A social scientist focuses on misinformation in the social media discourse during political events and wants to verify the veracity of a fact-checked claim.
2. A social scientist wants to find out if a claim/statement has been fact-checked before.
3. A social scientist wants to find similar statements/claims that have been previously fact-checked


## Repository Structure
The repository is organized as follows: 

* Files
  - [claim_similarity_retrieval.py](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/claim_similarity_retrieval.py): The main file to run the project
  - [claim_similarity_dataset.tsv](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/claim_similarity_dataset.tsv): Dataset of claims
  - [sample_input.txt](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/sample_input.txt) - Sample input of a claim that should be entered to the method to compute the similarity
  - [similarity_results.csv](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/similarity_results.csv) - Sample output generated for the sample input file
  - [requirements.txt](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/requirements.txt) - Text file listing mandatory python packages


 

## Environment Setup
 - This method requires Python 3.9 to run.
 - It also requires the following Python packages to be installed namely pandas, sentence_transformers, sklearn, and pickle.
 - Sample installation through requirements file
   
    `pip install -r requirements.txt`


  

## How to Use
To utilize this tutorial effectively, follow these steps
1. Run the method using the following command: 
   
   `python claim_similarity_retrieval.py`
   
2. The method will ask for user input.
     - Input the text/input sentence similar to which claims should be fetched
     - If the user doesn't input anything, a default sample sentence is used, and the program informs the user. The default input sentence can be found in the [sample_input.txt](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/sample_input.txt) file

   
3. Output is generated as the top 3 relevant and similar claims along with their source, veracity level, and similarity score in a CSV file

## Input Data 
There are two inputs that are expected to be a part of the method
1. Source dataset: A collection of claims to retrieve similar claims from, for given user query. The default is [claim_similarity_dataset.tsv](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/claim_similarity_dataset.tsv). 
2. User input query: The inputs a query against which similar claims are searched in the source dataset.
   
### Sample Input 
1. Source dataset: The [claim_similarity_dataset.tsv](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/claim_similarity_dataset.tsv) already present in the **claim_similarity_retrieval** method. 
2. User input query: The user input query can be provided either by entering it when the script prompts for it:
   
    `Enter a sentence for similarity check (or press Enter to use a sample sentence): Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016.`
   
   or through the file [sample_input.txt](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/sample_input.txt)

## Output Data 
* The output is exported to a CSV file [similarity_results.csv](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/similarity_results.csv) and contains the input sentence, normalized rating, similarity scores, claims source, claims reviewed, and messages if any.
  
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
For questions or feedback, contact Susmita Gangopadhyay via [Susmita.Gangopadhyay@gesis.org](mailto: Susmita.Gangopadhyay@gesis.org).


