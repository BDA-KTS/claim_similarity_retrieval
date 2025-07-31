# Fact-Checked Claim Retrieval

## Description
This method enables the retrieval of fact-checked claims or statements, making it particularly useful for analyzing online discourse and social media posts. It leverages ClaimsKG, a structured knowledge base that serves as a registry of fact-checked claims mined from the web. The database is regularly updated, with the latest release containing over 74,000 claims from 13 different fact-checking websites spanning 1996 to 2023. For detailed information about ClaimsKG, including its latest release and related publications, visit the [official webpage](https://data.gesis.org/claimskg/).

The method takes an input claim or sentence from the user, computes its similarity with the fact-checked claims in ClaimsKG, and returns a ranked list of matching claims. The results include relevance scores, veracity labels, and references to the original fact-check sources. The similarity between the input sentence and the claims in ClaimsKG is calculated using [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity). This involves comparing the embedding representations of the input queries and the claims, ensuring accurate and efficient retrieval of relevant fact-checked information.

*Please note that the method use [data/claimsKG_dataset.tsv](data/claimsKG_dataset.tsv) as the ClaimsKG source to retrieve similar claims. For better performance, the precomputed dataset embeddings are loaded from [data/claims_with_embeddings.pkl](data/claims_with_embeddings.pkl). The dataset is subject to change with the newer versions of ClaimsKG.*

## Use Cases

1. Identifying misinformation in the social media discourse during political events to verify the veracity of fact-checked claims
2. Finding claims/statements fact-checked before.
3. Finding similar statements/claims that have been previously fact-checked

## Input Data 
The method reads input data from the file [data/input_queries.txt](data/input_queries.txt), having a query per line.

|    |
|----|
| Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016. |
| The daughter of U.S. Vice President Dick Cheney went to Iraq to become a human shield |

   


## Output Data 
The output is written to [data/similarity_results.tsv](data/similarity_results.tsv) file containing query sequence number, query text, claim_review_source, claim_review, claim_veracity and similarity.

| query	| query_text	| claim_review_source	| claim_review	| claim_veracity	| similarity |
|-------|-------------|---------------------|---------------|-----------------|------------|
| query 1	| Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016.	| snopes	| Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016.	| false	| 1.0000000000000009 |
| query 1	| Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016.	| snopes	| Singer and actress Cher died in December 2022 or January 2023.	| false	| 0.3335796653639739 |
| query 1	| Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016.	| africacheck	| Melon and maize mixture no remedy for irregular periods and other reproductive conditions	| incorrect	| 0.2446108128980326 |
| query 1	| Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016.	| factcheck_afp	| Photo shows a South Korean politician embracing former Japanese Prime Minister Shinzo Abe	| altered image	| 0.17349590630252582 |
| query 1	| Musicians Robert Plant and Cher plan to wed at Westminster Abbey in July 2016.	| snopes	| A picture shows a new animal species that's taking over at Chernobyl.	| miscaptioned	| 0.16520475214575336 |
| query 2	| The daughter of U.S. Vice President Dick Cheney went to Iraq to become a human shield	| snopes	| The daughter of U.S. Vice President Dick Cheney went to Iraq to become a human shield.	| false	| 0.9916974702609328 |
| query 2	| The daughter of U.S. Vice President Dick Cheney went to Iraq to become a human shield	| snopes	| On Sept. 9, 2021, U.S. Rep. Liz Cheney, R-Wyo. responded to former U.S. President Donald Trump's endorsement of GOP challenger Harriet Hagemen, tweeting, Here’s a sound bite for you: Bring it.	| correct attribution	| 0.5197193722483 |
| query 2	| The daughter of U.S. Vice President Dick Cheney went to Iraq to become a human shield	| politifact	| Barack Obama and Hillary Clinton have changed their positions (on the Iraq war withdrawal) to follow Chris Dodd.	| half false	| 0.2727724108612234 |
| query 2	|The daughter of U.S. Vice President Dick Cheney went to Iraq to become a human shield	| politifact	| Barack Obama supported keeping troops in Iraq, but now he wants a precipitous withdrawal regardless of conditions on the ground or consequences of a defeat for the United States, an RNC radio ad.	| half false	| 0.24988936876668902 |
| query 2	| The daughter of U.S. Vice President Dick Cheney went to Iraq to become a human shield	| snopes	| A leaked e-mail revealed Clinton aide Cheryl Mills calling the men who died in Benghazi idiot soldiers and saying she was glad they were tortured.	| false	| 0.24665135811833286 |



The table captures key details of similarity analysis between the input query(ies) and claims texts of the dataset, ranked in decreasing order of their similarity.

*Note: veracity of the claims, i.e., it's labels (as true, mostly true, false etc.) is not considered in evaluating semantic similarity.*

## Hardware Requirements
The method runs on a small virtual machine provided by a cloud computing company (2 x86 CPU core, 4 GB RAM, 40GB HDD).

## Environment Setup
 - This method requires Python 3.9 to run.
 - It also requires the following Python packages to be installed namely pandas, sentence_transformers, sklearn, and pickle.
 - Sample installation through requirements file
   
    `pip install -r requirements.txt`

## How to Use
To utilize this tutorial effectively, follow these steps

1. Run the method using the following command: 
   
   `python claim_similarity_retrieval.py`
   
*By default, the method uses topK results (with K=5). Feel free to toggle between topK and threshold as cutoff with different values.*
   
## Technical Details
This tool provides a practical solution for verifying information, combating misinformation, and supporting research in the field of online content validation.

The embedding model used in this method is [SentenceTransformer](https://github.com/UKPLab/sentence-transformers) with the [paraphrase-MiniLM-L6-v2](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html) pre-trained model.
Using the **paraphrase-MiniLM-L6-v2** model ensures reproducibility by providing a standardized, pre-trained, and widely used model that generates consistent sentence embeddings. This version is deterministic, meaning the same input will always produce the same output, regardless of the environment, as long as the model version remains the same. It is publicly available, easy to load from GitHub, and documented for clarity, making it straightforward for others to replicate experiments and results with the same setup.

## References
Gangopadhyay, S., Schellhammer, S., Hafid, S., Dessi, D., Koß, C., Todorov, K., ... & Jabeen, H. (2024, September). Investigating characteristics, biases and evolution of fact-checked claims on the web. In Proceedings of the 35th ACM Conference on Hypertext and Social Media (pp. 246-258).

## Disclaimer
This method may struggle with nuanced meanings and can be computationally intensive for large datasets. 


## Contact Details
For questions or feedback, contact Susmita Gangopadhyay via [Susmita.Gangopadhyay@gesis.org](mailto:Susmita.Gangopadhyay@gesis.org).


