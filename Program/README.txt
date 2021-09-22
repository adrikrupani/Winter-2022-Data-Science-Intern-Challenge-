Author: Adrik Rupani
Project Name: Shopify 2022 Challenge

Description:
        This file contains the written and programed solutions to the proposed problems by shopify. The file titled
        'Written Answers.txt' contains the written answers for each question, it also details the meaning of the data
        outputted in the program. The program file titled 'Challenge Part 1.py' contains the code for all the questions.
        The code is broken down into functions for each part which are called and printed at the end of the code.
        The python file also contain documentation labeling the different processes in the code. Finally, for part two
        of the challenge the file titled 'Challenge 2.txt' contains the SQL statements and their answers.

Files Included:
    For Challenge 1:
        1. 2019 Winter Data Science Intern Challenge Data Set.csv
        2. Challenge Part 1.py
        3. Written Answers.txt
    For Challenge 2:
        4. Challenge 2.txt

Notes For Reviser:
   The following notes contains a brief description of the logic used in the python file 'Challenge Part 1.py'
   The reasoning and the process can be found in the file titled 'Written Answers.txt'

   Question 1:
        1.  For this question I first calculated the provided merit for AOV (Average Order Value).
            This process simply totals the amount earned per order and divides it by the total number of order.
        2.  For my own process I decided to order the amount earned per order in ascending order. Using
            the truncate mean method with a 5% percentile I eliminated 5% of the data on both ends. This removed
            all the outliers in the higher earned end and in the lower earned end. Which leaves us with a group of
            data centered around a tight range. Then using th traditional method of mean calculation the function
            returns the average earned for the middle 90% of the data and the average earned for the 5% of outliers
            on both ends of the high and low range.
   Question 2:
            In this process I take a similar approach where I retrieve the prices of each individual shoe per store
            and total earning per store. Then, when I arrange them in ascending order I can remove outliers in both
            prices and earning. Now that the data only includes the stores that have similar data I calculate their
            pricing brackets. This is done by keeping the ascending order and dividing the data up into 5 bracket.
            Then I iterated through each bracket, took the average price of shoes, the average earnings and divided them.
            This provided a dictionary where the key was the average prices for the bracket and the value was the multiple that
            the merchant in that bracket would earn for their product price.
   Question 3:
        There is no need for explaining question three as it is just the output, its interpretation can be found
        in the file named 'Written Answers.txt'.


