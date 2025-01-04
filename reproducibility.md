Reproducibility
The method accepts input text/claims from users and writes the top-3 most similar claims to the input from a dataframe of existing claims.
It uses sentence transformers to get embeddings of both the user input claims and the given dataframe of claims and generates output in a csv file.
It assists in replicability by allowing to execute the method under different settings e.g., with different set of reference claims.
Furthermore, working environment of the method is preserved in requirements.txt file.The necessary details to reuse the method are provided in this document.

Configuration Settings
Update claim_similarity_dataset.tsv file if you want to check similarity with another set of claims

Random Seed Control
NA

Requirements and Environment
The environment details are provided in requirements.txt. Running the pip install command ensures all necessary packages are installed.

Hardware Details
Average runtime: 1-2 minutes for generating embeddings of 74k reference claims and a few seconds to fetch similar claims from them on an 11th Gen Intel Core i7 processor with 16GB RAM (Windows 10).
