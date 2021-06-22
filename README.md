# Entity Matching Unsupervised
It is an Unsupervised Entity Matching used to create train file
and to calculate precision recall and f1 score of datasets

# References

https://github.com/uestc-db/Unsupervised-Entity-Resolution

This is a fork from Unsupervised Entity Resolution.

# Using Entity Matching Unsupervised

1- Run the script Run.sh as:
    
    sh ./Run.sh (DATASET_NAME) (N°BLOCKS)

Number of blocks is not required (set by default at 20)

2- If you want to store the Output in a file and include the two train files generated from this system run the script Run_and_save.sh as:
    
    sh ./Run_and_save.sh (DATASET_NAME)

it will store the output in a folder.

3- If you just want to store the two train files generated from this system (train.csv and (dataset_name)_output-unsupervised.csv) run the script Store_train_data.sh as:

    sh ./Store_train_data.sh (DATASET_NAME)


# Contents of 'output' folder

Inside the 'output' folder are stored the files processed by Entity Matching Unsupervised.
In particular we can see three type of files:

1- DATASET_NAME.txt -> in this file, the output of precompiled datasets is stored by running "Run_and_save.sh".

2- Inside every dataset folder we find two types of files:

    a- DATASET_NAME_output-unsupervised.csv -> in this file are stored the tuples that the system found. The format is:
        ltable_id,rtable_id,label
    
    b- train.csv -> this file instead contains the previous file but it will be processed in this way:
        - removing similar tuple from train taken from test.csv
        - adding random tuples with 0 label