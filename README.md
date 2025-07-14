# Fact-Checked Claim Retrieval

## Description
This method enables the retrieval of fact-checked claims or statements, making it particularly useful for analyzing online discourse and social media posts. It leverages ClaimsKG, a structured knowledge base that serves as a registry of fact-checked claims mined from the web. The database is regularly updated, with the latest release containing over 74,000 claims from 13 different fact-checking websites spanning 1996 to 2023. For detailed information about ClaimsKG, including its latest release and related publications, visit the [official webpage](https://data.gesis.org/claimskg/).

The method takes an input claim or sentence from the user, computes its similarity with the fact-checked claims in ClaimsKG, and returns a ranked list of matching claims. The results include relevance scores, veracity ratings, and references to the original fact-check sources. The similarity between the input sentence and the claims in ClaimsKG is calculated using [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity). This involves comparing the embedding representations of the input and the claims, ensuring accurate and efficient retrieval of relevant fact-checked information.

## Use Cases

1. A social scientist focuses on misinformation in the social media discourse during political events and wants to verify the veracity of a fact-checked claim.
2. A social scientist wants to find out if a claim/statement has been fact-checked before.
3. A social scientist wants to find similar statements/claims that have been previously fact-checked

## Input Data 
User input query: The method asks the user for input query as a sentence or phrase to retrieve claims similar to it. 

Please note that the method use [claim_similarity_dataset.tsv](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/claim_similarity_dataset.tsv) as the ClaimsKG source to retrieve similar claims. It is subject to change with the newer versions of ClaimsKG.   


## Output Data 
The output is exported to a CSV file [similarity_results.csv](https://github.com/BDA-KTS/claim_similarity_retrieval/blob/main/similarity_results.csv) and contains the input sentence, normalized rating, similarity scores, claims source, claims reviewed, and messages if any.
  
The program generates a CSV file with the following structure:

| **Input Sentence**                                                   | **Claim Source** | **Claim Reviewed**                                                              | **Normalized Rating** | **Similarity**      | **Message** |
|-----------------------------------------------------------------------|------------------|----------------------------------------------------------------------------------|------------------------|---------------------|--------------|
| Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016. | snopes           | Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016.   | false                 | 1.0000000000000007  |              |
| Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016. | snopes           | Singer and actress Cher died in December 2022 or January 2023.                  | false                 | 0.33357966160385355 |              |

The table captures key details of similarity analysis between the input query(ies) and claims texts of the dataset, ranked in decreasing order of their similarity.

*Note: *veracity of the claims i.e., its labels (as true, mostly true, false etc.) are not considered in evaluating semantic similarity.

## Hardware Requirements
The method runs on a cheap virtual machine provided by cloud computing company (2 x86 CPU core, 4 GB RAM, 40GB HDD).

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

## Technical Details
This tool provides a practical solution for verifying information, combating misinformation, and supporting research in the field of online content validation.

The embedding model used in this method is [SentenceTransformer](https://github.com/UKPLab/sentence-transformers) with the [paraphrase-MiniLM-L6-v2](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html) pre-trained model.
Using the **paraphrase-MiniLM-L6-v2** model ensures reproducibility by providing a standardized, pre-trained, and widely used model that generates consistent sentence embeddings. This version is deterministic, meaning the same input will always produce the same output, regardless of the environment, as long as the model version remains the same. It is publicly available, easy to load from Github, and documented for clarity, making it straightforward for others to replicate experiments and results with the same setup.

## Disclaimer
This method may struggle with nuanced meanings and can be computationally intensive for large datasets. 


## Contact Details
For questions or feedback, contact Susmita Gangopadhyay via [Susmita.Gangopadhyay@gesis.org](mailto:Susmita.Gangopadhyay@gesis.org).


