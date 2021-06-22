# Entity Matching Unsupervised
It is an Unsupervised Entity Matching used to create train file
and to calculate precision recall and f1 score of datasets

# References

https://github.com/uestc-db/Unsupervised-Entity-Resolution

This is a fork from Unsupervised Entity Resolution.

# Using Entity Matching Unsupervised

1- Run the script Run.sh as:
    
    sh ./Run.sh (DATASET_NAME) (N°BLOCKS)

Number of blocks is not required (setted by default at 20)

2- If you want to store Output in a file and put the two trains files generated from this system run the script Run_and_save.sh as:
    
    sh ./Run_and_save.sh (DATASET_NAME)

it will store the output in a folder.

3- If you just want to store the two trains files generated from this system (train.csv and (dataset_name)_output-unsupervised.csv) run the script Store_train_data.sh as:

    sh ./Store_train_data.sh (DATASET_NAME)